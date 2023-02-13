from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


#########"ProjectAdmin"
class ModelProjectAdmin(TranslationAdmin):
    pass
admin.site.register(CssProjectModel,ModelProjectAdmin)
admin.site.register(RubyProjectModel,ModelProjectAdmin)
admin.site.register(PythonProjectModel,ModelProjectAdmin)
admin.site.register(GoProjectModel,ModelProjectAdmin)
admin.site.register(NodeProjectModel,ModelProjectAdmin)
admin.site.register(DjangoProjectModel,ModelProjectAdmin)
admin.site.register(ReactProjectModel,ModelProjectAdmin)
admin.site.register(HtmlProjectModel,ModelProjectAdmin)
admin.site.register(JavaProjectModel,ModelProjectAdmin)
admin.site.register(CProjectModel,ModelProjectAdmin)
admin.site.register(CsharpProjectModel,ModelProjectAdmin)
admin.site.register(C_pluseProjectModel,ModelProjectAdmin)
admin.site.register(FlutterProjectModel,ModelProjectAdmin)
admin.site.register(JavascriptProjectModel,ModelProjectAdmin)
