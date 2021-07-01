from django.urls import path
from django.contrib import admin
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('account-list/', views.accountList, name='account-list'),
    path('account-detail/<str:username>/', views.accountDetail, name='account-detail'),
    path('account-create/', views.accountCreate, name='account-create'),
    path('account-update/<str:username>/', views.accountUpdate, name='account-update'),
    path('account-delete/<str:username>/', views.accountDelete, name='account-delete'),
]









from rest_framework.routers import DefaultRouter

# from .views import ListTodo, DetailTodo
# from .views import TodoViewSet
# urlpatterns = [
#     path('', ListTodo.as_view()),
#     path('<int:pk>/', DetailTodo.as_view()),
# ]
#
# router = DefaultRouter()
# router.register('', TodoViewSet, basename='todos')
# urlpatterns = router.urls