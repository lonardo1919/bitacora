from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='view00'),
    path('insertView', views.insert_habitat_view, name='view01'),
    path('listView', views.list_habitat_view, name='view02'),
    path('deleteView/<int:id>', views.delete_habitat_view, name='view03'),
    path('updateView/<int:id>', views.update_habitat_view, name='view04')
]

