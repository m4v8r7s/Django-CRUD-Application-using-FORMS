from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('employee/', views.employee_form, name = 'employee_insert'), #get and post request for insert operations
    path('<int:id>/', views.employee_form, name = 'employee_update'), # get and post request for update operations
    path('delete/<int:id>/', views.employee_delete, name = 'employee_delete'), # delete and post request for delete operations
    path('list/', views.employee_list, name = 'employee_list'), # get request to display and retrieve all records
    path('signup', views.signup, name = 'signup'), # sign up
    path('signin', views.signin, name = 'signin'), # sign in
    path('signout', views.signout, name = 'signout'), # sign out
    
]