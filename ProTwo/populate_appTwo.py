import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

# Populate fake script from faker library
import random
from appTwo.models import Users
from faker import Faker

fakegen = Faker()



def populate(N=10):
    for item in range(N):

        #create dummy users from fake library
        fake_fname = fakegen.first_name()
        fake_lname = fakegen.last_name()
        fake_email = fakegen.email()

        user_gen = Users.objects.get_or_create(
                            user_fname=fake_fname, 
                            user_lname=fake_lname, 
                            user_email=fake_email)[0]

if __name__ == '__main__':
    print("Populating script for user generation!")
    populate(20)
    print('Population Completed!')
        