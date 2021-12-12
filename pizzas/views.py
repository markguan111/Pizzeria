from django.shortcuts import redirect, render

from .forms import CommentForm

from .models import Comment, Pizza,Image

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
    comment = pizzas2.comment_set.all()
    image  = Image.objects.get(pizza=pizzas2)
    print(image)
    context = {'pizzas2':pizzas2, 'toppings':toppings, 'comment':comment,'image':image}

    return render(request,'pizzas/pizzas2.html',context)



def new_comment(request, pizzas2_id):
    pizzas2 = Pizza.objects.get(id=pizzas2_id)
    if request.method != 'POST' :
          form = CommentForm()
      
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizzas2 = pizzas2
            new_comment.save()
            return redirect('pizzas:pizzas2', pizzas2_id=pizzas2_id)
      
    context = {'form':form ,'pizzas2':pizzas2}
    return render(request,'pizzas/new_comment.html',context)
      


           
