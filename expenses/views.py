from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense


# ? save data
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(request.GET)
        return render(request, 'expenses/add_expense.html', {'form': form})


def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses/expense_list.html', {'expenses': expenses})

