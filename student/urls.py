from django.urls import path
from .views import *

urlpatterns = [
    
    path('', student_list, name='student-list'),
    path('create/', create_student, name='create-student'),
    path('update/<int:id>/', update_student, name='update-student'),
    
]