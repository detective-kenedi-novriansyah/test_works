from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from django.contrib.auth.models import User
from question.serializer.user import UserSerializer, BaseUserSerializer
from rest_framework import permissions

from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class UserModelViewSets(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    serializer = BaseUserSerializer

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [permissions.AllowAny,]
        else:
            permission_classes = [permissions.IsAuthenticated,]
        return [permission() for permission in permission_classes]

    def create(self, request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.filter(first_name=serializer.validated_data.get('first_name')).first()
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            return Response({'message': token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
