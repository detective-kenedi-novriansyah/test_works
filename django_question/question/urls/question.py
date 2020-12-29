from django.urls import path, include
from rest_framework import routers
from question.views.question import QuestionModelViewSets, AnswerModeViewSets, AnswerTextModeViewSets,PointAPIView

router = routers.DefaultRouter()
router.register('', QuestionModelViewSets, basename='question')
router.register('question/answer', AnswerModeViewSets, basename='answer')
router.register('question/answer/text/add', AnswerTextModeViewSets, basename="answer-text")

urlpatterns = [
    path('', include((router.urls, 'api'))),
    path("question/question/question/point/", PointAPIView.as_view(), name="point")
]