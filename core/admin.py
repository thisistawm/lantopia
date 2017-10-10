from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import User

from core.models import Profile, Todo



class ProfileInline(admin.StackedInline):
    model = Profile

class TodoInline(admin.StackedInline):
    model = Todo

class UserAdmin(DjangoUserAdmin):
    inlines = (ProfileInline, TodoInline)



admin.site.unregister(User)
admin.site.register(User, UserAdmin)