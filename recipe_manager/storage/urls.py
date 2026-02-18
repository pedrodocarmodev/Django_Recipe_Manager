from django.urls import path
from .views import StorageView, AddItemView, EditItemView, DeleteItemView

urlpatterns = [
    path('', StorageView.as_view(), name="storage"),
    path('add-item/', AddItemView, name="add_item"),
    path('edit-item/<int:id>/', EditItemView, name="edit_item"),
    path('delete-item/<int:id>/', DeleteItemView, name="delete_item")
]