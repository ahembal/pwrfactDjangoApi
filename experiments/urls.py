from django.urls import path

from . import views


urlpatterns = [
    path('', views.experiment_list_create_view),
    path('records/', views.record_list_create_view),

]