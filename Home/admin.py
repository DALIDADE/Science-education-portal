from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

########'SapaklarAdmin
class ModelAdmin(TranslationAdmin):
    pass
admin.site.register(CssModel,TranslationAdmin)
admin.site.register(RubyModel,TranslationAdmin)
admin.site.register(PythonModel,TranslationAdmin)
admin.site.register(GoModel,TranslationAdmin)
admin.site.register(NodeModel,TranslationAdmin)
admin.site.register(DjangoModel,TranslationAdmin)
admin.site.register(ReactModel,TranslationAdmin)
admin.site.register(HtmlModel,TranslationAdmin)
admin.site.register(JavaModel,TranslationAdmin)
admin.site.register(CModel,TranslationAdmin)
admin.site.register(CsharpModel,TranslationAdmin)
admin.site.register(C_pluseModel,TranslationAdmin)
admin.site.register(FlutterModel,TranslationAdmin)
admin.site.register(JavascriptModel,TranslationAdmin)

