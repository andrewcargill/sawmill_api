from rest_framework import generics, filters
from .models import Test, Tree, Log, Plank, MoistureCheck
from .serializers import TestSerializer, TreeSerializer, LogSerializer, PlankSerializer, MoistureCheckSerializer

class TestList(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['data1', 'data2','data3', 'id']

    def get_queryset(self):
        queryset = super().get_queryset()
        id_query = self.request.query_params.get('id')
        if id_query:
            queryset = queryset.filter(id=id_query)
        return queryset

class TestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TreeList(generics.ListCreateAPIView):
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['date', 'species','reason_for_felling', 'id']

    def get_queryset(self):
        queryset = super().get_queryset()
        id_query = self.request.query_params.get('id')
        if id_query:
            queryset = queryset.filter(id=id_query)
        return queryset

class TreeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer

class LogList(generics.ListCreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['date', 'length', 'id']

    def get_queryset(self):
        queryset = super().get_queryset()
        id_query = self.request.query_params.get('id')
        if id_query:
            queryset = queryset.filter(id=id_query)
        return queryset
    
class LogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

class PlankList(generics.ListCreateAPIView):
    queryset = Plank.objects.all()
    serializer_class = PlankSerializer

class MoistureCheckList(generics.ListCreateAPIView):
    queryset = MoistureCheck.objects.all()
    serializer_class = MoistureCheckSerializer



