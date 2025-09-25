from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auctions/add/<int:list_id>/', views.add, name='add'),
    path('<int:list_id>/', views.display, name='display'),
    path('<int:list_id>/',views.remove,name='remove'),
    #path('<int:list_id>/edit/', views.edit, name='edit'),  # Unique URL for edit page


]
