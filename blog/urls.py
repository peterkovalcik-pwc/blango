from django.urls import include, path
from . import views

urlpatterns = [
    path('blog/', views.index, name='index'),
]