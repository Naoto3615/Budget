
from django.contrib import admin
from django.urls import path
from expenses import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('expenses/', views.expense_list, name='expense_list'),
    path('add/', views.add_expense, name='add_expense'),
    path('', views.expense_list, name='expense_list'),
    path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user = True,template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # カスタムLogoutView
    path('accounts/signup/', views.signup, name='signup'),
    path('delete/<int:id>/', views.delete_expense, name='delete_expense'),  # 削除用のURL
]
