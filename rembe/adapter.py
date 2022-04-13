from allauth.account.adapter import DefaultAccountAdapter
from django.forms import ValidationError

class RestrictEmailAdapter(DefaultAccountAdapter):
	def clean_email(self, email):
		if not (email.endswith("@ciencias.unam.mx")):
			raise ValidationError('No puedes registrarte con ese dominio.\
												Por favor usa un correo @ciencias.unam.mx')
		return email
