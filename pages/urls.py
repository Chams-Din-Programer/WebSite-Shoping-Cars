from django.urls import path
from . import views


urlpatterns =[
    path('',views.Index, name='Index'),
    path('car/<str:car>',views.car, name='car'),
    path('model/<str:make>',views.model, name='model'),
    path('models',views.models, name='models'),
    path('search',views.search, name='search'),

    path('logout/', views.logout, name='logout'),
]