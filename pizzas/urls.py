from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

app_name = 'pizzas'

urlpatterns = [
<<<<<<< HEAD
    path('',views.index,name='index'),
    path('pizzas1',views.pizzas1,name='pizzas1'),
    path('pizzas1/<int:pizzas2_id>/',views.pizzas2,name='pizzas2'),
    path('new_comment/<int:pizzas2_id>',views.new_comment,name='new_comment'),
    
    
    
]
=======
    path('', views.index, name='index'),
    path('pizzas1', views.pizzas1, name='pizzas1'),
    path('pizzas1/<int:pizzas2_id>/', views.pizzas2, name='pizzas2'),
    path('pizzas1/<int:pizzas3_id>/', views.pizzas3, name='pizzas3'),
    # path('pizzas3/',views.pizzas3,name='pizzas3'),

>>>>>>> 343473556b38c6ba822f03dcc8f683ded4a38821


]
