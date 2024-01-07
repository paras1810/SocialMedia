from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator

from . serializers import UserSerializer


class UserViewSet(viewsets.ViewSet):
    #pagination.PageNumberPagination.max_page_size = 2
    def list(self, request):
        queryset = User.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 2
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = UserSerializer(result_page, many=True)
        return Response(serializer.data)
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self, request, pk):
        queryset = User.objects.all()
        user = get_object_or_404(queryset,pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


#{"username":"paras","email":"paras@gmail.com","password":"paras123"}
#{"username":"rishabh","email":"rishabh@gmail.com","password":"rishabh123"}

