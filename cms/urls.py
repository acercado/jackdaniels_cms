__author__ = 'acercado'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^contests$', views.contests, name='contests'),
    url(r'^promos$', views.promos, name='promos'),
    url(r'^newsfeeds$', views.newsfeeds, name='newsfeeds'),

    url(r'^location/accounts$', views.location_accounts, name='location_accounts'),
    url(r'^location/accounts/new$', views.location_new_account, name='location_new_account'),
    url(r'^location/accounts/edit/(?P<pk>[0-9]+)$', views.location_edit_account, name='location_edit_account'),
    url(r'^location/accounts/delete/(?P<pk>[0-9]+)$', views.location_del_account, name='location_del_account'),
    
    url(r'^location/products$', views.location_products, name='location_products'),
    url(r'^location/products/new$', views.location_new_product, name='location_new_product'),
    url(r'^location/products/edit/(?P<pk>[0-9]+)$', views.location_edit_product, name='location_edit_product'),
    url(r'^location/products/delete/(?P<pk>[0-9]+)$', views.location_del_product, name='location_del_product'),
    
    url(r'^location/promotions$', views.location_promotions, name='location_promotions'),

    url(r'^rewards$', views.rewards, name='rewards'),
    # url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    # url(r'^post/new/$', views.post_new, name='post_new'),
    # url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    # url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    # url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
    # url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
]