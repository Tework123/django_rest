from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter, Route, DynamicRoute

from men.views import MenViewList, MenViewDetail
from rest_framework import routers

# создаем собственный router, делает тоже, что и стандартный роутер
# class MyCustomRouter(routers.SimpleRouter):
#     """
#     A router for read-only APIs, which doesn't use trailing slashes.
#     """
#     routes = [
#         Route(
#             url=r'^{prefix}/$',
#             mapping={'get': 'list'},
#             name='{basename}-list',
#
#             # если false, то будет список возвращается, а иначе одна запись
#             detail=False,
#             initkwargs={'suffix': 'List'}
#         ),
#         Route(
#             url=r'^{prefix}/{lookup}/$',
#             mapping={'get': 'retrieve'},
#             name='{basename}-detail',
#             detail=True,
#             initkwargs={'suffix': 'Detail'}
#         ),
#         DynamicRoute(
#             url=r'^{prefix}/{lookup}/{url_path}$',
#             name='{basename}-{url_name}',
#             detail=True,
#             initkwargs={}
#         )
#     ]
# router = MyCustomRouter()
# router.register(r'men', MenViewSet, basename='men')

# router = routers.DefaultRouter()
# # basename обязательный, если не установлен queryset в view, он не сможет создать маршруты по модели
# router.register(r'men', MenViewSet, basename='men')
# print(router.urls)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/', include(router.urls)),

    path('api/v1/men/', MenViewList.as_view()),
    path('api/v1/men/<int:pk>/', MenViewDetail.as_view()),

    # маршрут для авторизации
    path('api/v1/drf_auth/', include('rest_framework.urls')),

    # маршрут для авторизации djoser
    path('api/v1/auth/', include('djoser.urls')),
    # отвечает за авторизацию по токена, сюда нужно слать их
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    # path('api/v1/men_list/', MenViewSet.as_view({'get': 'list', })),
    # path('api/v1/men_list/<int:pk>', MenViewSet.as_view({'put': 'update', })),
    # path('api/v1/men_detail/<int:pk>', MenViewDetail.as_view())
]
