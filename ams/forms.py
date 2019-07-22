from django import forms
from .models import user, accrediting_body, files, degree_program, document_outline, document_outline_item, \
    completed_accreditation, prev_accreditation


class UserForm(forms.ModelForm):
    class Meta:
        model = user
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
        model = accrediting_body
        fields = [
            "accrediting_body",
        ]


class FileForm(forms.ModelForm):
    class Meta:
        model = files
        fields = [
            "file_name",
            "file_type",
            "file_document",
        ]


class TeamForm(forms.ModelForm):
    class Meta:
        model = files
        fields = [
            "team_name",
        ]


class DegreeProgramForm(forms.ModelForm):
    class Meta:
        Model = degree_program
        fields = [
            "program_code",
            "program_name",
            "program_est",
            "program_grade",
        ]


class DocumentOutlineForm(forms.ModelForm):
    class Meta:
        Model = document_outline
        fields = [
            "document_name",
        ]


class DocumentOutlineItemForm(forms.ModelForm):
    class Meta:
        Model = document_outline_item
        fields = [
            "item_title",
            "item_type",
        ]


class CompletedAccreditationForm(forms.ModelForm):
    class Meta:
        Model = completed_accreditation
        fields = [
            "completed_result",
            "completed_year",
        ]


class PrevAccreditationForm(forms.ModelForm):
    class Meta:
        Model = prev_accreditation
        fields = [
            "accreditation_agency",
            "accreditation_result",
            "accreditation_year",
        ]
