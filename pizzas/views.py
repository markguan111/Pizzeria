from django.shortcuts import redirect, render



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

'''
def comment(request,pizzas2_id):
    pizzas2 = Pizza.objects.get(id=pizzas2_id)

    comments = pizzas2.Comment_set.all()

    context = {'pizzas2': pizzas2, 'comments':comments}

    return render(request,'pizzas/pizzas2.html',context)

def pizzas3(request):
      if request.method != 'POST' :
          form = commentform()
      
      else:
          form = commentform(data=request.POST)
          if form.is_valid():
              form.save()

              return redirect('pizzas:pizzas1')
      
      context = {'form': form }
      return render(request,'pizzas/pizzas3.html',context)
      '''


           
