from django.urls import path

from . import views

urlpatterns = [
    path("group", views.group_create, name="group"),
    path("groups", views.get_groups_list, name="get_groups_list"),
]
