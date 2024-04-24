import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()


## FAKE POPULATER SCRIPT
import random
from first_app.models import Topic, AccessRecord, Webpage
from faker import Faker

fakegen = Faker()
topics = [
    'Search',
    'Marketplace',
    'News',
    'Social',
    'Blog',
]

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for item in range(N):

        #get the topic for entry
        top = add_topic()

        # create fake data of webpage for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.name()

        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # create fake access record
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print('Populating scripts!')
    populate(10)
    print('Population completed!')