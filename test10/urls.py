
from django.contrib import admin
from django.urls import path, include, re_path
from poker_logic.views.core import IndexTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point"),
]
