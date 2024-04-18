from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio_project.urls', namespace='portfolio')),
    path('task_manager/', include('task_manager.urls', namespace='task_manager'))
]
