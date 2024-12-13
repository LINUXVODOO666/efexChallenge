from django.urls import path
from students.api.views import Student, StudentById

urlpatterns = [
    path('students/', Student.as_view(),name='students'),
    path('students/<int:student_id>/', StudentById.as_view(),name='studentId'),
]
