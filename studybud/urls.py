
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    # FOR API FOLDER
    path('api/', include('base.api.urls'))
]
