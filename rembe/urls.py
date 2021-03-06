from unicodedata import name
"""rembe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path


from core.views.profile import profile
from core.views.home import home

urlpatterns = [

    re_path(r'^$', home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('tarjetas/', include('core.urls', namespace='tarjetas')),
    path('accounts/profile/', profile),
    path('markdownx/', include('markdownx.urls')),
    # path('tarjeta/', TarjetaView.as_view()),
]


handler400 = 'core.views.error.error_400'
handler403 = 'core.views.error.error_403'
handler404 = 'core.views.error.error_404'
handler500 = 'core.views.error.error_500'