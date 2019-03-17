from django.urls import path
from django.contrib.auth import views as auth_views
from .views import ( autopost_list,autopost_crawling, autopost_create, 
    autopost_update, autopost_delete, autopost_detail, autopost_crawl, autopost_crawl_test )

app_name = 'autopost'

urlpatterns = [
    path('autopost/', autopost_list, name='autopost-list'),
    path('autocrawling/<int:id>', autopost_crawl, name='autopost-crawl'),
    path('autocrawling_test/<int:id>', autopost_crawl_test, name='autopost-crawl-test'),
    path('autopost/create', autopost_create, name='autopost-create'),
    path('autopost/<int:id>', autopost_detail, name='autopost-detail'),
    path('autopost/update/<int:id>', autopost_update, name='autopost-update'),
    path('autopost/delete/<int:id>', autopost_delete, name='autopost-delete'),
    path('postcrawling/', autopost_crawling, name='autopost-crawling'),
]