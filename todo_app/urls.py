from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin-area/', admin.site.urls),
    path('', include('tasks.urls')),
    path('account/', include('accounts.urls')),
]