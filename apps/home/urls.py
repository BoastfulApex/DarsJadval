from django.urls import path
from apps.home import views

urlpatterns = [

    path('', views.index, name='home'),
    path('teachers/', views.teachers, name='home-teachers'),
    path('teachers_create/', views.teachers_create, name='home-teachers-create'),
    path('teachers_file_create/', views.teachers_file_create, name='home-teachers-file-create'),
    path('teachers_detail/<int:pk>', views.teacher_detail, name='home-teachers-detail'),
    path('teachers_delete/<int:pk>', views.TeacherDelete.as_view(), name='home-teachers-delete'),
    path('groups/', views.study_groups, name='home-groups'),
    path('groups_create/', views.group_create, name='home-groups-create'),
    path('groups_detail/<int:pk>', views.group_detail, name='home-groups-detail'),
    path('groups_delete/<int:pk>', views.StudyGroupDelete.as_view(), name='home-groups-delete'),
]
