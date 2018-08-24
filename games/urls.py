from django.urls import path, re_path
from django.conf import settings
from django.conf.urls import include
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from .views import *

app_name = 'games'

urlpatterns = [
    path('player-detail/', login_required(PlayerDetail.as_view()), name='player-detail'),
    path('player-update/', login_required(PlayerUpdate.as_view()), name='player-update'),
    
    re_path(r'^login/$', LoginView.as_view(), name = 'login'),
    re_path(r'^signup/$', SignUp.as_view(), name='signup'),
    re_path(r'logout', LogoutView.as_view(), name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)