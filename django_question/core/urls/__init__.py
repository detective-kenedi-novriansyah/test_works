from django.urls import path, include

urlpatterns = [
    path('question/', include('question.urls.question')),
    path('user/', include('question.urls.user'))
]