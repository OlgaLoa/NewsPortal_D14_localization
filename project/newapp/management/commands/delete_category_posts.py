from django.core.management.base import BaseCommand, CommandError
from newapp.models import Post, Category


class Command(BaseCommand):
    help = 'Deleting all news of the selected category'  # показывает подсказку при вводе "python manage.py <ваша команда> --help"
    requires_migrations_checks = True  # напоминать ли о миграциях. Если тру — то будет напоминание о том, что не сделаны все миграции (если такие есть)

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('category', type=str) #принимаемый аргумент - выбранная категория, тип ввода категории - строка

    def handle(self, *args, **options):
        # здесь можете писать любой код, который выполнется при вызове вашей команды
        answer = input(f'Do you really want to delete all posts of the chosen category {options["category"]}? yes/no \n')

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Denied'))
            return

        try:
            category = Category.objects.get(name=options['category'])
            Post.objects.filter(postCategory = category).delete() #определяем посты выбранной категории и удаляем их (postCategory – из модели Post)
            self.stdout.write(self.style.SUCCESS(f'Succesfully deleted all news from category {category.name}'))   # в случае неправильного подтверждения говорим, что в доступе отказано
        except Post.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Could not find category {category.name}'))