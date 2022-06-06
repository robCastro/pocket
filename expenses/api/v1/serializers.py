from rest_framework import serializers


from expenses import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'name', 'limit']


class ExpenseSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = models.Expense
        fields = ['id', 'comment', 'amount', 'date', 'category']
