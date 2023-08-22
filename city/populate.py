import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','cityjobsfakeinfo.settings')

import django
django.setup()

from jobsapp.models import *
from faker import Faker
from random import *
fake=Faker()

def phonenumbergen():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompaney=fake.company()
        ftitle=fake.random_element(elements=('Team Lead','software Engineer','Project Manager'))
        feligibility=fake.random_element(elements=('B-Tech','M-Tech','PHD'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phonenumbergen()
        hydjobs_record=Hydjobs.objects.get_or_create(date=fdate,
                                                        companey=fcompaney,
                                                        title=ftitle,
                                                        eligibility=feligibility,
                                                        address=faddress,
                                                        email=femail,
                                                        phonenumber=fphonenumber)
        chennaijobs_record=Chennaijobs.objects.get_or_create(date=fdate,
                                                        companey=fcompaney,
                                                        title=ftitle,
                                                        eligibility=feligibility,
                                                        address=faddress,
                                                        email=femail,
                                                        phonenumber=fphonenumber)
populate(30)
