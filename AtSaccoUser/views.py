from rest_framework import generics, exceptions
from rest_framework.response import Response
from .models import UserMember
from .serializers import UserMemberCreateSerializer, UserMemberDisplaySerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.exceptions import APIException, MethodNotAllowed

class CustomResponse(Response):
    def __init__(self, success=True, download_url=None,  data=None, message=None, status=None, headers=None, exception=False, content_type=None):
        response_data = {
            'success': success,
            'data': data,
            'message': message,
            'download_url': download_url,
        }

        super().__init__(data=response_data, status=status, headers=headers, exception=exception, content_type=content_type)


class UserMemberListCreateView(generics.ListCreateAPIView):
    queryset = UserMember.objects.all()
    authentication_classes = []  # Disable authentication
    permission_classes = [AllowAny]  # Allow any user

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserMemberCreateSerializer
        return UserMemberDisplaySerializer

    def list(self, request, *args, **kwargs):
        UserMemberList = UserMember.objects.all()
        serializer = self.get_serializer(UserMemberList, many=True)
        return CustomResponse(success=True, data=serializer.data, message="Successfully fetched commits")

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return CustomResponse(success=True, data=serializer.data, message="Successfully created a member")

        except exceptions.ValidationError as e:
            return CustomResponse(success=False, message=str(e))

        except APIException as e:
            return CustomResponse(success=False, message=str(e))

class UserMemberDetailView(generics.RetrieveUpdateAPIView):
    queryset = UserMember.objects.all()
    serializer_class = UserMemberDisplaySerializer
    authentication_classes = []  # Disable authentication
    permission_classes = [AllowAny]  # Allow any user

    def list(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UserMemberCreateSerializer(instance, data=request.data, partial=True)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return CustomResponse(success=True, data=serializer.data, message="Successfully updated the member information")
        except APIException as e:
            return CustomResponse(success=False, message=str(e))

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        deleted_by = request.user

        instance.deleted_by = deleted_by
        instance.save()

        instance.delete()
        return CustomResponse(success=True, message="Member has been deleted")

