from rest_framework import serializers

from vuejs_django_course.calisthenics.models import Exercise, Hit


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'name', 'description', 'active')


class HitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hit
        fields = ('id', 'exercise', 'date', 'reps', 'weight', 'user')
