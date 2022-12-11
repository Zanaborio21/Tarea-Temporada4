from django.urls import path
from .views import home,newPost,modPost,detalle,registro_usuario,eliminar
urlpatterns = [
    path('', home,name=""),
    path('newpost/',newPost,name='newpost'),
    path('modpost/<id>/',modPost,name='modpost'),
    path('eliminar/<id>',eliminar,name="eliminar"),
    path("detalle/<id>",detalle,name="detalle"),
    path('registro/',registro_usuario,name='registro_usuario'),
]