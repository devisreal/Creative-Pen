from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users.views import user_external
from blog.views import create_post

urlpatterns = [
    path('froala_editor/', include('froala_editor.urls')),
    path('taggit/', include('taggit_selectize.urls')),
    path('pen_admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('auth/', include('account.urls')),
    path('', include('pages.urls')),
    path('<slug:slug>/', include('users.urls')),
    path('@<slug:slug>/', user_external, name='author_external'),
    path('post/new/', create_post, name='new_post')    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)