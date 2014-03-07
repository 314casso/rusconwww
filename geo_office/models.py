from django.db import models
from filer.fields.image import FilerImageField
from orderedmodel.models import OrderedModel
from cms.models.pluginmodel import CMSPlugin

class Country(models.Model):
    name = models.CharField(max_length=255)
    image = FilerImageField()
    def __unicode__(self):
        return self.name

class Town(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country)
    def __unicode__(self):
        return self.name        

class OfficeType(models.Model):
    name = models.CharField(max_length=255)
    head_title_template = models.CharField(max_length=255)
    office_title_template = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name
                            
class Office(models.Model):    
    office_type = models.ForeignKey(OfficeType)
    town = models.ForeignKey(Town)
    head = models.CharField(max_length=255)
    address = models.TextField()
    post_index = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    seo_title = models.CharField(max_length=255, default=u'Transportation logistics in')        
    @property
    def prime_phone(self):
        return self.get_prime_contact(ContactType.PHONE)       
        
    @property
    def prime_email(self):
        return self.get_prime_contact(ContactType.EMAIL)
        
    def get_prime_contact(self, contact_type_id):
        contacts = self.contacts.filter(contact_type_id=contact_type_id)
        contact = contacts[:1]
        if contact:
            return contacts[:1].get()
            
    @property
    def prime_contacts(self):
        contacts = self.contacts.all()
        return contacts[:2]
    @property
    def get_lat_lng(self):
        if self.latitude and self.longitude:
            return (self.latitude, self.longitude)
    @property
    def head_title(self):
        return u'<strong>%s</strong>: %s' % (self.office_type.head_title_template, self.head)      
    @property
    def office_title(self):
        return self.office_type.office_title_template % self.town

class ContactType(models.Model):
    PHONE = 1
    EMAIL = 3
    contact_type =  models.CharField(max_length=50)
    contact_short_type =  models.CharField(max_length=10)
    def __unicode__(self):
        return self.contact_short_type    

class OfficeContact(OrderedModel):
    office = models.ForeignKey(Office, related_name='contacts')
    contact_type = models.ForeignKey(ContactType)
    contact = models.CharField(max_length=100)
    def __unicode__(self):
        return '%s: %s' % (self.contact_type.contact_short_type, self.contact)

PLUGIN_TEMPLATES = (
  ('geo_office/list.html', 'List'),
  ('geo_office/prime_phone.html', 'Prime phone'),
  ('geo_office/detail.html', 'Detail'),
)

class OfficeCMSPlugin(CMSPlugin):
    ids = models.CharField(max_length=255, null=True, blank=True)
    template = models.CharField('Template', max_length=255, choices = PLUGIN_TEMPLATES)


    