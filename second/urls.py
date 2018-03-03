from django.conf.urls import url

from second.views import create,update,index,delete,view

urlpatterns = [


    url(r'^create$', create.as_view(), name="myview"),
    url(r'^index$', index.as_view(), name="index"),
    url(r'^update/(?P<pk>[0-9]+)$', update.as_view(), name="index"),
    url(r'^delete/(?P<pk>[0-9]+)$', delete.as_view(), name="index"),
    url(r'^view/(?P<pk>[0-9]+)$', view.as_view(), name="index"),
]