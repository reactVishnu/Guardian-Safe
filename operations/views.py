from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
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


class EmployeeUpdateView(UpdateView):
    model = Details
    fields = '__all__'
    template_name = "operations/create_emp.html"
    success_url = reverse_lazy('operations:all details')

    def get_object(self, queryset=None):
        # Use employee_code for lookup instead of primary key
        return get_object_or_404(Details, employee_code=self.kwargs['employee_code'])


class EmployeeCreateView(CreateView):
    model = Details
    fields = '__all__'
    template_name = 'operations/create_emp.html'
    success_url = reverse_lazy('operations:all details')


class EmployeeDeleteView(DeleteView):
    model = Details
    template_name = "operations/emp_delete.html"
    context_object_name = 'employee'
    success_url = reverse_lazy('operations:all details')

    def get_object(self, queryset=None):
        # Use employee_code for lookup instead of primary key
        return get_object_or_404(Details, employee_code=self.kwargs['employee_code'])


