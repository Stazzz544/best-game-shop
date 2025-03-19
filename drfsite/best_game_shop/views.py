# from django.core.serializers import serialize
# from django.forms import model_to_dict
# from rest_framework.response import Response
# from rest_framework.views import APIView
from .models import Games
from .serializers import GamesSerializer
from rest_framework import viewsets, mixins

# Create your views here.
#class GamesAPIView(generics.ListAPIView):
    #если у Games подчёркнут objects - это потому, что у меня халявная версия pycharm
#   queryset = Games.objects.all()
#   serializer_class = GamesSerializer



# Так можно создать все и сразу ЭП
# class GamesViewSet(viewsets.ModelViewSet):
#     queryset = Games.objects.all()
#     serializer_class = GamesSerializer

#А так можно выборочно добавлять миксины и получать сразу апишки
class GamesViewSet( mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer    

# mixins.CreateModelMixin,
# mixins.RetrieveModelMixin,
# mixins.UpdateModelMixin,
# mixins.DestroyModelMixin,
# mixins.ListModelMixin,
# GenericViewSet

#--------------------------------------------------------
# вариант создания ЭП

# class GamesApiList(generics.ListCreateAPIView):
#     queryset = Games.objects.all()
#     serializer_class = GamesSerializer

# class GamesAliUpdate(generics.UpdateAPIView):
#     # Это ленивый запрос. Тут просто связывавется queryset с моделью Games
#     # класс сам обработает атрибут и возвратит одну запись
#     queryset = Games.objects.all()
#     serializer_class = GamesSerializer

# class GamesApiDelete(generics.DestroyAPIView):
#     queryset = Games.objects.all()
#     serializer_class = GamesSerializer

# #универсальный CRUD метод
# class GamesApiDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Games.objects.all()
#     serializer_class = GamesSerializer

#--------------------------------------------------------

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