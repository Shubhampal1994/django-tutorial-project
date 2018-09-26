import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

import random
from AppTwo.models import User
from faker import Faker

fakegen = Faker()


def populate(N=10):
	for entry in range(N):
		fake_fname = fakegen.first_name()
		fake_lname = fakegen.last_name()
		fake_email = fakegen.email()

		user_details = User.objects.get_or_create(
			first_name=fake_fname, last_name=fake_lname, email=fake_email
			)


if __name__ == '__main__':
	print('populating User:')
	populate(20)
	print('Populating Complete!')
