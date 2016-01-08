from django.conf.urls import patterns, include, url
from django.contrib import admin
from myMusic import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name="index"),
    url(r'^player/$', views.player, name="player"),
    url(r'^related_videos/$', views.related_videos, name="related_videos"),
    url(r'^add_to_queue/$', views.add_to_queue, name="add_to_queue"),
    url(r'^about/$', views.about, name="about"),
)
