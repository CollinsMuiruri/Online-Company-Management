from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.home, name='home'),
    url(r'^index', views.index, name='index'),
    url(r'^search', views.search_results, name='search_results'),
    url(r'^image/(\d+)', views.image, name='image'),
    url(r'^manage', views.manage, name='manage'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
