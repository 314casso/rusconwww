from modeltranslation.translator import TranslationOptions, translator
from geo_office.models import Country, Town, OfficeType, Office, ContactType,\
    ContactLabel

class NameTranslationOptions(TranslationOptions):
    fields = ('name',) 
 
class OfficeTranslationOptions(TranslationOptions):
    fields = ('head', 'address', 'seo_title')
 
class ContactTypeTranslationOptions(TranslationOptions):
    fields = ('contact_type', 'contact_short_type', )

class OfficeTypeTranslationOptions(TranslationOptions):
    fields = ('name', 'head_title_template', 'office_title_template') 
    
class ContactLabelTranslationOptions(TranslationOptions):
    fields = ('label',)    
 
translator.register(Country, NameTranslationOptions)
translator.register(Town, NameTranslationOptions)
translator.register(OfficeType, OfficeTypeTranslationOptions)
translator.register(Office, OfficeTranslationOptions)
translator.register(ContactType, ContactTypeTranslationOptions)
translator.register(ContactLabel, ContactLabelTranslationOptions)

