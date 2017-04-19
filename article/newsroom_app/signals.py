from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from newsroom_app.models import Field, StyleValue
from django.template import Template, Context
from django.template.loader import get_template
from article.settings import BASE_DIR
import os


@receiver(m2m_changed, sender=Field.style.through)
@receiver(m2m_changed, sender=StyleValue)
def generate_css(instance, **kwargs):
    file_style_name = 'article_style.css'
    style_template_dir = os.path.join(BASE_DIR, 'templates', 'style_template.html')
    file_style_dir = os.path.join(BASE_DIR, 'static', file_style_name)
    fields_style = Field.objects.all()

    temp = get_template(style_template_dir)

    my_template = temp.render({'selectors': fields_style})

    print(kwargs['action'])
    print(my_template)
    filename = open(file_style_dir, 'w')
    filename.write(my_template)
    filename.close()
