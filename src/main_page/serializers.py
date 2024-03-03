from rest_framework import serializers
from .models import FormQuestion, OurTeam, QuestionList


class FormQuestionSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True, format='%d-%m-%Y')

    class Meta:
        model = FormQuestion
        fields = ('id', 'question_text', 'contact', 'created_at')


class OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeam
        fields = ('id', 'image', 'name', 'position', 'experience', 'quote', 'description')


class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionList
        fields = ('id', 'question', 'answer')
