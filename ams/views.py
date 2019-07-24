from django.shortcuts import render
from ams.models import User, AccreditingBody, Files, Team, DegreeProgram, DocumentOutline, DocumentOutlineItem, \
    CompletedAccreditation, PrevAccreditation
from ams.forms import UserForm, AccreditingBodyForm, FileForm, TeamForm, DegreeProgramForm, DocumentOutlineForm, \
    DocumentOutlineItemForm, \
    CompletedAccreditationForm, PrevAccreditationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def base(request):
    return render(request, 'ams/base.html')


def login(request):
    return render(request, 'ams/login.html')


def register(request):
    return render(request, 'ams/register.html')


def dash(request):
    return render(request, 'ams/dash.html')


def addagency(request):
    return render(request, 'ams/addagency.html')


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
        return render(request, 'ams/createdocuoutline.html', {
            "accrediting_bodies": accrediting_bodies
        })

    form = json.loads(request.body)
    document_outline = DocumentOutline.objects.create(accrediting_body_id=accrediting_bodies.get(id=form["agency"]), document_name=form["title"])
    for section in form["sections"]:
        save_section(section, document_outline, None)

    return JsonResponse({}, status=200)

def docuoutlinelist(request):
    return render(request, 'ams/docuoutlinelist.html')


def viewdocuoutline(request):
    return render(request, 'ams/viewdocuoutline.html')


def addprogram(request):
    return render(request, 'ams/addprogram.html')


def programlist(request):
    return render(request, 'ams/programlist.html')


def viewprogram(request):
    return render(request, 'ams/viewprogram.html')


def createperiod(request):
    return render(request, 'ams/createperiod.html')


def createteam(request):
    return render(request, 'ams/createteam.html')


def accreditationlist(request):
    return render(request, 'ams/accreditationlist.html')


def viewaccreditation(request):
    return render(request, 'ams/viewaccreditation.html')


def teamlist(request):
    return render(request, 'ams/teamlist.html')


def ongoinglist(request):
    return render(request, 'ams/ongoinglist.html')


def viewongoing(request):
    return render(request, 'ams/viewongoing.html')


def ansdocu(request):
    return render(request, 'ams/ansdocu.html')


def docurepo(request):
    return render(request, 'ams/filerepo.html')


def filerepo(request):
    return render(request, 'ams/filerepo.html')


def userlist(request):
    return render(request, 'ams/userlist.html')
