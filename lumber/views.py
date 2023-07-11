from rest_framework import generics, filters
from .models import Test, DropboxTest, Tree, Log, Plank, MoistureCheck, Post
from .serializers import TestSerializer, DropBoxFileSerializer, TreeSerializer, LogCreateSerializer, LogDetailSerializer, PlankCreateSerializer, PlankDetailSerializer, MoistureCheckSerializer, PostSerializer
from .pagination import CustomPagination
from  rest_framework.views import APIView
from rest_framework import filters
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import FileUploadParser
from django.http import JsonResponse
from cloudinary.uploader import upload
from django.http import JsonResponse
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from decimal import Decimal
from django.db.models import Q



"""Test"""


class HomeView(APIView):
   permission_classes = (IsAuthenticated, )

   def get(self, request):
        content = {'message': 'Welcome to Sawmill Go!(DV10) '}
        return Response(content)
   
class LogoutView(APIView):
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

"""Cloudinary"""
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        cloudinary_url = getattr(settings, 'CLOUDINARY_URL', ''),
    
        upload_result = upload(file, **cloudinary_url)
        # Process the upload result and save the necessary information in your database
        # Return a JSON response with the uploaded file details or a success message

        return JsonResponse({'upload_result': upload_result})
    
    return JsonResponse({'error': 'Invalid request'})

"""Cloudinary v3"""
class CloudPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

"""Cloudinary v2"""
@api_view(['POST'])
def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({'error': 'Post not found'}, status=404)

    serializer = PostSerializer(post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

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
class TreeListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class TreeList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = TreeListPagination

    search_fields = ['date', 'species', 'reason_for_felling', 'id', 'lumberjack', 'age']
    ordering_fields = ['date', 'species', 'age', 'id', 'lumberjack']

    def get_queryset(self):
        queryset = super().get_queryset()
        id_query = self.request.query_params.get('id')
        if id_query:
            queryset = queryset.filter(id=id_query)
        return queryset
    
class TreeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer

"""ID Validation"""
def validate_tree_id(request, tree_id):
    try:
        tree = Tree.objects.get(id=tree_id)
        return JsonResponse({'exists': True})
    except Tree.DoesNotExist:
        return JsonResponse({'exists': False})
    
validate_tree_id.permission_classes = [IsAuthenticated]
    
def validate_log_id(request, log_id):
    try:
        log = Log.objects.get(id=log_id)
        return JsonResponse({'exists': True})
    except Log.DoesNotExist:
        return JsonResponse({'exists': False})
    
validate_tree_id.permission_classes = [IsAuthenticated]
    
def validate_plank_id(request, plank_id):
    try:
        log = Plank.objects.get(id=plank_id)
        return JsonResponse({'exists': True})
    except Plank.DoesNotExist:
        return JsonResponse({'exists': False})
    
validate_tree_id.permission_classes = [IsAuthenticated]
    
    



"""Log Views"""
class LogListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class LogList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = LogListPagination
    search_fields = ['date', 'length', 'id', 'diameter', 'buck']
    ordering_fields = ['date', 'length', 'id', 'diameter', 'buck']
    pagination_class = LogListPagination

    def get_queryset(self):
        queryset = Log.objects.all()
        id_query = self.request.query_params.get('id')
        if id_query:
            queryset = queryset.filter(id=id_query)
        return queryset
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return LogDetailSerializer
        return LogCreateSerializer
    
class LogDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Log.objects.select_related('tree')
    serializer_class = LogDetailSerializer

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return LogCreateSerializer
        return self.serializer_class

"""Plank Views"""
class PlankListPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 200

class PlankList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['width', 'depth', 'wood_grade', 'id']
    ordering_fields = ['date', 'width', 'id', 'live_edge', 'depth']
    pagination_class = PlankListPagination

    def get_queryset(self):
        queryset = Plank.objects.all()
        id_query = self.request.query_params.get('id')
        if id_query:
            queryset = queryset.filter(id=id_query)

        width_min = self.request.query_params.get('width_min')
        width_max = self.request.query_params.get('width_max')
        if width_min and width_max:
            queryset = queryset.filter(width__gte=Decimal(width_min), width__lte=Decimal(width_max))
        elif width_min:
            queryset = queryset.filter(width__gte=Decimal(width_min))
        elif width_max:
            queryset = queryset.filter(width__lte=Decimal(width_max))

        depth_min = self.request.query_params.get('depth_min')
        depth_max = self.request.query_params.get('depth_max')
        if depth_min and depth_max:
            queryset = queryset.filter(depth__gte=Decimal(depth_min), depth__lte=Decimal(depth_max))
        elif depth_min:
            queryset = queryset.filter(depth__gte=Decimal(depth_min))
        elif depth_max:
            queryset = queryset.filter(depth__lte=Decimal(depth_max))

    
        grade_filter = self.request.query_params.get('wood_grade')  # Get the grade filter value
        if grade_filter:
            queryset = queryset.filter(wood_grade__icontains=grade_filter)
        
        general = self.request.query_params.get('general')
        if general == 'true':
            queryset = queryset.filter(general=True)
        elif general == 'false':
            queryset = queryset.filter(general=False)
        else:
            queryset = queryset.filter(Q(general=True) | Q(general=False))

        furniture = self.request.query_params.get('furniture')
        if furniture:
            queryset = queryset.filter(furniture=furniture)

        live_edge = self.request.query_params.get('live_edge')
        if live_edge:
            queryset = queryset.filter(live_edge=live_edge)

        structural = self.request.query_params.get('structural')
        if structural:
            queryset = queryset.filter(structural=structural)

        info_query = self.request.query_params.get('info')
        if info_query:
            queryset = queryset.filter(info__icontains=info_query)

        log_id = self.request.query_params.get('log_id')
        if log_id:
            queryset = queryset.filter(log__id=log_id)

        return queryset




    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PlankDetailSerializer
        return PlankCreateSerializer

class PlankDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Plank.objects.select_related('log__tree')
    serializer_class = PlankDetailSerializer

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return PlankCreateSerializer
        return self.serializer_class



"""Plank Report"""
class PlankReport(generics.RetrieveAPIView):
    queryset = Plank.objects.select_related('log__tree')
    serializer_class = PlankDetailSerializer
    permission_classes = [AllowAny]

    def get_allowed_methods(self):
        return ['GET']

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
    serializer_class = LogCreateSerializer  # Replace with your Log serializer

    def get_queryset(self):
        tree_id = self.request.query_params.get('tree_id')
        queryset = Log.objects.filter(tree=tree_id)  # Replace 'tree' with the actual foreign key relation to the parent tree in your Log model
        return queryset

class PlanksByLogList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlankCreateSerializer  

    def get_queryset(self):
        log_id = self.request.query_params.get('log_id')
        queryset = Plank.objects.filter(log=log_id) 
        return queryset
    
class MoistureChecksByPlankList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MoistureCheckSerializer  

    def get_queryset(self):
        plank_id = self.request.query_params.get('plank_id')
        queryset = MoistureCheck.objects.filter(plank=plank_id).order_by('-date')
        return queryset
    




