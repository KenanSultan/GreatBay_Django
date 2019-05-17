from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import *
from django.urls import reverse_lazy
from users_app.models import Customer
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProductCreateForm
from django.core.exceptions import ValidationError

class Categories(LoginRequiredMixin, ListView):
    model = Category
    login_url = reverse_lazy('login')
    template_name = 'categories.html'

    def get_queryset(self):
        qs = super().get_queryset()

        qs = qs.filter(owner=self.request.user).order_by('name')

        return qs

class Products(LoginRequiredMixin, ListView):
    model = Product
    login_url = reverse_lazy('login')
    template_name = 'products.html'

    def get_queryset(self):
        qs = super().get_queryset()

        qs = qs.filter(owner=self.request.user).order_by('category')

        return qs
    

class CreateCategory(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'create_category.html'
    fields = ('name',)
    success_url = reverse_lazy('categories')
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super(LoginRequiredMixin, self).get_context_data(**kwargs)
        context['users_fullname'] = f"{self.request.user.first_name} {self.request.user.last_name}"
        return context

    def form_valid(self, form):
        form.instance.owner = Customer.objects.get(pk=self.request.user.pk)
        return super(LoginRequiredMixin, self).form_valid(form)


class CreateProduct(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'create_product.html'
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('create_product')
    form_class = ProductCreateForm

    def get_form_kwargs(self):
        kwargs = super(LoginRequiredMixin, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.owner = Customer.objects.get(pk=self.request.user.pk)
        # try:
        #     form.instance.category = Category.objects.get(pk=form.instance.category.pk, owner=self.request.user)
        # except:
        #     raise ValidationError("Category is wrong")

        return super(LoginRequiredMixin, self).form_valid(form)