from django.contrib import admin
from .models import Project, IncidentReport, Milestone, Budget, ProjectExpense, BudgetExtension, ProjectContract


admin.site.register(Project)
admin.site.register(IncidentReport)
admin.site.register(Milestone)
admin.site.register(Budget)
admin.site.register(ProjectExpense)
admin.site.register(BudgetExtension)
admin.site.register(ProjectContract)