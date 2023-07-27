from django.urls import path
from . import views
urlpatterns = [
    path('',views.addshow,name="addshow"),
    path('update/<int:id>/',views.update,name="update"),
    path('delete/<int:id>/',views.delete_data,name="delete")
   
]
