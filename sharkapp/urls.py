from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sharks/', views.sharks_index, name='index'),
    path('sharks/<int:shark_id>/', views.shark_detail, name='detail'),
    path('sharks/create/', views.SharkCreate.as_view(), name='sharks_create'),
    path('sharks/<int:pk>/update/', views.SharkUpdate.as_view(), name= 'shark_update'),
    path('sharks/<int:pk>/delete/', views.SharkDelete.as_view(), name='shark_delete'),
    # path('sharks/<int:shark_id>/add_sighting/', views.add_sighting, name='add_sighting'),
    path('sharks/<int:shark_id>/assoc_sighting/<int:sighting_id>/', views.assoc_sighting, name='assoc_sighting'),
    path('sightings/', views.SightingList.as_view(), name='sightings_index'),
    path('sightings/<int:pk>/', views.SightingDetail.as_view(), name='sightings_detail'),
    path('sightings/create/', views.SightingCreate.as_view(), name='sightings_create'),
    path('sightings/<int:pk>/update', views.SightingUpdate.as_view(), name='sightings_update'),
    path('sightings/<int:pk>/delete/', views.SightingDelete.as_view(), name='sightings_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]
