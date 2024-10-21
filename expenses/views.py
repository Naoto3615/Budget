from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import SignUpForm
from django.db.models import Sum


def home(request):
    return render(request, 'expenses/expense_list.html')
# ? save data

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user  # 現在ログインしているユーザーを設定
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()

    return render(request, 'expenses/add_expense.html', {'form': form})


@login_required(login_url='/accounts/login/')
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    category_totals = expenses.values('category__name').annotate(total=Sum('amount'))
    print(category_totals)
    return render(request, 'expenses/expense_list.html', {'expenses': expenses, 'category_totals': category_totals})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('expense_list')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

