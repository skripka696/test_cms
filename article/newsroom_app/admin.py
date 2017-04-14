from django.contrib import admin
from newsroom_app.models import Article, Field, Style, StyleValue, ArticleContent, Comment, Revision

admin.site.register(Article)
admin.site.register(Field)
admin.site.register(Style)
admin.site.register(StyleValue)
admin.site.register(ArticleContent)
admin.site.register(Comment)
admin.site.register(Revision)
