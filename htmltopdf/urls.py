from django.urls import path

from .views import home, generate_pdf

urlpatterns = [
    path("", home, name="home"),
    path("pdf", generate_pdf, name="pdf"),
]
