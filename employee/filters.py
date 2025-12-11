import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Employee
        fields = ['designation']