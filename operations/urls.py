from django.urls import path
from .views import UserDetailsListView, IndividualEmployeeDetailView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView

app_name='operations'

urlpatterns=[path('details', UserDetailsListView.as_view(), name='all details'),
             path('detail/<str:employee_code>', IndividualEmployeeDetailView.as_view(), name='detail'),
             path('create', EmployeeCreateView.as_view(), name='create'),
             path('update/<str:employee_code>',EmployeeUpdateView.as_view(), name='update'),
             path('delete/<str:employee_code>',EmployeeDeleteView.as_view(), name='delete')
             ]
