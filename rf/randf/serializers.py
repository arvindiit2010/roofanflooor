from rest_framework import serializers
from randf.models import MovieRating, CustomUser


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieRating
        fields = ('name', 'rating', 'comment')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'contact',)


