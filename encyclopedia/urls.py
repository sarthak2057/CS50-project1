from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>",views.display, name="display"),
    path("Create",views.create,name="create"),
    path("search",views.search,name="search"),
    path('random',views.random,name='random'),
    path("edit/<str:entryTitle>",views.editPost,name="edit")
]
