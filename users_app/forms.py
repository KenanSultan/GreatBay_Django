from django.forms import ModelForm
from .models import Customer


class CustomerCreateForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'username', 'password', 'customer_type')