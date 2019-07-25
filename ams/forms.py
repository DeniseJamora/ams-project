from django import forms
from .models import User, AccreditingBody, Files, Team, DegreeProgram, DocumentOutline, DocumentOutlineItem, \
    CompletedAccreditation, PrevAccreditation


class UserForm(forms.ModelForm):

    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email',}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username',}))
    given_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-6', 'placeholder':'Given Name',}))
    middle_initial = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-3', 'placeholder':'Middle Initial',}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-3', 'placeholder':'Surname',}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password',}))
    type = forms.CharField(widget=forms.Select(attrs={'class':'form-control', 'id':'type'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'given_name', 'middle_initial', 'surname', 'password', 'type',)


class AccreditingBodyForm(forms.ModelForm):
    accrediting_body = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'e.g. PAASCU',}))

    class Meta:
        model = AccreditingBody
        fields = ('accrediting_body',)


class DegreeProgramForm(forms.ModelForm):
    program_code = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'e.g. BS INSYS',}))
    program_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'e.g. BS Information Systems',}))
    program_est = forms.CharField(widget=forms.Select(attrs={'class':'form-control', 'id':'year',}))
    program_grads = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'e.g. 5',}))

    class Meta:
        model = DegreeProgram
        fields = ('program_code', 'program_name', 'program_est', 'program_grads',)


class PrevAccreditationForm(forms.ModelForm):
    accreditation_agency = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'e.g. BS INSYS',}))
    accreditation_result = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'e.g. BS Information Systems',}))
    accreditation_year = forms.CharField(widget=forms.Select(attrs={'class':'form-control', 'id':'year',}))

    class Meta:
        model = PrevAccreditation
        fields = ('accreditation_agency', 'accreditation_result', 'accreditation_year')


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
        model = Team
        fields = [
            "team_name",
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
