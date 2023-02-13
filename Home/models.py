from django.db import models



###########"SpaklarModel_En"
class CssModel (models.Model):
    title = models.CharField(max_length = 150)
    videos = models.FileField(upload_to = 'Sapaklar_videos')


class RubyModel(models.Model):
    title = models.CharField(max_length = 150)
    videos = models.FileField(upload_to = 'Sapaklar_videos')


class PythonModel(models.Model):
    title = models.CharField(max_length = 150)
    videos = models.FileField(upload_to = 'Sapaklar_videos')


class GoModel (models.Model):
    title = models.CharField(max_length = 150)
    videos = models.FileField(upload_to = 'Sapaklar_videos')


class NodeModel (models.Model):
    title = models.CharField(max_length = 150)
    videos = models.FileField(upload_to = 'Sapaklar_videos')


class DjangoModel (models.Model):
    title = models.CharField(max_length = 150)
    videos = models.FileField(upload_to = 'Sapaklar_videos')


class ReactModel (models.Model):
    title = models.CharField(max_length = 150)
    videos = models.FileField(upload_to = 'Sapaklar_videos')    


class HtmlModel (models.Model):
    title = models.CharField(max_length = 150)
    videos = models.FileField(upload_to = 'Sapaklar_videos')


class JavaModel (models.Model):
    title = models.CharField(max_length = 150)
    videos = models.FileField(upload_to = 'Sapaklar_videos')


class CModel (models.Model):
    title = models.CharField(max_length = 150)
    videos = models.FileField(upload_to = 'Sapaklar_videos')


class CsharpModel (models.Model):
    title = models.CharField(max_length = 150)
    videos = models.FileField(upload_to = 'Sapaklar_videos')


class C_pluseModel (models.Model):
    title = models.CharField(max_length = 150)
    videos = models.FileField(upload_to = 'Sapaklar_videos')


class FlutterModel (models.Model):
    title = models.CharField(max_length = 150)
    videos = models.FileField(upload_to = 'Sapaklar_videos')


class JavascriptModel (models.Model):
    title = models.CharField(max_length = 150)
    videos = models.FileField(upload_to = 'Sapaklar_videos')
