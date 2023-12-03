from django.urls import path
from .views import UserDetailsListView, IndividualEmployeeDetailView

app_name='operations'

urlpatterns=[path('details', UserDetailsListView.as_view(), name='all details'),
             path('detail/<str:employee_code>', IndividualEmployeeDetailView.as_view(), name='detail')
             ]
