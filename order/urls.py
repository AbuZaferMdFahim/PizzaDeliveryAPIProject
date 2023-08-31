from django.urls import path
from . import views

urlpatterns=[
     path('',views.OrderCreateListView.as_view(),name="order"),
     path('<int:order_id>/',views.OrderDetailView.as_view(),name="order_detail"),
     path('update-status/<int:order_id>/',views.UpdateOrderStatusView.as_view(),name="update_order_status"),
     path('user/<int:user_id>/order/',views.UserOrderView.as_view(),name="user_order"),
     path('user/<int:user_id>/order/<int:order_id>/',views.UserOrderDetailView.as_view(),name="user_specific_detail"),
]