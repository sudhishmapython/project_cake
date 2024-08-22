from . import views,supplier_views,user_views,admin_views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('owner_registration',views.owner_registration,name='owner_registration'),
    path('user_registration',views.user_registration,name='user_registration'),
    path('login_view/', views.login_view, name='login_view'),
    path('logout_view', views.logout_view, name='logout_view'),

    path('admin_page', admin_views.admin_page, name='admin_page'),
    path('cat_add', admin_views.add_catogory, name='add_catogory'),
    path('cat_view',admin_views.cat_view,name='cat_view'),
    path('cat_update/<int:id>', admin_views.cat_update, name='cat_update'),
    path('cat_delete/<int:id>', admin_views.cat_delete, name='cat_delete'),
    path('cake_add', admin_views.cake_add, name='cake_add'),
    path('cake_view',admin_views.cake_view,name='cake_view'),
    path('cake_update/<int:id>', admin_views.cake_update, name='cake_update'),
    path('cake_delete/<int:id>', admin_views.cake_delete, name='cake_delete'),


    path('supplier_page', supplier_views.supplier_page, name='supplier_page'),



    path('user_page', user_views.user_page, name='user_page'),
    path('user_cake_view',user_views.user_cake_view,name='user_cake_view'),
    path('add_cart/<int:product_id>', user_views.add_to_cart,name='add_cart'),
    path('cart/', user_views.view_cart, name='view_cart'),
    path('remove/<int:item_id>/', user_views.remove_from_cart, name='remove_from_cart'),

]