from django.urls import path
from .views import CreateListStudent

urlpatterns = [
    path("student", CreateListStudent.as_view(), name="student")
]