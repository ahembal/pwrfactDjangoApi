from django.shortcuts import render
from rest_framework import generics, permissions, authentication
from .models import Experiment, Record
from .serializer import ExperimentSerializer, RecordSerializer

# Create your views here.
class ExperimentListCreateAPIView(# UserQuerySetMixin,
    # StaffEditorPermissionMixin,
    generics.ListCreateAPIView):

    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    authentication_classes = [
        authentication.TokenAuthentication,
        authentication.SessionAuthentication
    ]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

experiment_list_create_view = ExperimentListCreateAPIView.as_view()


class RecordListCreateAPIView(
    generics.ListCreateAPIView
):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

record_list_create_view = RecordListCreateAPIView.as_view()