# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin

class User(models.Model):
  uid = models.AutoField(primary_key=True)
  email = models.CharField(max_length=255, unique=True)

  def __unicode__(self):
    return u'%s' % self.email

admin.site.register(User)
