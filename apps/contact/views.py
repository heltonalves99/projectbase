# -*- coding: utf-8 -*-
from django.views.generic.edit import CreateView

from .models import Contact

class ContactCreateView(CreateView):
    model = Contact
    success_url = '/contact/success/'
