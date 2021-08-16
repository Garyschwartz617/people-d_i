from django.urls import path

from .views import homepage, peoples,id

urlpatterns = [
    path('', homepage),
    path('peoples', peoples),
    path('id/<int:num>', id),
]
