from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from question.serializer.question import QuestionSerializer, AnswerSerializer, BaseAnswerSerializer, BaseQuestionSerializer, BaseAnswerTextSerializer, AnswerTextSerializer
from database.models.question import Question, Answer, AnswerText
from django.utils.translation import gettext as _
from database.models.question import Point

class QuestionModelViewSets(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    serializer = BaseQuestionSerializer

    permission_classes = [permissions.AllowAny,]

    def create(self, request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": _("Question has been created")}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        serializer = self.serializer(question,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": _("Question has been update")}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class AnswerModeViewSets(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    serializer = BaseAnswerSerializer

    def get_permissions(self):
        if self.action == "update":
            permission_classes = [permissions.IsAuthenticated,]
        else:
            permission_classes = [permissions.AllowAny,]
        return [permission() for permission in permission_classes]


    def create(self, request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": _("Answer has been created")}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        answers = Answer.objects.filter(name=request.data.get('answers'),id=pk,right=True).first()
        point = Point.objects.filter(candidate=request.user).first()
        print(point)
        if not point:
            point = Point(candidate=request.user)
            point.save()
        if not answers:
            answers = get_object_or_404(Answer, pk=pk)
            answers.right = False
            point.point -= 10
            point.answer.add(answers)
            point.save()
            return Response({'message': 'Maaf anda salah silahkan coba besok', 'point': point.point}, status=status.HTTP_400_BAD_REQUEST)
        point.point += 10
        point.answer.add(answers)
        point.save()
        return Response({'message': 'Selamat anda menang mendapatkan hadiah mobil biaya pembelian ditanggung pemenang','point': point.point}, status=status.HTTP_200_OK)



class AnswerTextModeViewSets(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerTextSerializer
    serializer = BaseAnswerTextSerializer

    permission_classes = [permissions.AllowAny,]


    def create(self, request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": _("Answer has been created")}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PointAPIView(APIView):

    def get(self, request):
        point = Point.objects.filter(candidate=request.user).first()
        if not point:
            return Response(0, status=status.HTTP_200_OK)
        return Response(point.point, status=status.HTTP_200_OK)