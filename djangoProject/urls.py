

from django.urls import path

from . import views

urlpatterns = [
    path('format/', views.string_formatter),
    path('all/', views.get_all_results)
]
