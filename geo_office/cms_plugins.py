from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from geo_office.models import Office, OfficeCMSPlugin, PLUGIN_TEMPLATES


class OfficePlugin(CMSPluginBase):
        model = OfficeCMSPlugin
        name = _("Offices")        
        render_template = PLUGIN_TEMPLATES[0][0]
        def render(self, context, instance, placeholder):
            offices = Office.objects.all()
            if instance and instance.template:
                self.render_template = instance.template
            if instance and instance.ids:
                ids = instance.ids.split(',')
                ids = [i.strip() for i in ids] 
                offices = offices.filter(id__in=ids)
                office = offices[:1].get() if offices else None
            context.update({
                    'offices': offices,
                    'placeholder': placeholder,
                    'object': instance,
                    'office': office,
            })
            return context
                
plugin_pool.register_plugin(OfficePlugin)

    