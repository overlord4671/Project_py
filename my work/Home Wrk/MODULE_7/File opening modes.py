class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name},{self.weight} кг,{self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'product.txt'

    def get_products(self):
        in_file = open(self.__file_name, 'r')
        read_file = in_file.read()
        in_file.close()
        return read_file

    def add(self, *products):

        products_in_file = open(self.__file_name, 'r')
        product_names = []
        for line in products_in_file:
            product_name = line.split(', ')[0]
            product_names.append(product_name)
        products_in_file.close()

        for product in products:
            if product.name not in product_names:
                out_file = open(self.__file_name, 'a')
                out_file.write(f'{product.name}, {product.weight}, {product.category}\n')
                out_file.close()
            else:
                print(f'Продукт "{product.name}" уже есть в магазине!')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
