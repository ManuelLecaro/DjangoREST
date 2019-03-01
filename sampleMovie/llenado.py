from django_seed import Seed
import random

import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sampleMovie.settings")
django.setup()

seeder = Seed.seeder()

from movies.models import TipoPlan,Plan,Persona,Peliculas,Log,RatingPeliculas
seeder.add_entity(TipoPlan, 5)
seeder.add_entity(Plan,40)
seeder.add_entity(Persona,40)
seeder.add_entity(Peliculas,40)
seeder.add_entity(Log,40)
seeder.add_entity(RatingPeliculas,90)

inserted_pks = seeder.execute()

seeder.add_entity(TipoPlan, 50, {
    'nombre': lambda x: seeder.faker.word(),
    'costo': lambda x: random.randint(1,10000),
})

seeder.add_entity(Persona, 40, {
    'nombre': lambda x: seeder.faker.name(),
    'apellido': lambda x: seeder.faker.name(),
    'fecha': lambda x: seeder.faker.date(),
})

seeder.add_entity(Peliculas, 40, {
    'titulo': lambda x: seeder.faker.word(),
    'director': lambda x: seeder.faker.name(),
    'calificacion': lambda x: random.randint(1,5),
    'reparto' : lambda x: seeder.faker.word(),
})

seeder.add_entity(RatingPeliculas, 90, {
	'cali': lambda x: random.randint(1,5),
})


seeder.execute()
