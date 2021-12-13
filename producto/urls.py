from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio,name='home'),
    path('inicio',views.inicio, name= 'inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('productos', views.productos,name='productos'),
    path('productosjson', views.productosjson,name='productosjson'),
    path('productos/crear', views.crear,name='crear'),
    path('productos/editar/<int:id>', views.editar, name='editar'),
    path('productos/eliminar/<int:id>',views.eliminar,name='eliminar')

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

