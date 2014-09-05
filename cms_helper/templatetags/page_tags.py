# -*- coding: utf-8 -*-
from django import template
from cms_helper.models import ClockTown, MenuImage
import datetime
from cms.models.pagemodel import Page
from sitetree.models import TreeItem
from django.template import loader
from django.template.context import Context
import re
import base64

register = template.Library()

@register.inclusion_tag('tags/clock.html')
def clocks(limit):        
    clocks = ClockTown.objects.all()[:limit]
    if clocks:
        return {'clocks': clocks}
    
@register.filter()
def get_page_reverce_id(value):        
    mapper = {2:'company',3:'company', 4:'logistic', 5: 'logistic', 6:'logistic', 7:'logistic', 8:'logistic', 9:'carier'}    
    try:    
        return mapper[value]
    except KeyError:
        return 'company'
    
@register.filter()
def get_page_reverce_id_form_entry(value):
    categories = value.categories.all()[:1]
    if categories:
        return get_page_reverce_id(categories[0].id)
    
@register.simple_tag
def get_copyright():
    return u'© 1997—%s' % datetime.datetime.now().year

@register.filter()
def get_root_page_reverse_id(value):
    page = Page.objects.get(reverse_id=value)
    return page.get_root().reverse_id

@register.simple_tag()
def get_menuitem(alias, template_name):
    t = loader.get_template(template_name)
    item = TreeItem.objects.get(alias=alias)  
    return t.render(Context({
        'menu_item': item,        
        'parent_item': item.parent
    }))
    
@register.simple_tag
def get_image_by_menu(item_id):    
    menu_image = MenuImage.objects.get(menu_item_id=item_id)    
    return menu_image.image.url    

@register.filter()
def human_lang(lang):
    mapper = {'en': u'English', 'ru': u'По-русски'}
    return mapper[lang]

@register.filter()
def email(content):
    template = '<span class="mailto" data-email="%s"></span>'
    matches = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}', content)
    for m in matches:
        content = content.replace(m, template % base64.b64encode(m))
        print m  
    #re.sub(r'', repl, string, count, flags) (r'', content)
    return content 
