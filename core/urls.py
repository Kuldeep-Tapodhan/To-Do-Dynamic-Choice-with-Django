from django.urls import path, include
from . import views     
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet)

urlpatterns = [
    path('', views.task_board_page, name='task-board'),
    path('api/', include(router.urls)),
    path('api/register/', views.RegisterView.as_view(), name='api-register'),
    path('api/profile/', views.UserProfileView.as_view(), name='api-profile'),
    path('api/users/', views.UserListView.as_view(), name='api-users'),
]
