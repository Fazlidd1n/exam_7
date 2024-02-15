from django.urls import path

from apps.views import UserListView, UserDeleteView, UserUpdateView

urlpatterns = [
    path('', UserListView.as_view(), name='index'),
    path('delete-user/<int:pk>', UserDeleteView.as_view(), name='delete_user'),
    path('update-user/<int:pk>', UserUpdateView.as_view(), name='update_user'),
]
