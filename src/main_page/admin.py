from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import FormQuestion, OurTeam, QuestionList


@admin.register(FormQuestion)
class FormQuestionAdmin(admin.ModelAdmin):
    list_display = ('truncated_question_text', 'contact', 'created_at')
    ordering = ('-created_at',)

    def truncated_question_text(self, obj):
        if len(obj.question_text) > 75:
            return obj.question_text[:75] + '...'
        else:
            return obj.question_text

    truncated_question_text.short_description = _('Question Text')


@admin.register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'experience')
    ordering = ('-created_at',)


@admin.register(QuestionList)
class QuestionListAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    ordering = ('-created_at',)
