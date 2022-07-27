from django.urls import path
from . import views


urlpatterns = [
    # Employee
    path("add_emp/", views.addEmployee, name="add_emp"),
    path("get_emp/", views.getEmployee, name="get_emp"),
    path("my_emp/", views.getCompanyEmployee, name="get_comp_emp"),
    path("edit_emp/<emp_id>", views.editEmployee, name="edit_emp"),
    path("delete_emp/<emp_id>", views.deleteEmployee, name="delete_emp"),
    path("emp/<employee_id>", views.getEmp, name="single_employee"),
    # Requests 
    path("add_req/<emp_id>", views.add_req, name="add_req"),
    path("get_sent_req/", views.get_sent, name="get_sent_req"),
    path("get_received_req/", views.get_received, name="get_received_req"),
    path("delete_req/<req_id>", views.delete_req, name="delete_req"),
    # Fav
    path("add_fav/<emp_id>", views.add_fav, name="add_fav"),
    path("get_fav/", views.get_fav, name="get_fav"),
    path("delete_fav/<fav_id>", views.delete_fav, name="delete_fav"),
]
