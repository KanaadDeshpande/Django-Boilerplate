from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
        path('jet/', include('jet.urls', 'jet')), 
        path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    ]
