# -*- coding: utf-8 -*-
import re
from django.shortcuts import render
from landingpage.models import User
from landingpage.forms import EmailForm, FileForm

def parse_and_save(data):
  '''Parse le fichier uploade et stocke les adresses
  email valides dans la base de donnees'''
  pattern = r"([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`" \
             "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|" \
             "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"
  mails = re.findall(pattern, data)
  ret = []
  for mail in mails:
    if (User.objects.filter(email=mail[0])):
      pass
    else:
      ret.extend([mail[0]])
      User(email=mail[0]).save()
  return ret

def home(request):
  '''Page d'accueil'''
  done = False
  done2 = False
  empty = False
  form = EmailForm()
  form2 = FileForm()
  if request.method == 'POST':
    form = EmailForm(request.POST)
    if form.is_valid():
      if (User.objects.filter(email=form.cleaned_data['email'])):
        form = 'Cette adresse existe deja dans la base de donnees'
      else:
        User(email=form.cleaned_data['email']).save();
        form = 'Merci pour votre inscription'
      done = True
    else:
      form = EmailForm()
    form2 = FileForm(request.POST, request.FILES)
    if form2.is_valid():
      done2 = True
      form2 = parse_and_save(request.FILES['fd'].read())
      if (not form2):
        empty = True
    else:
      form2 = FileForm()
  return render(request, 'base.html', locals())

def huit(request):
  '''Bonux'''
  done = False
  done2 = False
  empty = False
  form = EmailForm()
  form2 = FileForm()
  if request.method == 'POST':
    form = EmailForm(request.POST)
    if form.is_valid():
      if (User.objects.filter(email=form.cleaned_data['email'])):
        form = 'Cette adresse existe deja dans la base de donnees'
      else:
        User(email=form.cleaned_data['email']).save();
        form = 'Merci pour votre inscription'
      done = True
    else:
      form = EmailForm()
    form2 = FileForm(request.POST, request.FILES)
    if form2.is_valid():
      done2 = True
      form2 = parse_and_save(request.FILES['fd'].read())
      if (not form2):
        empty = True
    else:
      form2 = FileForm()
  return render(request, '8b.html', locals())
