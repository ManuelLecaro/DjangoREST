from django.conf.urls import url, include
from client import views
urlpatterns = [
    url(r'^listar', views.getRating,name='rating_listar'),
	url(r'^crear/', views.createRating,name='rating_crear'),
	url(r'^editar/(?P<pk>\d+)/$', views.updateRating,name='rating_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$', views.deleteRating,name='rating_eliminar'),
	#url(r'^ratings/$', views.rating_list),
    #url(r'^ratings/(?P<pk>[0-9]+)$', views.rating_detail),

]