from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .views import *

app_name = 'games'

urlpatterns = [
path('player-create/', PlayerCreate.as_view(), name='player-create'),


    path('player-detail/<int:pk>/', login_required(PlayerDetail.as_view()), name='player-detail'),
    
    
    path('player-update/<int:pk>/', PlayerUpdate.as_view(), name='player-update'),
    path('player-delete/<int:pk>/', PlayerDelete.as_view(), name='player-delete'),
url(r'^login/$', login_user, name = 'login'),
    # url(r'^main/$', main, name="main"),
    url(r'^signup/$', signup, name='signup'),
    url(r'logout', LogoutView.as_view(template_name="games/logout.html"), name='logout')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)