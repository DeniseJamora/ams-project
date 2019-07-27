from django.contrib import admin
from .models import User, AccreditingBody, File, DegreeProgram, DocumentOutline, DocumentOutlineItem, \
    CompletedAccreditation, PrevAccreditation, Team, UserTeam

admin.site.register(User)
admin.site.register(AccreditingBody)
admin.site.register(File)
admin.site.register(DegreeProgram)
admin.site.register(DocumentOutline)
admin.site.register(DocumentOutlineItem)
admin.site.register(CompletedAccreditation)
admin.site.register(PrevAccreditation)
admin.site.register(Team)
admin.site.register(UserTeam)

# Register your models here.
