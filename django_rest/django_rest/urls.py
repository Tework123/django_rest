from django.contrib import admin
from django.urls import path

from men.views import MenView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/men_list/', MenView.as_view())
]
