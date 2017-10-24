from django.contrib import admin
from .models import Team, TeamMember


class TeamMemberInline(admin.StackedInline):
    model = TeamMember
    extra = 2

class TeamAdmin(admin.ModelAdmin):
    inlines = (TeamMemberInline,)

admin.site.register(Team, TeamAdmin)
