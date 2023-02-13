from dataclasses import field
from modeltranslation.translator import register,TranslationOptions
from .models import*

###################Project Translation

@register(CssProjectModel)
class CssProjectModelTranslationOptions(TranslationOptions):
    fields = ('title','videos',)

@register(RubyProjectModel)
class RubyProjectModelTranslationOptions(TranslationOptions):
    fields = ('title','videos',)

@register(PythonProjectModel)
class PythonProjectModelTranslationOptions(TranslationOptions):
    fields = ('title','videos',)

@register(GoProjectModel)
class GoProjectModelTranslationOptions(TranslationOptions):
    fields = ('title','videos',)

@register(NodeProjectModel)
class NodeProjectModelTranslationOptions(TranslationOptions):
    fields = ('title','videos',)

@register(DjangoProjectModel)
class DjangoProjectModelTranslationOptions(TranslationOptions):
    fields = ('title','videos',)

@register(ReactProjectModel)
class ReactProjectModelTranslationOptions(TranslationOptions):
    fields = ('title','videos',)

@register(HtmlProjectModel)
class  HtmlProjectModelTranslationOptions(TranslationOptions):
    fields = ('title','videos',)

@register(JavaProjectModel)
class JavaProjectModelTranslationOptions(TranslationOptions):
    fields = ('title','videos',)

@register(CProjectModel)
class CProjectModelTranslationOptions(TranslationOptions):
    fields = ('title','videos',)

@register(CsharpProjectModel)
class CsharpProjectModelTranslationOptions(TranslationOptions):
    fields = ('title','videos',)

@register(C_pluseProjectModel)
class C_pluseProjectModelTranslationOptions(TranslationOptions):
    fields = ('title','videos',)

@register(FlutterProjectModel)
class  FlutterProjectModelTranslationOptions(TranslationOptions):
    fields = ('title','videos',)

@register(JavascriptProjectModel)
class  JavascriptProjectModelTranslationOptions(TranslationOptions):
    fields = ('title','videos',)
