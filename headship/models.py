# -*- coding: utf-8 -*-
from django.db import models
from filer.fields.image import FilerImageField
from django.utils.translation import ugettext_lazy as _


class Headship(models.Model):    
    GENDER_CHOICES = (('F', _('Female')), ('M', _('Male')),)
    last_name = models.CharField(_('LastName'), max_length=100,) # Фамилия
    first_name = models.CharField(_('FirstName'), max_length=100,) # Имя
    patronymic = models.CharField(_('Patronymic'), max_length=100, blank=True, null=True) # Отчество    
    gender = models.CharField(_('Gender'), max_length=1, choices=GENDER_CHOICES, default='M')
    post = models.CharField(_('Position'), max_length=255)  
    email = models.EmailField(_('Email')) 
    phone = models.CharField(_('Phone'), max_length=100, blank=True, null=True)
    image = FilerImageField(blank=True, null=True)
    active = models.BooleanField(_('Active'), default=False)
    sort_order = models.IntegerField(_('Sort'), default=0)
    subpost = models.CharField(_('Sub position'), max_length=255, blank=True, null=True)
    biopic = models.TextField(_('Biopic'), blank=True, null=True)
    show_biopic = models.BooleanField(_('Show biopic'), default=False)
    
    def extraclass(self):
        if self.show_biopic:
            return 'custom-modal-trigger'
    
    def __unicode__(self):
        return u'%s %s %s' % (self.first_name, self.patronymic ,self.last_name)
    
    class Meta:
        ordering = ['sort_order']