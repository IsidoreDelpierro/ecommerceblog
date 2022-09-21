from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from blog.views import NewMigrate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('store/', include('store.urls')),
    #path('info/', include('info.urls')),
    path('migrate/', NewMigrate.as_view(), name="migrate"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
