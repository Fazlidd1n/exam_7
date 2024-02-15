from django.contrib import admin

from apps.models import Workers


@admin.register(Workers)
class WorkersListAdmin(admin.ModelAdmin):
    pass
