from django.forms import model_to_dict
from django.template.context_processors import request
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Games
from django.shortcuts import render
from .serializers import GamesSerializer


# Create your views here.
#class GamesAPIView(generics.ListAPIView):
    #если у Games одчёркнут objects - это потому, что у меня халявная версия pycharm
#   queryset = Games.objects.all()
#   serializer_class = GamesSerializer

class GamesAPIView(APIView):
    def get(self, request):
        lst = Games.objects.all().values()
        return Response({'games' : list(lst)})

    def post(self, request):
        post_new = Games.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            category_id=request.data['category_id']
        )

        return Response({'post' :  model_to_dict(post_new)})