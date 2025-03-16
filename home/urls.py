from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import home 

urlpatterns = [
    path('', views.LandingPage, name="LandingPage"),
    path('home/', views.home, name="home"),
    path('add_meme/',views.add_meme, name="add_meme"),
    path('delete_meme/<memeid>',views.delete_meme, name="delete_meme"),
    path('update_meme/<memeid>',views.update_meme, name="update_meme"),
    path('login/',views.Login,name="login"),
    path('Signup/',views.Signup,name="Signup"),
    path('logout/',views.Logout_view,name='Logout_view'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)