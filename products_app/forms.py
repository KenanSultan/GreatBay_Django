from django.forms import ModelForm
from .models import *


class ProductCreateForm(ModelForm):
    class Meta:
        fields = ('category', 'title', 'price', 'description')
        model = Product

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(owner=user)