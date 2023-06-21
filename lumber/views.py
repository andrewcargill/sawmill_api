from rest_framework import generics
from .models import Test, Tree, Log, Plank, MoistureCheck
from .serializers import TestSerializer, TreeSerializer, LogSerializer, PlankSerializer, MoistureCheckSerializer

class TestList(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TreeList(generics.ListCreateAPIView):
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer

class LogList(generics.ListCreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

class PlankList(generics.ListCreateAPIView):
    queryset = Plank.objects.all()
    serializer_class = PlankSerializer

class MoistureCheckList(generics.ListCreateAPIView):
    queryset = MoistureCheck.objects.all()
    serializer_class = MoistureCheckSerializer



