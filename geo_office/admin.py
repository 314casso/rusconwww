from django.contrib import admin
from geo_office.models import OfficeContact, Office, Country, Town, OfficeType,\
    ContactType, ContactLabel
from modeltranslation.admin import TranslationAdmin

class ModelTranslationMedia(object):    
    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',           
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        } 

class ContactInline(admin.TabularInline):
    model = OfficeContact

class OfficeAdmin(TranslationAdmin, ModelTranslationMedia):    
    list_display = ('town',) 
    inlines = [ContactInline,]    

class TransAdmin(TranslationAdmin, ModelTranslationMedia):
    pass

admin.site.register(Office,OfficeAdmin)
admin.site.register(Country,TransAdmin)
admin.site.register(Town,TransAdmin)
admin.site.register(OfficeType,TransAdmin)
admin.site.register(ContactType,TransAdmin)
admin.site.register(ContactLabel,TransAdmin)