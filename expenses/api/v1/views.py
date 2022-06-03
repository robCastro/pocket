from rest_framework import viewsets

from expenses.api.v1.serializers import CategorySerializer, ExpenseSerializer
from expenses.models import Category, Expense

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all().order_by('-date')
    serializer_class = ExpenseSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer