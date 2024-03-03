from django.contrib import admin

from .models import FormQuestion, OurTeam, QuestionList

admin.site.register(FormQuestion)
admin.site.register(OurTeam)

"""Раскоментить после доплаты правок"""
# admin.site.register(QuestionList)


