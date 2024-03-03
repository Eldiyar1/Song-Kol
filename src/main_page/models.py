from django.db import models


class FormQuestion(models.Model):
    question_text = models.TextField(verbose_name="Write your question")
    contact = models.CharField(verbose_name="Leave your E-mail or WhatsApp", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class OurTeam(models.Model):
    image = models.ImageField(upload_to='our_team', verbose_name="Фото сотрудника")
    name = models.CharField(verbose_name="Имя", max_length=100)
    position = models.CharField(verbose_name="Должность", max_length=200)
    experience = models.CharField(verbose_name="Опыт", max_length=200, blank=True, null=True)
    quote = models.TextField(verbose_name="Цитата", blank=True, null=True)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    def __str__(self):
        return self.name, " ", self.position

    class Meta:
        verbose_name = "Наша команда"
        verbose_name_plural = "Наша команда"
        db_table = 'our_team'


class QuestionList(models.Model):
    question = models.CharField(verbose_name="Вопрос", max_length=250)
    answer = models.CharField(verbose_name="Ответ", max_length=250)

    def __str__(self):
        return self.question, " ", self.answer

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
        db_table = 'question_list'
