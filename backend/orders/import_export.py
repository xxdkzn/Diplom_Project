import yaml
from .models import Product, Supplier


def import_products_from_yaml(file_path):
    """
    Импортирует товары из YAML файла в базу данных.

    :param file_path: Путь к YAML файлу с данными о товарах.
    """
    with open(file_path, 'r') as file:
        products = yaml.safe_load(file)  # Загружаем данные из файла
        for product in products:
            # Получаем или создаем поставщика
            supplier, created = Supplier.objects.get_or_create(name=product['supplier'])
            # Создаем товар
            Product.objects.create(
                name=product['name'],
                price=product['price'],
                supplier=supplier
            )