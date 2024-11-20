from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
   path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('user_interface/', views.user_interface_view, name='user_interface'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
     path('facture/<int:facture_id>/', views.facture_detail_view, name='facture_detail'),
        path('facture/<int:facture_id>/recu/', views.generer_recu, name='generer_recu'),
       path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]