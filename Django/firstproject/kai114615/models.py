from django.db import models, connection

# Create your models here.
class Sakila:
    def countries():
        with connection.cursor() as cursor:
            cursor.execute('select country_id, country from country')
            countries = cursor.fetchall()
            return countries