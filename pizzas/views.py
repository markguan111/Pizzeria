from django.shortcuts import render

from .models import Pizza

# Create your views here.
def index(request):
    return render(request,'pizzas/index.html')

def pizzas1(request):
  pizzas1 = Pizza.objects.order_by('date_added')
  
  context = {'pizzas1': pizzas1}

  return render(request,'pizzas/pizzas1.html',context)

def pizzas2(request,pizzas2_id):
    pizzas2 = Pizza.objects.get(id=pizzas2_id)

    toppings = pizzas2.topping_set.all()

    context = {'pizzas2': pizzas2, 'toppings':toppings}

    return render(request,'pizzas/pizzas2.html',context)
