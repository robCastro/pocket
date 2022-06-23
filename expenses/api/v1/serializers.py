from rest_framework import serializers


from expenses import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'name', 'limit']


class ExpenseSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=models.Category.objects.all(), source='category')

    class Meta:
        model = models.Expense
        fields = ['id', 'comment', 'amount', 'date', 'category', 'category_id']

