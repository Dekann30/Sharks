from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sharks/', views.sharks_index, name='index'),
    path('sharks/<int:shark_id>/', views.shark_detail, name='detail'),
    path('sharks/create/', views.SharkCreate.as_view(), name='sharks_create'),
    path('sharks/<int:pk>/update/', views.SharkUpdate.as_view(), name= 'shark_update'),
    path('sharks/<int:pk>/delete/', views.SharkDelete.as_view(), name='shark_delete'),
]
