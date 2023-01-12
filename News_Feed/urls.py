from django.urls import path
from . import views
from .views import MainListView ,ListPageView,PostFormCreate,RegisterView

app_name = "News_Feed"

urlpatterns = [
    path('list/',MainListView.as_view(),name = "main"),
    path('list/<int:pk>',ListPageView.as_view(),name = "detail"),
    path('list/create_post/',PostFormCreate.as_view(),name = "create"),
    path('accounts/register/',RegisterView.as_view(),name = "register")
]