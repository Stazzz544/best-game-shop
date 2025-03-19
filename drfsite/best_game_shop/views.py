# from django.core.serializers import serialize
# from django.forms import model_to_dict
# from rest_framework.response import Response
# from rest_framework.views import APIView
from .models import Category, Games
from .serializers import GamesSerializer
from rest_framework import viewsets, mixins 
from rest_framework.decorators import action
from rest_framework.response import Response

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
    #queryset = Games.objects.all()
    serializer_class = GamesSerializer    

    #переопределение метода # queryset (его нужно в этом случае закомментить)
    #возвращает 3 записи или одну запись по id. Можно более сложные запросы писать
    def get_queryset(self):
        pk=self.kwargs.get('pk')
        if not pk:
            return Games.objects.all()[:3] 
        
        return Games.objects.filter(pk=pk)
    
    #http://127.0.0.1:8000/api/v1/games/1/category/
    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        category = Category.objects.get(pk=pk)
        return Response({'category': category.name})

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