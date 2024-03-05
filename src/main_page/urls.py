from django.urls import path

from main_page.views import (
    FormQuestionCreateView, OurTeamListCreateView, OurTeamRetrieveUpdateDestroyView,
    QuestionListCreateView, QuestionListRetrieveUpdateDestroyView
)

urlpatterns = [
    path('questions/', FormQuestionCreateView.as_view(), name='formquestion-create'),
    path('our_team/', OurTeamListCreateView.as_view(), name='ourteam-create'),
    path('our_team/<int:pk>/', OurTeamRetrieveUpdateDestroyView.as_view(), name='ourteam-detail'),
    path('question_list/', QuestionListCreateView.as_view(), name='questionlist-create'),
    path('question_list/<int:pk>/', QuestionListRetrieveUpdateDestroyView.as_view(), name='questionlist-detail'),
]
