"""
URL configuration for drfsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

#swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from best_game_shop.views import * #импортируем всё, что есть в файле

router = routers.SimpleRouter()
router.register(r'games', GamesViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Your API",
      default_version='v1',
      description="API description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@yourapi.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)), # http://127.0.0.1:8000/api/v1/games/ - games это 'r'

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # path('api/v1/gameslist', GamesViewSet.as_view({'get': 'list'})),
    # path('api/v1/gameslist/<int:pk>/', GamesViewSet.as_view({'put': 'update'}))
 
    # path('api/v1/gameslist/', GamesApiList.as_view()),
    # # тут класс сам поймёт, какой из методов дальше вызвать
    # path('api/v1/gameslist/<int:pk>/', GamesApiList.as_view()), 
    # path('api/v1/game_delete/<int:pk>/', GamesApiDelete.as_view()),
]

