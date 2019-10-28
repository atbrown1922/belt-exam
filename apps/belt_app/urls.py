from django.conf.urls import url
from . import views	# the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
    url(r'^$', views.home),
    url(r'dashboard$', views.dashboard), 
    url(r'^dashboard/(?P<user_id>\d+)$', views.index),
    url(r'addJob$', views.add_job),
    url(r'create_job$', views.create_job),
    url(r'^view/(?P<job_id>\d+)$', views.view), 
    url(r'^edit/(?P<job_id>\d+)$', views.edit), 
    url(r'^update/(?P<job_id>\d+)$', views.update),
    url(r'^cancel/(?P<job_id>\d+)$', views.destroy), 
    url(r'^registration$', views.registration),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
]