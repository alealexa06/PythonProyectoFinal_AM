from django.urls import path
from . import views

urlpatterns = [
    path('', views.InboxView.as_view(), name='inbox'),
    path('send/', views.SendMessageView.as_view(), name='send_message'),
    path('<int:pk>/', views.MessageDetailView.as_view(), name='message_detail'),
]
