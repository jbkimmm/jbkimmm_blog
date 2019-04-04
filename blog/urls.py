from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from posts.views import (
    index, camp_map, blog, post, search, 
    post_create, post_update, post_delete)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('campmap/', camp_map, name='camp-map'),
    path('blog/', blog, name='post-list'),
    path('search/', search, name='search'),
    path('create/', post_create, name='post-create'),
    path('post/<id>/', post, name='post-detail'),
    path('post/<id>/update/', post_update, name='post-update'),
    path('post/<id>/delete/', post_delete, name='post-delete'),
    path('tinymce/', include('tinymce.urls')),
    path('profile/', include('users.urls', namespace='users')),
    path('autopost/', include('autopost.urls', namespace='autopost')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)