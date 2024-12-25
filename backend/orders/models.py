from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=100)  # Название поставщика
    contact_email = models.EmailField()  # Email для связи с поставщиком

    def __str__(self):
        return self.name  # Строковое представление модели

class Product(models.Model):
    name = models.CharField(max_length=100)  # Название товара
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена товара
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)  # Связь с поставшиком

    def __str__(self):
        return self.name  # Строковое представление модели

class Customer(models.Model):
    username = models.CharField(max_length=100)  # Имя пользователя
    email = models.EmailField(unique=True)  # Уникальный email
    password = models.CharField(max_length=100)  # Пароль (в реальном приложении используйте хеширование)

    def __str__(self):
        return self.username  # Строковое представление модели

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Связь с клиентом
    products = models.ManyToManyField(Product)  # Связь с товарами
    status = models.CharField(max_length=20, default='pending')  # Статус заказа
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания заказа

    def __str__(self):
        return f'Order {self.id} by {self.customer.username}'  # Строковое представление модели