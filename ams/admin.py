from django.contrib import admin
from .models import user, accrediting_body, files, degree_program, document_outline, document_outline_item, \
    completed_accreditation, prev_accreditation

admin.site.register(user)
admin.site.register(accrediting_body)
admin.site.register(files)
admin.site.register(degree_program)
admin.site.register(document_outline)
admin.site.register(document_outline_item)
admin.site.register(completed_accreditation)
admin.site.register(prev_accreditation)

# Register your models here.
