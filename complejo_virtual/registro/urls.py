from django.urls import path
from .views import registro,cerrar_sesion,logear,password_reset_request,password_reset_done
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('login/', logear, name='login'),
    path('password_reset/', password_reset_request, name='password_reset'),
    path('password_reset/done/', password_reset_done, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
   
    
]