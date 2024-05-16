from django.urls import path

from . import views
app_name = "Lab5App"
urlpatterns = [
    path("", view=views.default, name="default"),
    path("add", view=views.add, name="add")
]