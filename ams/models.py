from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class User_Manager(BaseUserManager):
    def create_user(self, email, username, type, given_name, middle_initial, surname, password=None):
        if not email:
            raise ValueError("Please input email address")
        if not username:
            raise ValueError("Please input username")
        if not type:
            raise ValueError("Please select user type")
        if not given_name:
            raise ValueError("Please input name")
        if not middle_initial:
            raise ValueError("Please input middle initial")
        if not surname:
            raise ValueError("Please input surname")

        u = self.model(
            email=self.normalize_email(email),
            username=username,
            type=type,
            given_name=given_name,
            middle_initial=middle_initial,
            surname=surname,
        )

        u.set_password(password)
        u.save(using=self._db)
        return u

    def create_superuser(self, email, username, type, given_name, middle_initial, surname, password=None):
        u = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            type=type,
            given_name=given_name,
            middle_initial=middle_initial,
            surname=surname,
        )
        u.is_admin = True
        u.is_staff = True
        u.is_superuser = True
        u.save(using=self._db)
        return u


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', unique=True)
    username = models.CharField(max_length=60, unique=True)
    given_name = models.CharField(max_length=60)
    middle_initial = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    type = models.CharField(max_length=60)
    date_joined = models.DateTimeField(verbose_name='date_joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last_login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'given_name', 'middle_initial', 'surname', 'type']

    def __str__(self):
        return self.surname + ", " + self.given_name + " " + self.middle_initial + "."

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    objects = User_Manager()


class AccreditingBody(models.Model):
    accrediting_body = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = "accrediting_Bodies"

    def __str__(self):
        return self.accrediting_body


class DegreeProgram(models.Model):
    program_code = models.CharField(max_length=60)
    program_name = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = "degree_Programs"

    def __str__(self):
        return self.program_name


class PrevAccreditation(models.Model):
    degree_program_id = models.ForeignKey(DegreeProgram, default='1', on_delete=models.CASCADE)
    accreditation_agency = models.CharField(max_length=60)
    accreditation_result = models.CharField(max_length=60)
    accreditation_year = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = "previous_Program_Accreditations"

    def __str__(self):
        return self.degree_program_id.program_code + " " + self.accreditation_agency + " " + self.accreditation_year


class File(models.Model):
    file_name = models.CharField(max_length=60)
    file_type = models.CharField(max_length=30)
    file_document = models.FileField(max_length=250)

    def __str__(self):
        return self.file_name


class Team(models.Model):
    team_name = models.CharField(max_length=60)


class DocumentOutline(models.Model):
    accrediting_body_id = models.ForeignKey(AccreditingBody, default='1', on_delete=models.CASCADE)
    document_name = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = "document_Outlines"

    def __str__(self):
        return self.document_name


class DocumentOutlineItem(models.Model):
    document_outline_id = models.ForeignKey(DocumentOutline, default='1', on_delete=models.CASCADE)
    parent_document_outline_item_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    criteria_description = models.CharField(max_length=512)
    criteria_evidences = models.CharField(max_length=256)
    criteria_minimum = models.CharField(max_length=60)
    criteria_maximum = models.CharField(max_length=60)
    item_title = models.CharField(max_length=60)
    item_type = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = "document_Outline_Items"

    def __str__(self):
        return self.document_outline_id.document_name


class OngoingAccreditation(models.Model):
    accrediting_id = models.ForeignKey(AccreditingBody, default='1', on_delete=models.CASCADE)
    degree_program_id = models.ForeignKey(DegreeProgram, default='1', on_delete=models.CASCADE)
    team_id = models.ForeignKey(Team, default='1', on_delete=models.CASCADE)
    document_id = models.ForeignKey(DocumentOutline, default='1', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "ongoing_Accreditations"

    def __str__(self):
        return self.degree_program_id.program_name + " " + self.accrediting_id.accrediting_body


class CompletedAccreditation(models.Model):
    accrediting_id = models.ForeignKey(AccreditingBody, default='1', on_delete=models.CASCADE)
    degree_program_id = models.ForeignKey(DegreeProgram, default='1', on_delete=models.CASCADE)
    team_id = models.ForeignKey(Team, default='1', on_delete=models.CASCADE)
    document_id = models.ForeignKey(DocumentOutline, default='1', on_delete=models.CASCADE)
    completed_result = models.CharField(max_length=60)
    completed_year = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = "completed_Accreditations"

    def __str__(self):
        return self.degree_program_id.program_name + " " + self.accrediting_id.accrediting_body


class ChapterTeam(models.Model):
    accrediting_id = models.ForeignKey(AccreditingBody, default='1', on_delete=models.CASCADE)
    team_id = models.ForeignKey(Team, default='1', on_delete=models.CASCADE)
    document_id = models.ForeignKey(DocumentOutline, default='1', on_delete=models.CASCADE)
    document_outline_item_id = models.ForeignKey(DocumentOutlineItem, default='1', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "team_Chapters"

    def __str__(self):
        return self.team_id.team_name + " " + self.document_id.document_name + " " + self.document_outline_item_id.item_title


class UserTeam(models.Model):
    accrediting_id = models.ForeignKey(AccreditingBody, default='1', on_delete=models.CASCADE)
    team_id = models.ForeignKey(Team, default='1', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, default='1', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "team_Members"

    def __str__(self):
        return self.team_id.team_name + " " + self.user_id.given_name + " " + self.user_id.surname

class Evidences(models.Model):
    evidences_text = models.CharField(max_length=512)
    document_outline_item = models.ForeignKey(DocumentOutlineItem, default='1', on_delete=models.CASCADE)

class OutlineCriteria(models.Model):
    outline_criteria_text = models.CharField(max_length=512)
    document_outline = models.ForeignKey(DocumentOutline, default='1', on_delete=models.CASCADE)
    document_outline_item = models.ForeignKey(DocumentOutlineItem, default='1', on_delete=models.CASCADE)

class AccreditationPeriod(models.Model):
    agency_id = models.IntegerField()
    type = models.CharField(max_length=128)
    document_id = models.IntegerField()
    degree_program_id = models.IntegerField()
    end_date = models.DateField(blank=True)
# Create your models here.
