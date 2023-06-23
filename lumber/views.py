from rest_framework import generics, filters
from .models import Test, DropboxTest, Tree, Log, Plank, MoistureCheck
from .serializers import TestSerializer, DropBoxFileSerializer, TreeSerializer, LogSerializer, PlankSerializer, MoistureCheckSerializer
from  rest_framework.views import APIView
from rest_framework import filters
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response

"""Test"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters

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

"""Dropbox Test"""
class DropboxFileList(generics.ListCreateAPIView):
    queryset = DropboxTest.objects.all()
    serializer_class = DropBoxFileSerializer

class DropboxFileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DropboxTest.objects.all()
    serializer_class = DropBoxFileSerializer


"""Tree Views"""
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

"""Log Views"""
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

"""Plank Views"""
class PlankList(generics.ListCreateAPIView):
    queryset = Plank.objects.all()
    serializer_class = PlankSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['width', 'depth', 'wood_grade', 'id']

    def get_queryset(self):
        queryset = super().get_queryset()
        id_query = self.request.query_params.get('id')
        if id_query:
            queryset = queryset.filter(id=id_query)
        return queryset

class PlankDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plank.objects.all()
    serializer_class = PlankSerializer

"""Moisture Views"""
class MoistureCheckList(generics.ListCreateAPIView):
    queryset = MoistureCheck.objects.all()
    serializer_class = MoistureCheckSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['date', 'water_percentage', 'id']

    def get_queryset(self):
        queryset = super().get_queryset()
        id_query = self.request.query_params.get('id')
        if id_query:
            queryset = queryset.filter(id=id_query)
        return queryset

class MoistureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MoistureCheck.objects.all()
    serializer_class = MoistureCheckSerializer

"""Additional Views"""
class LogsByTreeList(generics.ListAPIView):
    serializer_class = LogSerializer  # Replace with your Log serializer

    def get_queryset(self):
        tree_id = self.request.query_params.get('tree_id')
        queryset = Log.objects.filter(tree=tree_id)  # Replace 'tree' with the actual foreign key relation to the parent tree in your Log model
        return queryset

class PlanksByLogList(generics.ListAPIView):
    serializer_class = PlankSerializer  

    def get_queryset(self):
        log_id = self.request.query_params.get('log_id')
        queryset = Plank.objects.filter(log=log_id) 
        return queryset
    
class MoistureChecksByPlankList(generics.ListAPIView):
    serializer_class = MoistureCheckSerializer  

    def get_queryset(self):
        plank_id = self.request.query_params.get('plank_id')
        queryset = MoistureCheck.objects.filter(plank=plank_id) 
        return queryset



