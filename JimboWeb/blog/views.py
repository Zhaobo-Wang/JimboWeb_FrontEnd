from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import BlogSerializer
from .models import BlogModel
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
# Create your views here.


class ApiBlogListView(ListAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'articles', 'tags')

    @api_view(['GET'])
    def blogs(request):
        blogs = BlogModel.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def blog_detail(request, id):
    try:
        blog = BlogModel.objects.get(pk=id)
    except BlogModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = BlogSerializer(blog)
    return Response(serializer.data)
