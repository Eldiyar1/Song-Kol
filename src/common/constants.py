from django.utils.translation import gettext_lazy as _

CATEGORY_CHOICES = (
    ('Новости', _('Новости')),
    ('Блог', _('Блог')),
)

STATUS_CHOICES = (
    ('Доступно', _('Доступно')),
    ('Не доступно', _('Не доступно')),
)

HORSE_TOUR = '1'
WALK_TOUR = '2'
JEEP_TOUR = '3'
WINTER_TOUR = '4'
TYPE_CHOICES = (
    (HORSE_TOUR, 'Конный тур'),
    (WALK_TOUR, 'Пеший тур'),
    (JEEP_TOUR, 'Джип тур'),
    (WINTER_TOUR, 'Зимний тур'),
)

LOCATION = '1'
FOOD = '2'
SLEEP = '3'
LOCATION_CHOICE = (
    (LOCATION, 'Место'),
    (FOOD, 'Питание'),
    (SLEEP, 'Ночлег'),
)

WALK = '1'
HORSE = '2'
CAR = '3'
TRANSPORT_CHOICES = (
    (WALK, 'Пешком'),
    (HORSE, 'Лошадь'),
    (CAR, 'Машина'),
)

TYPE_OF_TRANSPORT = (
    ('car', 'car'),
    ('horse', 'horse'),
    ('on foot', 'on foot'),
    ('Пешком', 'Пешком'),
    ('На машине', 'На машине'),
    ('Верхом', 'Верхом'),
)
