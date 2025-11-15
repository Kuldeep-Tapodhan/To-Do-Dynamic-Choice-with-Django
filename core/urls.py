from django.urls import path, include
from . import views,create_admin
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet)

urlpatterns = [
    path('', views.task_board_page, name='task-board'),
    path('api/', include(router.urls)),
    path('create-admin/', create_admin),
]