from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import FormQuestion, OurTeam, QuestionList


def truncated_text(obj, text_field):
    if len(getattr(obj, text_field)) > 75:
        return getattr(obj, text_field)[:75] + '...'
    else:
        return getattr(obj, text_field)


@admin.register(FormQuestion)
class FormQuestionAdmin(admin.ModelAdmin):
    list_display = ('truncated_question_text', 'contact', 'created_at')
    ordering = ('-created_at',)

    def truncated_question_text(self, obj):
        return truncated_text(obj, 'question_text')

    truncated_question_text.short_description = _('Вопрос')


@admin.register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'truncated_experience')
    ordering = ('-created_at',)

    def truncated_experience(self, obj):
        return truncated_text(obj, 'experience')

    truncated_experience.short_description = _('Опыт')


@admin.register(QuestionList)
class QuestionListAdmin(admin.ModelAdmin):
    list_display = ('truncated_question', 'truncated_answer')
    ordering = ('-created_at',)

    def truncated_question(self, obj):
        return truncated_text(obj, 'question')

    def truncated_answer(self, obj):
        return truncated_text(obj, 'answer')

    truncated_question.short_description = _('Вопрос')
    truncated_answer.short_description = _('Ответ')
