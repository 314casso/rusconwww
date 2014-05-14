# -*- coding: utf-8 -*-
from django import template
from geo_office.models import ContactType

register = template.Library()
@register.filter
def to_comma_sep(iterval):
    result = []
    for contact in iterval.all():
        if not contact.contact_type_id == ContactType.EMAIL:
            result.append(u'<strong>%s</strong>: %s' % (contact.contact_type, contact.contact))
    if result:
        return u' <br /> '.join(result)
    return u'-'