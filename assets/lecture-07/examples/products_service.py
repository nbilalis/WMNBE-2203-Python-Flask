from random import randint, choice, sample
from inspect import cleandoc


def get_products(q) -> list:
    ret = [get_product(f'{i:04}') for i in range(1, 101)]
    return list(filter(lambda p: p['title'].lower().find(q.lower()) > -1, ret))


def get_product(id):
    if int(id) not in range(1, 101):
        return None

    adjectives = ('Super', 'Awesome', 'Unique', 'Gorgeous',
                  'Floral', 'Casual', 'Standard', 'Formal')
    items = ('Shirt', 'T-Shirt', 'Pants', 'Dress',
             'Blouse', 'Jeans', 'Trousers')
    sizes = ('XS', 'S', 'M', 'L', 'XL')
    colors = ('green', 'yellow', 'pink', 'black', 'white')

    description = cleandoc(
        '''Lorem ipsum dolor sit amet, consectetur adipisicing elit.
        Numquam accusamus facere iusto,
        autem soluta amet sapiente ratione inventore nesciunt a,
        maxime quasi consectetur, rerum illum.'''
    ).replace('\n', '')

    is_sale = choice((True, False, False))
    is_sold_out = not is_sale and choice((True, False, False))
    is_hot = not is_sale and not is_sold_out and choice((True, False, False))

    return {
        'id': id,
        'title': f'{choice(adjectives)} {choice(items)}',
        'description': description,
        'long_description': ' '.join([description for i in range(10)]),
        'price': randint(1000, 9999) / 100,
        'discount_ratio': randint(0, 99) / 100 if is_sale else 0,
        'stock': randint(0, 100),
        'sizes': sample(sizes, randint(1, len(sizes))),
        'colors': sample(colors, randint(1, len(colors))),
        'is_sale': is_sale,
        'is_sold_out': is_sold_out,
        'is_hot': is_hot,
    }
