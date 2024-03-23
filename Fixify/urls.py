from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('authentication.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]
urlpatterns += staticfiles_urlpatterns()
