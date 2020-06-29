from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
app_name = 'HrJobs'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboards.urls')),
    path('accounts/', include('accounts.urls', namespace="accounts")),
    path('jobs/', include('JobsAvailable.urls', namespace="jobs")),
    path('candidates/', include('candidates.urls', namespace="candidates")),
    path('recruiters/', include('recruiters.urls', namespace="recruiters")),
    path('Interviews/', include('interviews.urls', namespace="interviews")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),