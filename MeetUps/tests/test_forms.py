from .forms import RegistrationForm
from .models import*


def test_valid_form(self):
    email = RegistrationForm(email='nknvic00#@myuct.ac.za')
    participant=Participant.objects.get_or_create(email=email)


    # data ="victor.nkuna@yahoo.com"

    form = RegistrationForm(data=email)

    self.asserFalse(form.is_valid())