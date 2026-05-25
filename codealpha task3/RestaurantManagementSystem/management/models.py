from django.db import models

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.table_number}"


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    table = models.ForeignKey(Table,on_delete=models.CASCADE)
    reservation_time = models.DateTimeField()

    def __str__(self):
        return self.customer_name


class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    menu_item = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name


class Inventory(models.Model):
    item_name = models.CharField(max_length=100)
    stock = models.IntegerField()

    def __str__(self):
        return self.item_name