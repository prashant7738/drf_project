import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(lookup_expr='iexact')
    emp_name = django_filters.CharFilter(lookup_expr='icontains')
    
    # # it gives range of filter for any integer field 
    # id = django_filters.RangeFilter(field_name='id')
    
    # But for char field like EMP001 we need to use custom fields 
    id_max = django_filters.CharFilter(method='filter_by_emp_id' , label='Emp_Max')
    id_min = django_filters.CharFilter(method='filter_by_emp_id' , label='Emp_Min')

    class Meta:
        model = Employee
        fields = ['designation', 'emp_name', 'id_max','id_min']
        
    def filter_by_emp_id(self, queryset ,name ,  value ):
        
        if name == 'id_min':
            return queryset.filter(emp_id__gte= value)
        elif name == 'id_max':
            return queryset.filter(emp_id__lte= value)
        
        return queryset