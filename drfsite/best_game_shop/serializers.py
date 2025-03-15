from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import  Games


# class GamesModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

#class GamesSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Games
#        fields = ('title', 'category_id')


#тут прописывается практически тоже самое, что и в models.py, но обрати внимание на category
class GamesSerializer(serializers.ModelSerializer):
   class Meta:
       model = Games
       #если надо отдать конкретные поля"
       #fields = ("title", "content", "category") #просто category, а не catId

       #вариант отдать "сразу всё"
       fields = "__all__"

#Вариант с ручным прописыванием сериализатора
# class GamesSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)#помечаем, чтобы было необязательно
#     # отпарвлять с фронта
#     time_update = serializers.DateTimeField(read_only=True)
#     category_id = serializers.IntegerField() # тут сеез подстрочник добавляется id и код
#     # понимает, что мы к ключу у category из Games(models.Model) обращаемся
#
#     def create(self, validated_data):
#         return Games.object.create(**validated_data) #**validated_data - распакованный словарь
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance)
#         instance.content = validated_data.get("content", instance)
#         instance.time_update = validated_data.get("time_update", instance)
#         instance.category_id = validated_data.get("category_id", instance)
#         instance.save()
#         return instance

# def encode():
#     model = GamesModel('my title', 'my content')
#     model_sr = GamesSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep = '\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)