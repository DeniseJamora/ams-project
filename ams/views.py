from django.shortcuts import render, redirect, render_to_response
from django.contrib import auth
from .models import User, AccreditingBody, File, Team, DegreeProgram, DocumentOutline, DocumentOutlineItem, \
    CompletedAccreditation, PrevAccreditation, UserTeam
from .forms import UserForm, AccreditingBodyForm, FileForm, TeamForm, DegreeProgramForm, DocumentOutlineForm, \
    DocumentOutlineItemForm, \
    CompletedAccreditationForm, PrevAccreditationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.


def login(request):
    if request.method == 'POST':
        u = auth.authenticate(email=request.POST.get('email'), password=request.POST.get('password'))
        if u is not None:
            auth.login(request, u)
            return redirect('dash')
        else:
            return render(request, 'ams/login.html', {'error': 'Email or password is incorrect'})
    else:
        return render(request, 'ams/login.html')


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            if request.POST['password'] == request.POST['confirm_password']:
                form.save()
                return redirect('login')
            else:
                return render(request, 'ams/register.html', {'form': form, 'error': 'Passwords do not match'})
    else:
        form = UserForm()
        return render(request, 'ams/register.html', {'form': form})


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')


def dash(request):
    return render(request, 'ams/dash.html')


def addagency(request):
    if request.method == "POST":
        form = AccreditingBodyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addagency')
    else:
        form = AccreditingBodyForm()
        return render(request, 'ams/admin/addagency.html', {'form': form})


@csrf_exempt
def createdocuoutline(request):
    accrediting_bodies = AccreditingBody.objects.all()

    def save_section(section_form, document_outline_id, parent):
        doc_outline_item = DocumentOutlineItem.objects.create(document_outline_id=document_outline_id,
                                                              parent_document_outline_item_id=parent,
                                                              item_title=section_form["title"],
                                                              item_type=section_form["section"])

        for subsection in section_form["subsections"]:
            save_section(subsection, document_outline_id, doc_outline_item)

    if request.method == 'GET':
        return render(request, 'ams/admin/createdocuoutline.html', {
            "accrediting_bodies": accrediting_bodies
        })

    form = json.loads(request.body)
    document_outline = DocumentOutline.objects.create(accrediting_body_id=accrediting_bodies.get(id=form["agency"]),
                                                      document_name=form["title"])
    for section in form["sections"]:
        save_section(section, document_outline, None)

    return JsonResponse({}, status=200)


def docuoutlinelist(request):
    outlines = DocumentOutline.objects
    return render(request, 'ams/config/docuoutlinelist.html', {'outlines':outlines})


def viewdocuoutline(request):
    return render(request, 'ams/config/viewdocuoutline.html')


def addprogram(request):
    if request.method == "POST":
        form = DegreeProgramForm(request.POST)
        if form.is_valid():
            if request.POST['prev_acc'] == "Yes":
                f = request.POST['program_name']
                form.save()
                return redirect('programprev', f)
            else:
                form.save()
                return redirect('programlist')
    else:
        form = DegreeProgramForm()
        program_form = PrevAccreditationForm()
        return render(request, 'ams/admin/addprogram.html', {
            'form': form,
            'program_form': program_form
        })


def programprev(request, f):
    programs = DegreeProgram.objects.get(program_name=f)
    if request.method == 'POST':
        form = PrevAccreditationForm(request.POST)
        if form.is_valid():
            a = form.save(commit=False)
            a.degree_program_id = programs.id
            a.save()
            return redirect('programlist')
    else:
        form = PrevAccreditationForm(request.POST)
        return render(request, 'ams/admin/programprev.html', {'programs': programs, 'form': form})


def programlist(request):
    programs = DegreeProgram.objects
    return render(request, 'ams/admin/programlist.html', {'programs': programs})


def viewprogram(request, pk):
    program = DegreeProgram.objects.get(id=pk)
    prevs = PrevAccreditation.objects.filter(degree_program_id=pk)

    return render(request, 'ams/admin/viewprogram.html', {'program': program, 'prevs': prevs})


def createperiod(request):
    return render(request, 'ams/config/createperiod.html')


def createteam(request):
    return render(request, 'ams/config/createteam.html')


def accreditationbase(request):
    return render(request, 'ams/accreditationbase.html')


def accreditationlist(request):
    return render(request, 'ams/config/accreditationlist.html')


def viewaccreditation(request):
    return render(request, 'ams/config/viewaccreditation.html')


def teamlist(request):
    teams = Team.objects
    members = UserTeam.objects
    return render(request, 'ams/config/teamlist.html', {'teams':teams, 'members':members})


def ongoinglist(request):
    return render(request, 'ams/config/ongoinglist.html')


def viewongoing(request):
    return render(request, 'ams/config/viewongoing.html')


def ansdocu(request):
    return render(request, 'ams/ansdocu.html')


def filerepo(request):
    return render(request, 'ams/filerepo.html')


def userlist(request):
    users = User.objects
    teams = UserTeam.objects
    return render(request, 'ams/admin/userlist.html', {'users':users}, {'teams':teams})