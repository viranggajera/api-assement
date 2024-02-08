from django.urls import path
from app_api import views

urlpatterns = [
   path("employeeapi/", views.employeeapi),
   path("employeedetailapi/<int:employee_id>", views.employeedetailapi),
   path("post", views.post)
]