from django.core.serializers import serialize
from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Games
from .serializers import GamesSerializer
from rest_framework import generics

# Create your views here.
#class GamesAPIView(generics.ListAPIView):
    #если у Games подчёркнут objects - это потому, что у меня халявная версия pycharm
#   queryset = Games.objects.all()
#   serializer_class = GamesSerializer

class GamesApiList(generics.ListCreateAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer

class GamesApiDelete(generics.DestroyAPIView):
    queryset = Games.objects.all()  # Указываем queryset
    serializer_class = GamesSerializer


#ниже вариант как всё раписать вручную
# class GamesAPIView(APIView):
#     def get(self, request):
#         g = Games.objects.all()
#         return Response({'games' : GamesSerializer(g, many=True).data})
#
#     def post(self, request):
#         #Валидируем данные перед дальнейшими действиями
#         serializer = GamesSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'games' :  serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         #pk - идентификатор записи
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error", "Method PUT not allowed"})
#
#         try:
#             instance = Games.objects.get(pk=pk)
#         except:
#             return Response({"error", "Method PUT not allowed"})
#
#         serializer = GamesSerializer(data=request.data, instance=instance) #так как тут у
#         # сериализатора 2 поля - data и instance - то сериализатор понимает, что надо вызвать
#         # метод update
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error", "Method DELETE not allowed"})
#
#         try:
#             instance = Games.objects.get(pk=pk)
#             instance.delete()  # Удаляем объект из базы данных
#             return Response({"games": "Game " + str(pk) + " deleted successfully"})
#         except Games.DoesNotExist:
#             return Response({"error": "Object not found"})