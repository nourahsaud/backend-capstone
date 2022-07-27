from django.urls import path
from . import views

app_name = "jobs"

urlpatterns = [
    path("add_job", views.add_job, name="add_job"),
    path("get_jobs", views.get_jobs, name="add_job"),
    path("delete_job/<job_id>", views.delete_job, name="add_job"),
    path("edit_job/<job_id>", views.edit_job, name="add_job"),
]