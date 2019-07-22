from django.contrib import admin
from .models import User, AccreditingBody, Files, DegreeProgram, DocumentOutline, DocumentOutlineItem, \
    CompletedAccreditation, PrevAccreditation

admin.site.register(User)
admin.site.register(AccreditingBody)
admin.site.register(Files)
admin.site.register(DegreeProgram)
admin.site.register(DocumentOutline)
admin.site.register(DocumentOutlineItem)
admin.site.register(CompletedAccreditation)
admin.site.register(PrevAccreditation)

# Register your models here.
