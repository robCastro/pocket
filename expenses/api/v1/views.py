from datetime import datetime

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Sum, Q, DecimalField
from django.db.models.functions import Coalesce

from expenses.api.v1.serializers import CategorySerializer, CategoryWithExpensesSerializer, ExpenseSerializer
from expenses.models import Category, Expense


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all().select_related('category').order_by('-date')
    serializer_class = ExpenseSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=False)
    def overview(self, request):
        queryset = self.get_queryset()
        start_date = datetime.now().replace(day=1)
        coalesce_query = Coalesce(Sum('expenses__amount', filter=Q(expenses__date__date__gte=start_date)), 0.0, output_field=DecimalField())
        queryset = queryset.annotate(expended=coalesce_query)
        categories_serializer = CategoryWithExpensesSerializer(instance=queryset, many=True).data
        return Response(categories_serializer, 200)
    