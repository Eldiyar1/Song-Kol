from django.urls import path, include
from rest_framework import routers

from main_page.views import FormQuestionViewSet, OurTeamViewSet, QuestionListViewSet

router = routers.DefaultRouter()
router.register(r'questions', FormQuestionViewSet)
router.register(r'our_team', OurTeamViewSet)
router.register(r'question_list', QuestionListViewSet)

urlpatterns = [
    path('', include(router.urls)),
]