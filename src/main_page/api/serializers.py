from rest_framework import serializers
from main_page.models import FormQuestion, OurTeam, QuestionList


class FormQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormQuestion
        fields = ('id', 'question_text', 'contact',)


class OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeam
        fields = ('id', 'image', 'name', 'position', 'experience', 'quote', 'description')


class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionList
        fields = ('id', 'question', 'answer')
