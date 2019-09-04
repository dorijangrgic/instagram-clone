from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from users.models import CustomUser, Follow
from users.serializers import UserSerializer, UserRegistrationSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    http_method_names = ['get', 'patch', 'post', 'delete']

    @action(methods=['post'], detail=False, permission_classes=[AllowAny], url_path='registration')
    def user_registration(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.is_active = True
            user.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FollowView(APIView):

    def put(self, request, pk):
        user = request.user
        user_to_follow = CustomUser.objects.get(pk=pk)

        if user.id == user_to_follow.id:
            print("Cannot follow yourself!!!")
            return Response(status=status.HTTP_400_BAD_REQUEST)

        follows = Follow.objects.filter(who_id=user.id, whom_id=user_to_follow.id)

        if follows:
            # user vec follow-a drugog usera, napravi unfollow
            follows.delete()
            return Response()

        follow = Follow()
        follow.who = user
        follow.whom = user_to_follow
        follow.save()

        return Response()
