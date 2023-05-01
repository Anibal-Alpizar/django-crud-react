# frontend urls
from django.urls import include, path
from rest_framework import routers
from tasks import views
from rest_framework.documentation import include_docs_urls

# api version
router = routers.DefaultRouter()
router.register(r'tasks', views.TaskView, 'task')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('docs/', include_docs_urls(title='Task API'))
]
