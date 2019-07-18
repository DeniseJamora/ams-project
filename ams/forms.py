from django import forms
from django.db import transaction
from django.forms import modelformset_factory
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import IncidentReport, Project, ProjectExpense, Milestone, Budget, BudgetExtension


class MilestoneForm(forms.ModelForm):
    milestoneName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    assignedTo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    milestoneDate = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': 'form-control col-md-7 col-xs-12'}))

    class Meta:
        model = Milestone
        fields = ('milestoneName', 'assignedTo', 'milestoneDate',)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, label='First Name',
                                 widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    last_name = forms.CharField(max_length=50, label='Last Name',
                                widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    email = forms.EmailField(max_length=254, label='Email Address',
                             widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control col-md-7 col-xs-12'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control col-md-7 col-xs-12'})


class ProjectForm(forms.ModelForm):
    projectTitle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    fundingAgency = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    projectDate = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': 'form-control col-md-7 col-xs-12'}))

    class Meta:
        model = Project
        fields = [
            'projectTitle',
            'fundingAgency',
            'projectDate',
        ]


class ProjectAccountForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "accountNumber",
            "projectTitle",
            "principalInvestigator",
            "projectMember",
            "fundingAgency",
            "startDate",
            "endDate",
            "projectCost",
            "projectOverview",
            "files",
            "contractFile",
        ]

        widgets = {'accountNumber': forms.TextInput(attrs={
            'class': 'form-control',

        }), 'projectTitle': forms.TextInput(attrs={
            'class': 'form-control',

        }), 'principalInvestigator': forms.TextInput(attrs={
            'class': 'form-control',

        }), 'projectMember': forms.TextInput(attrs={
            'class': 'tags form-control',
            'id': 'tags_1',

        }), 'fundingAgency': forms.TextInput(attrs={
            'class': 'form-control',
        }), 'startDate': forms.TextInput(attrs={
            'class': 'form-control has-feedback-left',
            'type': 'date'
        }), 'endDate': forms.TextInput(attrs={
            'class': 'form-control has-feedback-left',
            'type': 'date'
        }), 'projectCost': forms.TextInput(attrs={
            'class': 'form-control',
        }), 'projectOverview': forms.Textarea(attrs={
            'class': 'form-control',

        }), 'contractFile': forms.FileInput(attrs={
            'data-role': "magic-overlay",
            'data-target': "#pictureBtn",
            'data-edit': "insertImage",
        })
        }


class ExpenseParticularForm(forms.ModelForm):
    class Meta:
        model = ProjectExpense
        fields = [
            "expenseType",
            "expenseName",
            "expenseQuantity",
            "expenseAmount",

        ]


ExpenseParticularFormset = modelformset_factory(
    ProjectExpense,
    fields=('expenseName', 'expenseQuantity', 'expenseAmount', 'expenseTotal'),
    extra=1,
    widgets={'expenseName': forms.TextInput(attrs={
        'class': ' form-control name',

        'required': 'required',
    }),
        'expenseQuantity': forms.TextInput(attrs={
            'class': ' form-control quantity',
            'required': 'required',
            'type': 'number',
            'placeholder': '0',
        }),
        'expenseAmount': forms.TextInput(attrs={
            'class': ' form-control amount',
            'required': 'required',
            'type': 'number',
            'placeholder': '0.0',
        }),

        'expenseTotal': forms.TextInput(attrs={
            'class': 'form-control total',
            'required': 'required',
            'placeholder': '0',
            'readonly': 'readonly',
        })}
)


class BudgetForm(forms.ModelForm):
    approvedAmount = forms.CharField(max_length=20,
                                     widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    dateReceived = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': 'form-control col-md-7 col-xs-12'}))

    class Meta:
        model = Budget
        fields = ['approvedAmount', 'dateReceived']


class IncidentForm(forms.ModelForm):
    issueEncountered = forms.CharField(label='Issue encountered', max_length=1000)
    issueDescription = forms.CharField(label='Description of the issue', max_length=5000)
    dateEncountered = forms.DateField()

    class Meta:
        model = IncidentReport
        fields = ['issueEncountered', 'issueDescription', 'dateEncountered']


EXPENSE_TYPE_CHOICES = (
    ('Personnel'),
    ('Fieldwork Expenses'),
    ('Office Equipment'),
    ('Others')
)


class ExpenseForm(forms.ModelForm):
    expenseName = forms.CharField(max_length=1000, label='Expense Name',
                                  widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    expenseQuantity = forms.CharField(max_length=10, label='Quantity',
                                      widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    expenseAmount = forms.CharField(max_length=20, label='Total Amount',
                                    widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    expenseDescription = forms.CharField(max_length=1000, label='Description',
                                         widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    expensePurpose = forms.CharField(max_length=1000, label='Purpose',
                                     widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    expenseDate = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': 'form-control col-md-7 col-xs-12'}))

    class Meta:
        model = ProjectExpense
        fields = ['expenseName', 'expenseQuantity', 'expenseAmount', 'expenseDescription', 'expensePurpose',
                  'expenseDate']


class BudgetExtensionForm(forms.ModelForm):
    amountRequested = forms.CharField(max_length=20,
                                      widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    reason = forms.CharField(max_length=1000,
                             widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))

    class Meta:
        model = BudgetExtension
        fields = ['amountRequested', 'reason']
