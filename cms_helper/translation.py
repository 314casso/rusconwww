from modeltranslation.translator import translator, TranslationOptions
from zinnia import models as zinnia_models
from cms_helper.models import ClockTown, Params
from sitetree.models import TreeItem 

 
class ZinniaEntryTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'excerpt')
 
class ZinniaCategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class ClockTownTranslationOptions(TranslationOptions):
    fields = ('town',)
 
class SiteTreeTranslationOptions(TranslationOptions):
    fields = ('title', 'hint') 
 
class ParamsTranslationOptions(TranslationOptions):
    fields = ('value',) 

 
translator.register(zinnia_models.Entry, ZinniaEntryTranslationOptions)
translator.register(zinnia_models.Category, ZinniaCategoryTranslationOptions)
translator.register(ClockTown, ClockTownTranslationOptions)
translator.register(TreeItem, SiteTreeTranslationOptions)
translator.register(Params, ParamsTranslationOptions)
