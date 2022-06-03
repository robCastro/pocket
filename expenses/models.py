from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=50)
    limit = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name


class Expense(models.Model):

    comment = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_registered = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Gasto"
        verbose_name_plural = "Gastos"

    def __str__(self):
        return f'{self.category} - {self.amount} - {self.date:%d/%m/%Y}'