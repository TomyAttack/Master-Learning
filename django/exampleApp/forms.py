from django import forms
# from .models import GeeksModel
from .models import Employee
class EmployeeForm(forms.ModelForm):
	class Meta:
		model = Employee
		# fields = '__all__'
		fields = ('full_name', 'emp_code', 'mobile', 'position')
		labels = {
			'full_name':'Full Name',
			'emp_code':'Employee Code'
		}