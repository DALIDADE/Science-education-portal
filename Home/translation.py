from dataclasses import field
from modeltranslation.translator import register,TranslationOptions
from .models import*

@register(CssModel)
class CssModelTranslationOptions(TranslationOptions):
    fields = ('title','videos',)
    
@register(RubyModel)
class RubyModelTranslationOptions(TranslationOptions):
    fields = ('title','videos',)

@register(PythonModel)
class PythonModelTranslationOptions(TranslationOptions):
    fields = ('title','videos',)

@register(GoModel)
class GoModelTranslationOptions(TranslationOptions):
    fields = ('title','videos',)

@register(NodeModel)
class NodeModelTranslationOptions(TranslationOptions):
    fields = ('title','videos',)

@register(DjangoModel)
class DjangoModelTranslationOptions(TranslationOptions):
    fields = ('title','videos',)


@register(ReactModel)
class ReactModelTranslationOptions(TranslationOptions):
    fields = ('title','videos',)

@register(HtmlModel)
class  HtmlModelTranslationOptions(TranslationOptions):
    fields = ('title','videos',)

@register(JavaModel)
class JavaModelTranslationOptions(TranslationOptions):
    fields = ('title','videos',)

@register(CModel)
class CModelTranslationOptions(TranslationOptions):
    fields = ('title','videos',)

@register(CsharpModel)
class CsharpModelTranslationOptions(TranslationOptions):
    fields = ('title','videos',)

@register(C_pluseModel)
class C_pluseModelTranslationOptions(TranslationOptions):
    fields = ('title','videos',)

@register(FlutterModel)
class  FlutterModelTranslationOptions(TranslationOptions):
    fields = ('title','videos',)

@register(JavascriptModel)
class  JavascriptModelTranslationOptions(TranslationOptions):
    fields = ('title','videos',)
