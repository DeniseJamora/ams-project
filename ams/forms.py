from django import forms
from .models import User, AccreditingBody, File, Team, DegreeProgram, DocumentOutline, DocumentOutlineItem, \
     CompletedAccreditation, PrevAccreditation
from django_select2.forms import Select2MultipleWidget

class UserForm(forms.ModelForm):
    user_type = (
        ('', 'Please Select Type'),
        ('survey-executive', 'Survey Executive'),
        ('member', 'Member'),
    )
    departments = (
        ('', 'Please Select Department'),
        ('comp-tech', 'Computer Technology Dept'),
        ('soft-tech', 'Software Technology Dept'),
    )
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email',}))
    dept = forms.CharField(widget=forms.Select(attrs={'class':'form-control',},choices=departments))
    given_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-6', 'placeholder':'Given Name',}))
    middle_initial = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-3', 'placeholder':'Middle Initial',}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-3', 'placeholder':'Surname',}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password',}))
    type = forms.CharField(widget=forms.Select(attrs={'class':'form-control', 'id':'type'},choices=user_type))

    class Meta:
        model = User
        fields = ('email', 'dept', 'given_name', 'middle_initial', 'surname', 'password', 'type',)


class AccreditingBodyForm(forms.ModelForm):
    accrediting_body = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'e.g. PAASCU',}))

    class Meta:
        model = AccreditingBody
        fields = ('accrediting_body',)


class DegreeProgramForm(forms.ModelForm):
    program_code = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'e.g. BS INSYS',}))
    program_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'e.g. BS Information Systems',}))

    class Meta:
        model = DegreeProgram
        fields = ('program_code', 'program_name',)


class PrevAccreditationForm(forms.ModelForm):
    accreditation_agency = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'e.g. BS INSYS',}))
    accreditation_result = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'e.g. BS Information Systems',}))
    accreditation_year = forms.CharField(widget=forms.Select(attrs={'class':'form-control', 'id':'year',}))

    class Meta:
        model = PrevAccreditation
        fields = ('accreditation_agency', 'accreditation_result', 'accreditation_year')


class FileForm(forms.ModelForm):
    class Meta:
        model = File
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
        ]


class CompletedAccreditationForm(forms.ModelForm):
    class Meta:
        Model = CompletedAccreditation
        fields = [
            "completed_result",
            "completed_year",
        ]

class MultiSelectUsersForm(forms.Form):
    Users = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=Select2MultipleWidget)

"""class StudentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput())
    house = forms.ModelChoiceField(queryset=House.objects.all(), initial=0)
 
    class Meta:
        model = Student
        fields = [
             “name”,”house”,
        ]"""
