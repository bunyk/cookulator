# coding=utf-8
from __future__ import unicode_literals
from __future__ import print_function

class Product(object):
    bar_code=None
    name=None 
    producer=None
    country=None # ISO code

    price=None # UAH
    amount=None # g
    
    proteins=None # g per 100g
    carbohydrates=None # g per 100g
    fats=None # g per 100g
    energy=None # joules
    opening_shelf_life=None # hours

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def clone(self):
        return Product(self.__dict__)

    def __mul__(self, scalar):
        res = self.clone()
        res.amount *= scalar
        res.price *= scalar
        return res
    
    def __add__(self, other):
        res = Product()
        res.amount = self.amount + other.amount
        res.price = self.price + other.price
        res.name = self.name + ' і ' + other.name

        res.opening_shelf_life = min(
            self.opening_shelf_life,
            other.opening_shelf_life
        )

        def new_value(name):
            a = getattr(self, name) * self.amount
            b = getattr(other, name) * other.amount
            return (a + b) / self.amount

        res.proteins = new_value('proteins')
        res.carbohydrates = new_value('carbohydrates')
        res.fats = new_value('fats')
        res.energy = new_value('energy')

        return res

    def __str__(self):
        res = []
        res.append(self.name)
        res.append('Ціна: %.2f грн. Вихід: %.0f грам' % (self.price, self.amount))
        res.append('Енергетична цінність в 100 г продукту: %.1f кДж' % (self.energy / 1000.0))
        res.append('білки - %.2f г, жири - %.2f г, вуглеводи %.2f г. ' % (
                self.proteins, self.fats, self.carbohydrates
        ))
        res.append('Після відкриття зберігати не більше ніж: %s год' % self.opening_shelf_life)
        return '\n'.join(res)
        

кукурудза = Product(
    bar_code=4824024004211,
    name='Кукурудза ніжна вакуумована стерилізована',
    producer='Бондюель',
    country='HU', 

    price=12.49,
    amount=340, # g
    
    # g per 100g:
    proteins=3.1,
    carbohydrates=21.8,
    fats=1.6,
    energy=505000, # joules

    opening_shelf_life=48, # hours
)

тунець = Product(
    bar_code=4824024002439,
    name='Консерви рибні. Тунець подрібнений стерилізований.',
    producer='Chotiwat manufacturing',
    country='TH', 

    price=19.99,
    amount=130, # g

    # per 100g:
    proteins=22.06,
    carbohydrates=0.07,
    fats=1.4,
    energy=442000, # joules

    opening_shelf_life=48, # hours
)

print(кукурудза + тунець)
