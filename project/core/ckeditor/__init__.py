from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string

class CKEditor(forms.Textarea):
        
    def render(self, name, value, attrs=None):
        if value is not None and not isinstance(value, basestring):
            value = edit_string_for_tags([o.tag for o in value.select_related("tag")])
        html = super(CKEditor, self).render(name, value, attrs)
        js = render_to_string('ckeditor/base.html', { 
            'id': attrs['id'], 
            'STATIC_URL': settings.STATIC_URL,  
            'toolbar': attrs.get('toolbar', 'Default')
        })
        
        return mark_safe("\n".join([html, js]))

    class Media:
        static_url = getattr(settings, 'JS_PACKS_URL', '%spacks' % settings.STATIC_URL)
        js = (
            '%s/ckeditor/ckeditor.js' % static_url,
        )