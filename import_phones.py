import csv
from django.core.management.base import BaseCommand
from phones.models import Phone

class Command(BaseCommand):
    def handle(self, *args, **options):
#         # Мы определяем новый класс Command, который наследуется от BaseCommand. 
#         # Метод handle является точкой входа для нашей пользовательской команды управления. 
#         # Он принимает два аргумента: *args и **options, которые в этом случае не используются.
        with open('phones.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
#         # Мы открываем файл phones.csv в режиме чтения ('r') и создаем объект DictReader, 
#         # который позволяет нам читать файл CSV и получать доступ к значениям в каждой строке как к словарям.
            for row in reader:
                phone, created = Phone.objects.get_or_create(
                    name=row['name'],
                    price=row['price'],
                    image=row['image'],
                    release_date=row['release_date'],
                    lte_exists=row['lte_exists'] == 'True'
                )
                if created:
                    print(f"Created phone: {phone.name}")
                else:
                    print(f"Updated phone: {phone.name}")
#                 # Мы проходим по каждой строке в файле CSV с помощью цикла for. 
#                 # Для каждой строки мы создаем или обновляем объект Phone с помощью метода get_or_create. 
#                 # Мы передаем значения из строки CSV в соответствующие поля модели Phone. Если объект создан,
#                 #  мы печатаем сообщение о создании телефона, если обновлен - о обновлении.
#                 # В целом, этот скрипт импортирует данные из файла CSV и создает или обновляет объекты Phone в базе данных.
