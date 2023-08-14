from django.contrib import admin
from django.urls import path, include

from men.views import MenViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'men', MenViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),

    # path('api/v1/men_list/', MenViewSet.as_view({'get': 'list', })),
    # path('api/v1/men_list/<int:pk>', MenViewSet.as_view({'put': 'update', })),
    # path('api/v1/men_detail/<int:pk>', MenViewDetail.as_view())
]
