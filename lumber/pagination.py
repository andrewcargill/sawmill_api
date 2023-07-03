from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 2  # Number of items per page
    page_size_query_param = 'page_size'  # URL query parameter for page size
    max_page_size = 100  # Maximum page size allowed
