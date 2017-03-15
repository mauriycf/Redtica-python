"""redtica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url, include

"""url(r'^$', IndexView.as_view()),
    url(r'^entrada/(?P<slug>[-\w]+)/$', EntradaDetailView.as_view()),"""

"""from blog.views import IndexView, EntradaDetailView"""
from blog.views import(
    post_list,
    post_detail,
    )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^draceditor/', include('draceditor.urls')),
    url(r'^$', post_list),
    url(r'^entrada/(?P<slug>[-\w]+)/$', post_detail),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)