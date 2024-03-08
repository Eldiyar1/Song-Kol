from rest_framework import generics, permissions, status

from common.decorators import limit_rate
from main_page.models import FormQuestion, OurTeam, QuestionList
from main_page.api.serializers import FormQuestionSerializer, OurTeamSerializer, QuestionListSerializer

from main_page.services.questions import QuestionService


class FormQuestionCreateView(generics.CreateAPIView):
    queryset = FormQuestion.objects.all()
    serializer_class = FormQuestionSerializer
    permission_classes = [permissions.AllowAny]

    @limit_rate(num_requests=3, period=3600)
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return QuestionService.create_question(self, request)


class OurTeamListCreateView(generics.ListCreateAPIView):
    queryset = OurTeam.objects.all()
    serializer_class = OurTeamSerializer


class OurTeamRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OurTeam.objects.all()
    serializer_class = OurTeamSerializer


class QuestionListCreateView(generics.ListCreateAPIView):
    queryset = QuestionList.objects.all()
    serializer_class = QuestionListSerializer


class QuestionListRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestionList.objects.all()
    serializer_class = QuestionListSerializer
