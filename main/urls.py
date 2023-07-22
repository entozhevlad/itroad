from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('maps/', views.maps, name='maps'),
    path('profile', views.profile_view, name='profile'),
    path('register', views.RegisterView.as_view(),name='register'),
    path('maps/languages', views.languages, name='language'),
    path('maps/track', views.track, name='track'),
    path('maps/other', views.maps_other, name='other')
]