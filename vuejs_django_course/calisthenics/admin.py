from django.contrib import admin

from vuejs_django_course.calisthenics.models import Exercise, Hit
from vuejs_django_course.core.admin import AuditableAdminMixin


# Register your models here.
@admin.register(Exercise)
class ExerciseAdmin(AuditableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'description', 'active')
    search_fields = ('name', 'description')
    list_filter = ('active',)


@admin.register(Hit)
class HitAdmin(AuditableAdminMixin, admin.ModelAdmin):
    list_display = ('exercise', 'date', 'reps', 'weight', 'user')
    search_fields = ('exercise__name', 'exercise__description')
    list_filter = ('date', 'user')
