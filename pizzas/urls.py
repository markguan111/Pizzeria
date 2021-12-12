from django.urls import path
from django.urls.resolvers import URLPattern


from . import views

app_name = 'pizzas'

urlpatterns = [
    path('',views.index,name='index'),
    path('pizzas1',views.pizzas1,name='pizzas1'),
    path('pizzas1/<int:pizzas2_id>/',views.pizzas2,name='pizzas2'),
    path('new_comment/<int:pizzas2_id>',views.new_comment,name='new_comment'),
    
   
    
]
 



