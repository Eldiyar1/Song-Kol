from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import format_lazy

from common.models import BaseModel


class FormQuestion(BaseModel):
    question_text = models.TextField(verbose_name=_("Введите ваш вопрос"))
    contact = models.CharField(max_length=100, verbose_name=_("Оставьте ваш E-mail или WhatsApp"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))

    def __str__(self):
        return str(format_lazy(_("Вопрос: {question} - Контакт: {contact}"), question=self.question_text,
                               contact=self.contact))

    class Meta:
        verbose_name = _("Вопрос в форме")
        verbose_name_plural = _("Вопросы в форме")
        db_table = 'form_question'


class OurTeam(BaseModel):
    image = models.ImageField(upload_to='our_team', verbose_name=_("Фото сотрудника"))
    name = models.CharField(max_length=100, verbose_name=_("Имя"))
    position = models.CharField(max_length=200, verbose_name=_("Должность"))
    experience = models.CharField(max_length=200, blank=True, null=True, verbose_name=_("Опыт"))
    quote = models.TextField(blank=True, null=True, verbose_name=_("Цитата"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Описание"))

    def __str__(self):
        return str(format_lazy(_("Сотрудник: {name} ({position})"), name=self.name, position=self.position))

    class Meta:
        verbose_name = _("Наша команда")
        verbose_name_plural = _("Наши команды")
        db_table = 'our_team'


class QuestionList(BaseModel):
    question = models.CharField(max_length=250, verbose_name=_("Вопрос"))
    answer = models.CharField(max_length=250, verbose_name=_("Ответ"))

    def __str__(self):
        return str(format_lazy(_("Вопрос: {question} - Ответ: {answer}"), question=self.question, answer=self.answer))

    class Meta:
        verbose_name = _("Вопрос")
        verbose_name_plural = _("Вопросы")
        db_table = 'question_list'
