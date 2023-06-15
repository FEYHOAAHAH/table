from django.db import models


# Create your models here.

class Products(models.Model):
    idd = models.IntegerField()
    product = models.CharField(max_length=100)
    count = models.IntegerField()

    def __str__(self):
        return f"{self.idd} - {self.product} - {self.count}"


class Orders(models.Model):
    order_number = models.IntegerField()
    client_name = models.CharField(max_length=100)
    product_id = models.IntegerField()
    order_cost = models.IntegerField()

    def __str__(self):
        return f"{self.order_number} - {self.client_name} - {self.product_id} - {self.order_cost}"


class Users(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=100)
    user_nickname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user_id} - {self.user_name} - {self.user_nickname}"


class Mouses(models.Model):
    m_developer = models.CharField(max_length=100)
    m_count = models.IntegerField()

    def __str__(self):
        return f"{self.m_developer} - {self.m_count}"


class Keyboards(models.Model):
    k_developer = models.CharField(max_length=100)
    k_count = models.IntegerField()

    def __str__(self):
        return f"{self.k_developer} - {self.k_count}"


class Headphones(models.Model):
    h_developer = models.CharField(max_length=100)
    h_count = models.IntegerField()

    def __str__(self):
        return f"{self.h_developer} - {self.h_count}"


class Gamepads(models.Model):
    g_developer = models.CharField(max_length=100)
    g_count = models.IntegerField()

    def __str__(self):
        return f"{self.g_developer} - {self.g_count}"


class Notebooks(models.Model):
    n_developer = models.CharField(max_length=100)
    n_count = models.IntegerField()

    def __str__(self):
        return f"{self.n_developer} - {self.n_count}"
