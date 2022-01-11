from django.urls import path
from .views import MyUserViewset
from DjangoRestApis import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', MyUserViewset.as_view({'post': 'create',
                                           'get': 'retrieve',
                                           'put': 'update',
                                           'delete': 'destroy'}))
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
