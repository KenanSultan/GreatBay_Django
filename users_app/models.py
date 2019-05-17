from django.db import models
from django.contrib.auth.models import User


class Customer(User):
    CUSTOMER_TYPE_CONSUMER = 1
    CUSTOMER_TYPE_OWNER = 2

    customer_types = {
        CUSTOMER_TYPE_CONSUMER: 'Consumer',
        CUSTOMER_TYPE_OWNER: 'Owner'
    }


    customer_type = models.IntegerField(choices=list(customer_types.items()))

    def save(self, *args, **kwargs):
        self.set_password(self.password)

        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.customer_types[self.customer_type]}"

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'