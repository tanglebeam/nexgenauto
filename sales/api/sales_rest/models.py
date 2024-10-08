from django.db import models

# Create your models here.


class AutomobileVO(models.Model):
    vin = models.CharField(max_length=17, unique=True)
    sold = models.BooleanField(default=False)

    def __str__(self):
        return self.vin


# ====================================================


class Salesperson(models.Model):
    DEFAULT_HEADSHOT_URL = "https://t4.ftcdn.net/jpg/02/15/84/43/360_F_215844325_ttX9YiIIyeaR7Ne6EaLLjMAmy4GvPC69.jpg"

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    employee_id = models.CharField(max_length=200, unique=True)
    picture_url = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        default=DEFAULT_HEADSHOT_URL,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# ====================================================


class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# ====================================================


class Sale(models.Model):
    price = models.CharField(max_length=50)

    automobile = models.ForeignKey(
        AutomobileVO,
        related_name="sales",
        on_delete=models.PROTECT,
    )
    salesperson = models.ForeignKey(
        Salesperson,
        related_name="sales",
        on_delete=models.PROTECT,
    )
    customer = models.ForeignKey(
        Customer,
        related_name="sales",
        on_delete=models.PROTECT,
    )
