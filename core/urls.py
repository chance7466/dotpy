from django.conf.urls.defaults import *
from dotpy.core import views

urlpatterns = patterns('',
    (r'^signin/$', views.signin),
    (r'^signout/$', views.signout),
    (r'^signup/$', views.signup),
    url(r'^confirm/(?P<code>\w+)/$', views.confirm, name='confirm-signup'),
)
