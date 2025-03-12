from homework.test_shop import product


class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        return self.quantity >= quantity
        # self.quantity = quantity
        # needProduct = None
        # if self.quantity >= needProduct:
        #     needProduct = True
        # else:
        #     needProduct = False

        # raise NotImplementedError

    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if self.check_quantity(quantity):
            self.quantity -= quantity
        else:
            raise ValueError("Продуктов не хватает")



        # raise NotImplementedError

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if product in product:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count


        # self.products += buy_count

        # raise NotImplementedError

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        -Если remove_count не передан, то удаляется вся позиция
        -Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if product in self.products:
            if remove_count is None or self.products <= remove_count:
                del self.products[product]
        else:
            self.products[product] -= remove_count


        # self.products -= remove_count


        # raise NotImplementedError

    def clear(self):
        # ?
        raise NotImplementedError

    def get_total_price(self) -> float:
        total = 0
        for product, count in self.products.items():
            total += product.price * count
        return total

        # raise NotImplementedError

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """

        for product, thing in self.products.items():
            if product.quantity < thing:
                raise ValueError("Товаров не хватает на складе")
            else:
                product.buy(thing)


        # if self.add_product():
        #     self.products -= product()
        # else:
        #     raise ValueError("Товаров не хватает на складе")

        # raise NotImplementedError
