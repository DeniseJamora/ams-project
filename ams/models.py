from django.db import models


class User(models.Model):
    user_email = models.EmailField()
    user_password = models.CharField(max_length=60)
    user_givenName = models.CharField(max_length=60)
    user_middleInitial = models.CharField(max_length=60)
    user_surname = models.CharField(max_length=60)
    user_type = models.CharField(max_length=60)


class AccreditingBody(models.Model):
    accrediting_body = models.CharField(max_length=60)


class Files(models.Model):
    file_name = models.CharField(max_length=60)
    file_type = models.CharField(max_length=30)
    file_document = models.FileField(max_length=250)


class Team(models.Model):
    team_name = models.CharField(max_length=60)


class DegreeProgram(models.Model):
    program_code = models.CharField(max_length=60)
    program_name = models.CharField(max_length=60)
    program_est = models.CharField(max_length=60)
    program_grads = models.CharField(max_length=60)


class DocumentOutline(models.Model):
    accrediting_body_id = models.ForeignKey(AccreditingBody, default='1', on_delete=models.CASCADE)
    document_name = models.CharField(max_length=120)


class DocumentOutlineItem(models.Model):
    document_outline_id = models.ForeignKey(DocumentOutline, default='1', on_delete=models.CASCADE)
    parent_document_outline_item_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    item_title = models.CharField(max_length=60)
    item_type = models.CharField(max_length=60)


class OngoingAccreditation(models.Model):
    accrediting_id = models.ForeignKey(AccreditingBody, default='1', on_delete=models.CASCADE)
    degree_program_id = models.ForeignKey(DegreeProgram, default='1', on_delete=models.CASCADE)
    teams_id = models.ForeignKey(Team, default='1', on_delete=models.CASCADE)
    document_id = models.ForeignKey(DocumentOutline, default='1', on_delete=models.CASCADE)


class CompletedAccreditation(models.Model):
    accrediting_id = models.ForeignKey(AccreditingBody, default='1', on_delete=models.CASCADE)
    degree_program_id = models.ForeignKey(DegreeProgram, default='1', on_delete=models.CASCADE)
    teams_id = models.ForeignKey(Team, default='1', on_delete=models.CASCADE)
    document_id = models.ForeignKey(DocumentOutline, default='1', on_delete=models.CASCADE)
    completed_result = models.CharField(max_length=60)
    completed_year = models.CharField(max_length=60)


class ChapterTeam(models.Model):
    accrediting_id = models.ForeignKey(AccreditingBody, default='1', on_delete=models.CASCADE)
    teams_id = models.ForeignKey(Team, default='1', on_delete=models.CASCADE)
    document_id = models.ForeignKey(DocumentOutline, default='1', on_delete=models.CASCADE)
    document_outline_item_id = models.ForeignKey(DocumentOutlineItem, default='1', on_delete=models.CASCADE)


class UserTeams(models.Model):
    accrediting_id = models.ForeignKey(AccreditingBody, default='1', on_delete=models.CASCADE)
    teams_id = models.ForeignKey(Team, default='1', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, default='1', on_delete=models.CASCADE)


class PrevAccreditation(models.Model):
    degree_program_id = models.ForeignKey(DegreeProgram, default='1', on_delete=models.CASCADE)
    accreditation_agency = models.CharField(max_length=60)
    accreditation_result = models.CharField(max_length=60)
    accreditation_year = models.CharField(max_length=60)

# Create your models here.
