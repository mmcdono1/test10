
from django.contrib import admin
from django.urls import path, include, re_path
from poker_logic.views.core import IndexTemplateView
from poker_logic.views.tracks import tracks_all


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('tracks/all/', tracks_all, name='tracks_all'),
    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point"),

]
