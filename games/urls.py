from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static

from .views import *

app_name = 'games'

urlpatterns = [
    path('test', test, name='test'),

    path('player-create/', login_required(PlayerCreate.as_view()), name='player-create'),
    path('player-detail/', login_required(PlayerDetail.as_view()), name='player-detail'),
    path('player-update/<int:pk>/', PlayerUpdate.as_view(), name='player-update'),
    path('player-delete/<int:pk>/', PlayerDelete.as_view(), name='player-delete'),
    
    url(r'^login/$', LoginView.as_view(), name = 'login'),
    url(r'^signup/$', signup, name='signup'),
    url(r'logout', LogoutView.as_view(template_name="games/logout.html"), name='logout')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)