# -*- coding: utf-8 -*-
from django import forms

class EmailForm(forms.Form):
  email = forms.EmailField(label='Email ')

class FileForm(forms.Form):
  fd = forms.FileField(label='')
