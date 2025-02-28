from rest_framework import generics, permissions
from user.models import User
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from ..serializers import CreateUserSerializer


class UserRegistrationViews(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        return Response(
                {
                    "status": HTTP_201_CREATED,
                    "success": True,
                    "message": "Provided API endpoint doesnot exist!",
                    "data ": user
                },
                status=HTTP_201_CREATED
            )
