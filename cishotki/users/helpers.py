import time
from django.utils import timezone
from datetime import timedelta
from hashlib import sha256

from cishotki.settings import SECRET_KEY

def in_48_hours():
	return timezone.now() + timedelta(days=2)

def generate_confirmation_hash(user):
	return sha256(
		"{}{}{}{}{}".format(
			time.time(),
			user.first_name,
			user.last_name,
			#user.confirmation_expire_datetime,
			user.password,
			SECRET_KEY,
		).encode('utf-8')
	).hexdigest()