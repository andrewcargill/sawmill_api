from rest_framework import generics, filters
from .models import Test, DropboxTest, Tree, Log, Plank, MoistureCheck
from .serializers import TestSerializer, DropBoxFileSerializer, TreeSerializer, LogSerializer, PlankSerializer, MoistureCheckSerializer
from  rest_framework.views import APIView
from rest_framework import filters
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import FileUploadParser
from django.http import JsonResponse

"""Test"""


class HomeView(APIView):
   permission_classes = (IsAuthenticated, )

   def get(self, request):
        content = {'message': '(V2) Welcome to the JWT Authentication page using React Js and Django!'}
        return Response(content)
   
class LogoutView(APIView):
     permission_classes = (IsAuthenticated,)
     def post(self, request):
          
          try:
               refresh_token = request.data["refresh_token"]
               token = RefreshToken(refresh_token)
               token.blacklist()
               return Response(status=status.HTTP_205_RESET_CONTENT)
          except Exception as e:
               return Response(status=status.HTTP_400_BAD_REQUEST)


class TestList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
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
    permission_classes = (IsAuthenticated,)
    queryset = Test.objects.all()
    serializer_class = TestSerializer

"""Dropbox Test"""
class DropboxFileList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = DropboxTest.objects.all()
    serializer_class = DropBoxFileSerializer

class DropboxFileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = DropboxTest.objects.all()
    serializer_class = DropBoxFileSerializer

"""Dropbox Upload"""

class ImageUploadView(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = [FileUploadParser]

    def post(self, request, format=None):
        serializer = DropBoxFileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

"""Tree Views"""
class TreeList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['date', 'species', 'reason_for_felling', 'id']

    def get_queryset(self):
        queryset = super().get_queryset()
        id_query = self.request.query_params.get('id')
        if id_query:
            queryset = queryset.filter(id=id_query)
        return queryset

"""ID Validation"""
def validate_tree_id(request, tree_id):
    try:
        tree = Tree.objects.get(id=tree_id)
        return JsonResponse({'exists': True})
    except Tree.DoesNotExist:
        return JsonResponse({'exists': False})
    
def validate_log_id(request, log_id):
    try:
        log = Log.objects.get(id=log_id)
        return JsonResponse({'exists': True})
    except Log.DoesNotExist:
        return JsonResponse({'exists': False})
    
def validate_plank_id(request, plank_id):
    try:
        log = Plank.objects.get(id=plank_id)
        return JsonResponse({'exists': True})
    except Plank.DoesNotExist:
        return JsonResponse({'exists': False})
    
    

class TreeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer

"""Log Views"""
class LogList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
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
    permission_classes = (IsAuthenticated,)
    queryset = Log.objects.all()
    serializer_class = LogSerializer

"""Plank Views"""
class PlankList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
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
    permission_classes = (IsAuthenticated,)
    queryset = Plank.objects.all()
    serializer_class = PlankSerializer

"""Moisture Views"""
class MoistureCheckList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
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
    permission_classes = (IsAuthenticated,)
    queryset = MoistureCheck.objects.all()
    serializer_class = MoistureCheckSerializer

"""Additional Views"""
class LogsByTreeList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LogSerializer  # Replace with your Log serializer

    def get_queryset(self):
        tree_id = self.request.query_params.get('tree_id')
        queryset = Log.objects.filter(tree=tree_id)  # Replace 'tree' with the actual foreign key relation to the parent tree in your Log model
        return queryset

class PlanksByLogList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlankSerializer  

    def get_queryset(self):
        log_id = self.request.query_params.get('log_id')
        queryset = Plank.objects.filter(log=log_id) 
        return queryset
    
class MoistureChecksByPlankList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MoistureCheckSerializer  

    def get_queryset(self):
        plank_id = self.request.query_params.get('plank_id')
        queryset = MoistureCheck.objects.filter(plank=plank_id) 
        return queryset



