from django.urls import path

from vuejs_django_course.calisthenics.api.views import exercise_create_api_view, exercise_list_api_view, \
    hit_create_api_view, hit_list_api_view

app_name = 'calisthenics'

urlpatterns = [
    path('exercises/create/', exercise_create_api_view, name='exercise-create'),
    path('exercises/', exercise_list_api_view, name='exercise-list'),
    path('hits/create/', hit_create_api_view, name='hit-create'),
    path('hits/', hit_list_api_view, name='hit-list'),
]
