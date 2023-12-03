from django.shortcuts import render
from django.views.generic import ListView, DetailView
from core.models import Details
from django.shortcuts import get_object_or_404

# Create your views here.


class UserDetailsListView(ListView):
    model = Details
    template_name = 'operations/details_list.html'


class IndividualEmployeeDetailView(DetailView):
    model = Details
    template_name = 'operations/employee_detail.html'
    context_object_name = 'employee'

    def get_object(self, queryset=None):
        # Use employee_code for lookup instead of primary key
        return get_object_or_404(Details, employee_code=self.kwargs['employee_code'])