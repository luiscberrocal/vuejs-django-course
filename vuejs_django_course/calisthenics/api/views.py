from rest_framework.generics import CreateAPIView, ListAPIView

from vuejs_django_course.calisthenics.api.serializers import ExerciseSerializer, HitSerializer
from vuejs_django_course.calisthenics.models import Exercise, Hit


class ExerciseCreateAPIView(CreateAPIView):
    # queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


exercise_create_api_view = ExerciseCreateAPIView.as_view()


class ExerciseListAPIView(ListAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


exercise_list_api_view = ExerciseListAPIView.as_view()


class HitCreateAPIView(CreateAPIView):
    # queryset = Hit.objects.all()
    serializer_class = HitSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


hit_create_api_view = HitCreateAPIView.as_view()


class HitListAPIView(ListAPIView):
    queryset = Hit.objects.all()
    serializer_class = HitSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = HitFilter


hit_list_api_view = HitListAPIView.as_view()
