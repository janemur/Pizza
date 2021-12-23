import random
import click


class Pizza:
    def __init__(self, title, size):
        self.title = title
        self.size = size

        # Добавляем каждой пицце рецепт и эмоджи
        if self.title == 'Mozzarella':
            self.recipe = {'tomato sauce': '5', 'mozzarella': '20', 'tomatoes': '8'}
            self.title += ' 🧀'
        elif title == 'Pepperoni':
            self.recipe = {'tomato sauce': '5', 'mozzarella': '20', 'pepperoni': '8'}
            self.title += ' 🍕'
        elif title == 'Hawaiian':
            self.recipe = {'tomato sauce': '5', 'mozzarella': '20', 'chicken': '4', 'pineapples':'6'}
            self.title += ' 🍍'
        else:
            print('We do not have that kind of pizza :(')

        # проверяем другие варианта ввода L и XL от клиента
        if self.size in ['large', 'big', 'usual', 'normal']:
            self.size = 'L'
        elif self.size in ['extra large', 'huge', 'i do not care']:
            self.size = 'XL'

        # исключение помогает также не отвергать значения написанные не капсом, если у нас такого размер нет,
        # выдаем сообщение об ошибке
        if self.size.upper() not in ['L', 'XL']:
            print('Currently we have only L and XL sizes. There should be a lot of good pizza')

    # Выводит рецепт пиццы
    def dict(self):
        print('recipe:' + self.title)

    def __eq__(self, other: object):
        return self.title == other.title


def cli():
    pass


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    ordered_pizza = ''
    if pizza in ['mozzarella', 'Mozzarella', 'margherita', 'Margherita']:
        ordered_pizza = pizza_Mozzarella
    elif pizza in ['pepperoni', 'Pepperoni']:
        ordered_pizza = pizza_Pepperoni
    elif pizza in ['hawaiian', 'Hawaiian']:
        ordered_pizza = pizza_Hawaiian

    # Если у нас есть пицца, которую попросил клиент, начинаем ее готовить. Если нет - выводим сообщение
    if ordered_pizza != '':
        bake(ordered_pizza)
        if delivery:
            delivery_p(ordered_pizza)
        else:
            pick(ordered_pizza)
    else:
        print('We do not have this type of pizza, but there are many others. Our personnel recommendation is Hawaiian!')


def log(text):
    """Декоратор для вывода времени приготовления/доставки/самовывоза"""
    def time_giver(function):
        def decorator(*args, **kwargs):
            function(*args, **kwargs)
            time_in_min = random.randint(5, 20)
            print(text.format(str(time_in_min)))
        return decorator
    return time_giver


@log("🍓 Приготовили за {} минут!")
def bake(pizza: Pizza) -> str:
    """Готовит пиццу"""


@log("🏠 Получено за {} минут!")
def pick(pizza: Pizza) -> str:
    """Самовывоз"""


@log('🛴 Доставили за {} минут!')
def delivery_p(pizza: Pizza) -> str:
    """Доставляет пиццу"""


@cli.command()
def menu():
    """Выводит меню"""
    print('For today our menu is:')
    for i in [pizza_Mozzarella, pizza_Pepperoni, pizza_Hawaiian]:
        ingredients = []
        for key, value in i.recipe.items():
            ingredients.append(key)
        m = map(str, ingredients)  # map function to convert each item in the list to a string
        recipe = ', '.join(m)  # join to combine those strings with ', '
        print(f'{i.title}: {recipe}')


if __name__ == '__main__':
    # Все наши пиццы
    pizza_Mozzarella = Pizza('Mozzarella', 'l')
    pizza_Pepperoni = Pizza('Pepperoni', 'l')
    pizza_Hawaiian = Pizza('Hawaiian', 'l')

    # Pizza('Mozzarella', 'l').dict()
    cli()
