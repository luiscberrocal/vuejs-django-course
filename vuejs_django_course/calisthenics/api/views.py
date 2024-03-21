from rest_framework.generics import CreateAPIView, ListAPIView

from vuejs_django_course.calisthenics.api.serializers import ExerciseSerializer, HitSerializer
from vuejs_django_course.calisthenics.models import Exercise


class ExerciseCreateAPIView(CreateAPIView):
    # queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class ExerciseListAPIView(ListAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class HitCreateAPIView(CreateAPIView):
    # queryset = Hit.objects.all()
    serializer_class = HitSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
