from django.db import models

# Create your models here.
class Games(models.Model):
    title = models.CharField(max_length=30)
    #blank=True - поле может быть пустым
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    #В Django category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    #это определение поля модели, которое создает связь "многие к одному" (ForeignKey) с другой моделью.
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
         return self.title

class Category(models.Model):
    class GameType(models.TextChoices):
        STRATEGY = 'STR', 'Strategy'
        RPG = 'RPG', 'Role-Playing Game'
        ACTION = 'ACT', 'Action'

    name = models.CharField(
        max_length=3,
        choices=GameType.choices,
        db_index=True
    )

    def __str__(self):
        return self.get_name_display()

    # Пример использования:
    # category = Category(name=Category.GameType.RPG)
    # category.save()
    # print(category)  # Выведет: Role-Playing Game