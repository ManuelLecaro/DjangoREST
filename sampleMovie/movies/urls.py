from django.conf.urls import url, include
from movies import views
urlpatterns = [
    url(r'^listar', views.ListaRating,name='rating_listar'),
	
	url(r'^crear/(?P<pk>\d+)/$', views.ProfileDetail.as_view(),name='rating_crear'),
	url(r'^editar/(?P<pk>\d+)/$', views.ProfileDetail.as_view(),name='rating_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$', views.RatingDelete.as_view(),name='rating_eliminar'),
	url(r'^ratings/$', views.rating_list),
    #url(r'^ratings/(?P<pk>[0-9]+)$', views.rating_detail),

]
