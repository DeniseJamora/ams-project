from django import forms
from .models import User, AccreditingBody, Files, DegreeProgram, DocumentOutline, DocumentOutlineItem, \
    CompletedAccreditation, PrevAccreditation


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "user_email",
            "user_password",
            "user_givenName",
            "user_middleInitial",
            "user_surname",
            "user_type",
        ]


class AccreditingBodyForm(forms.ModelForm):
    class Meta:
        model = AccreditingBody
        fields = [
            "accrediting_body",
        ]


class FileForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = [
            "file_name",
            "file_type",
            "file_document",
        ]


class TeamForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = [
            "team_name",
        ]


class DegreeProgramForm(forms.ModelForm):
    class Meta:
        Model = DegreeProgram
        fields = [
            "program_code",
            "program_name",
            "program_est",
            "program_grade",
        ]


class DocumentOutlineForm(forms.ModelForm):
    class Meta:
        Model = DocumentOutline
        fields = [
            "document_name",
        ]


class DocumentOutlineItemForm(forms.ModelForm):
    class Meta:
        Model = DocumentOutlineItem
        fields = [
            "item_title",
            "item_type",
        ]


class CompletedAccreditationForm(forms.ModelForm):
    class Meta:
        Model = CompletedAccreditation
        fields = [
            "completed_result",
            "completed_year",
        ]


class PrevAccreditationForm(forms.ModelForm):
    class Meta:
        Model = PrevAccreditation
        fields = [
            "accreditation_agency",
            "accreditation_result",
            "accreditation_year",
        ]
