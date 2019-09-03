from rest_framework import serializers
from users.models import CustomUser
from instagramcloneapp.models import Post
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    following = serializers.PrimaryKeyRelatedField(many=True, queryset=CustomUser.objects.all())

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'following', 'posts']


class UserRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    password = serializers.CharField(min_length=8)

    def validate(self, data):
        password = data.get('password')

        errors = dict()
        try:
            validate_password(password=password, user=CustomUser(**data))
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return super(UserRegistrationSerializer, self).validate(data)

    class Meta:
        model = CustomUser
        fields = ('username', 'password')

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
