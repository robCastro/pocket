from datetime import timedelta
import random

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django.db import transaction

from expenses.models import Category, Expense

class Command(BaseCommand):
    help = 'Genera las categorias'

    CATEGORIES = [
        Category(id=1,name='Gasolina', limit=80.0),
        Category(id=2,name='Comida', limit=120.0),
        Category(id=3,name='Dieta', limit=50.0),
        Category(id=4,name='Gimnasio', limit=10.0),
    ]

    def add_arguments(self, parser):
        parser.add_argument(
            '--categories',
            action='store_true',
            help='Seed default categories',
        )
        parser.add_argument(
            '--expenses',
            help='How many expenses to generate',
            type=int,
            default=500,
        )
        parser.add_argument(
            '--months',
            help='How many months back the expenses should go',
            type=int,
            default=6,
        )
        
    @transaction.atomic
    def handle(self, *args, **options):
        if options['categories']:
            self._seed_categories()
        count = options.get('expenses')
        months = options.get('months')
        print(count, months)
        self._seed_expenses(count, months)

    def _seed_categories(self):
        if Category.objects.all().exists():
            raise CommandError('Hay categorias existentes, no se puede hacer seed.')
        Category.objects.bulk_create(self.CATEGORIES)
        print('Categories seeded')

    def _seed_expenses(self, count, months):
        expenses = []
        categories = list(Category.objects.all())
        max_days_back = months*30
        for i in range(count):
            date = timezone.now() - timedelta(days=random.randint(0, max_days_back))
            expense = Expense(
                comment=f'Random expense number {i}',
                amount=(random.random()*100 + 5),
                date=date,
                date_registered=date,
                category=random.choice(categories),
            )
            expenses.append(expense)
        Expense.objects.bulk_create(expenses)
        print(f'{count} expenses seeded as far as {months} back')