import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","Pizzeria.settings")

import django

django.setup()

from pizzas.models import Pizza, Topping

pizzas1 = Pizza.objects.all()

for pizza in pizzas1:
    print(pizza.id)
    print(pizza.name)
    print(pizza.date_added)

p = Pizza.objects.get(id=1)
print(p)

toppings = p.topping_set.all()

for t in toppings:
   print(t)
   
comments = p.comment_set.all()

for c in comments:
    print(c)