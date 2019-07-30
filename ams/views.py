from django.shortcuts import render, redirect, render_to_response
from django.contrib import auth
from .models import User, AccreditingBody, File, Team, DegreeProgram, DocumentOutline, DocumentOutlineItem, \
    CompletedAccreditation, PrevAccreditation, UserTeam, Evidences, AccreditationPeriod, OutlineCriteria
from .forms import UserForm, AccreditingBodyForm, FileForm, TeamForm, DegreeProgramForm, DocumentOutlineForm, \
    DocumentOutlineItemForm, \
    CompletedAccreditationForm, PrevAccreditationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            if request.POST['password'] == request.POST['confirm_password']:
                form = form.save()
                form.set_password(request.POST['password'])
                form.save()
                return redirect('login')
            else:
                return render(request, 'ams/register.html', {'form': form, 'error': 'Passwords do not match'})
    else:
        form = UserForm()
        return render(request, 'ams/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        u = auth.authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if u is not None:
            auth.login(request, u)
            return redirect('dash')
        else:
            return render(request, 'ams/login.html', {'error': 'Username or password is incorrect'})
    else:
        return render(request, 'ams/login.html')


@login_required
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')


@login_required
def dash(request):
    user = User.objects.all()
    context = {'username': user}
    return render(request, 'ams/dash.html', context)


@login_required
def addagency(request):
    if request.method == "POST":
        form = AccreditingBodyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addagency')
    else:
        form = AccreditingBodyForm()
        return render(request, 'ams/admin/addagency.html', {'form': form})


@login_required
@csrf_exempt
def createdocuoutline(request):
    accrediting_bodies = AccreditingBody.objects.all()

    def save_section(section_form, document_outline_id, parent):
        doc_outline_item = DocumentOutlineItem.objects.create(document_outline_id=document_outline_id,
                                                              parent_document_outline_item_id=parent,
                                                              item_title=section_form["title"])

        if(section_form.get("subsections")):
            for subsection in section_form["subsections"]:
                save_section(subsection, document_outline_id, doc_outline_item)

            # if(subsection.get("sections") == 'Criteria'):
            #     OutlineCriteria.objects.create(outline_criteria_text=subsection.get("title"), document_outline=document_outline_id, document_outline_item=doc_outline_item)

            # if(subsection.get("criteria")):
            #     criteria = subsection.get("criteria")
                # if(criteria.get("evidences")):
                #     evidences = criteria.get("evidences")
                #     for evidence in evidences:
                #         Evidences.objects.create(evidences_text=evidence, document_outline_item=doc_outline_item)

    if request.method == 'POST':
        form = json.loads(request.body)
        document_outline = DocumentOutline.objects.create(accrediting_body_id=accrediting_bodies.get(id=form["agency"]),
                                                        document_name=form["title"])
        for section in form["sections"]:
            save_section(section, document_outline, None)

        return JsonResponse({}, status=200)

    elif request.method == 'GET':
        return render(request, 'ams/admin/createdocuoutline.html', {
            "accrediting_bodies": accrediting_bodies
        })

@login_required
def setcriteria(request):
    return render(request, 'ams/admin/setcriteria.html')


@login_required
def docuoutlinelist(request):
    outlines = DocumentOutline.objects
    return render(request, 'ams/config/docuoutlinelist.html', {'outlines': outlines})


@login_required
def viewdocuoutline(request):
    return render(request, 'ams/config/viewdocuoutline.html')


@login_required
def addprogram(request):
    if request.method == "POST":
        form = DegreeProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('programlist')
    else:
        form = DegreeProgramForm()
        program_form = PrevAccreditationForm()
        return render(request, 'ams/admin/addprogram.html', {
            'form': form,
            'program_form': program_form
        })


@login_required
def programlist(request):
    programs = DegreeProgram.objects
    return render(request, 'ams/admin/programlist.html', {'programs': programs})


@login_required
def viewprogram(request, pk):
    program = DegreeProgram.objects.get(id=pk)
    return render(request, 'ams/admin/viewprogram.html', {'program': program})


@login_required
def createperiod(request):
    if request.method == "POST":
        accreditation_period_id = AccreditationPeriod.objects.create(
                                                agency_id=request.POST['agency'],
                                                type=request.POST['accred_type'],
                                                document_id=request.POST['document'],
                                                degree_program_id=request.POST['program'],
                                                onsite_date=request.POST['end_date'],
                                                end_date=request.POST['end_date'])
        users = User.objects.all()
        documents = DocumentOutlineItem.objects.filter(document_outline_id_id=request.POST['document'])
        # outline_criteria = OutlineCriteria.objects.filter(outline_criteria_text=subsection.get("title"), document_outline=document_outline_id, document_outline_item=doc_outline_item)
        return render(request, 'ams/config/createteam.html', {'accreditation': accreditation_period_id, 'users': users, 'documents': documents})
    else:
        agency = AccreditingBody.objects.all()
        outlines = DocumentOutline.objects.all()
        programs = DegreeProgram.objects.all()

        return render(request, 'ams/config/createperiod.html', {'agency': agency, 'outlines': outlines, 'programs': programs})


@login_required
def createteam(request):
    if request.method == "POST":
        return render(request, 'ams/config/createteam.html')
    else:
        return render(request, 'ams/config/createteam.html')


@login_required
def assigncriteria(request):
    return render(request, 'ams/config/assigncriteria.html')


@login_required
def setdeadlines(request):
    return render(request, 'ams/config/setdeadlines.html')


@login_required
def accreditationbase(request):
    return render(request, 'ams/accreditationbase.html')


@login_required
def accreditationlist(request):
    return render(request, 'ams/config/accreditationlist.html')


@login_required
def viewaccreditation(request):
    return render(request, 'ams/config/viewaccreditation.html')


@login_required
def teamlist(request):
    teams = Team.objects
    members = UserTeam.objects
    return render(request, 'ams/config/teamlist.html', {'teams': teams, 'members': members})


@login_required
def ongoinglist(request):
    return render(request, 'ams/config/ongoinglist.html')


@login_required
def viewongoing(request):
    return render(request, 'ams/config/viewongoing.html')


@login_required
def evidencelist(request):
    return render(request, 'ams/evidencelist.html')


@login_required
def ansdocu(request):
    return render(request, 'ams/ansdocu.html')


@login_required
def uploadevidence(request):
    return render(request, 'ams/uploadevidence.html')


@login_required
def approveevidence(request):
    return render(request, 'ams/approveevidence.html')


@login_required
def deadlines(request):
    return render(request, 'ams/deadlines.html')


@login_required
def docurepo(request):
    return render(request, 'ams/filerepo.html')


@login_required
def filerepo(request):
    return render(request, 'ams/filerepo.html')


@login_required
def finalizedocument(request):
    return render(request, 'ams/finalizedocument.html')


@login_required
def userlist(request):
    users = User.objects
    return render(request, 'ams/admin/userlist.html', {'users': users})


@login_required
def agencylist(request):
    agencies = AccreditingBody.objects
    return render(request, 'ams/admin/agencylist.html', {'agencies': agencies})
