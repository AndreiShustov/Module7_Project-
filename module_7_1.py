# Домашнее задание по теме "Режимы открытия файлов"
# Цель: закрепить знания о работе с файлами (чтение/запись) решив задачу.

# Задача "Учёт товаров":
#
# Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл с продуктами.
#
# Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables')
# и обладать следующими свойствами:
#
# Атрибут name - название продукта (строка).
# Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
# Атрибут category - категория товара (строка).
# Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'.
# Все данные в строке разделены запятой с пробелами.
#
# Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
#
# Инкапсулированный атрибут __file_name = 'products.txt'.
# Метод get_products(self), который считывает всю информацию из файла __file_name,
# закрывает его и возвращает единую строку со всеми товарами из файла __file_name.
# Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
# Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
# Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине'.
#
# Пример результата выполнения программы:
#
# s1 = Shop()
# p1 = Product('Potato', 50.5, 'Vegetables')
# p2 = Product('Spaghetti', 3.4, 'Groceries')
# p3 = Product('Potato', 5.5, 'Vegetables')

# print(p2) # __str__
#
# s1.add(p1, p2, p3)
#
# print(s1.get_products())
#
# Вывод на консоль:
#
# Первый запуск:
#
# Spaghetti, 3.4, Groceries
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Potato, 5.5, Vegetables
#
# Второй запуск:
#
# Spaghetti, 3.4, Groceries
# Продукт Potato уже есть в магазине
# Продукт Spaghetti уже есть в магазине
# Продукт Potato уже есть в магазине
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Potato, 5.5, Vegetables
#
# Примечания:
#
# Не забывайте при записи в файл добавлять спец. символ перехода на следующую строку в конце - '\n'.
# При проверке на существование товара в методе add можно вызывать метод get_products для получения текущих продуктов.
# Не забывайте закрывать файл вызывая метод close() у объектов файла.

class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        file_str = file.read()
        file.close()
        return file_str

    def add(self, *products: Product):
        file_str = self.get_products()
        for product in products:
            if product.name in file_str:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(str(product) + '\n')
                file.close()


# Пример результата выполнения программы:

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
