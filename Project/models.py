from django.db import models



#########ProjectModel_EN"
class CssProjectModel (models.Model):
    title = models.CharField(max_length = 150)
    videos = models.FileField(upload_to = 'Project_videos')


class RubyProjectModel(models.Model):
    title = models.CharField(max_length = 150)
    videos = models.FileField(upload_to = 'Project_videos')


class PythonProjectModel(models.Model):
    title = models.CharField(max_length = 150)
    videos = models.FileField(upload_to = 'Project_videos')


class GoProjectModel (models.Model):
    title = models.CharField(max_length = 150)
    videos = models.FileField(upload_to = 'Project_videos')


class NodeProjectModel (models.Model):
    title = models.CharField(max_length = 150)
    videos = models.FileField(upload_to = 'Project_videos')


class DjangoProjectModel (models.Model):
    title = models.CharField(max_length = 150)
    videos = models.FileField(upload_to = 'Project_videos')


class ReactProjectModel (models.Model):
    title = models.CharField(max_length = 150)
    videos = models.FileField(upload_to = 'Project_videos')    


class HtmlProjectModel (models.Model):
    title = models.CharField(max_length = 150)
    videos = models.FileField(upload_to = 'Project_videos')


class JavaProjectModel (models.Model):
    title = models.CharField(max_length = 150)
    videos = models.FileField(upload_to = 'Project_videos')


class CProjectModel (models.Model):
    title = models.CharField(max_length = 150)
    videos = models.FileField(upload_to = 'Project_videos')


class CsharpProjectModel (models.Model):
    title = models.CharField(max_length = 150)
    videos = models.FileField(upload_to = 'Project_videos')


class C_pluseProjectModel (models.Model):
    title = models.CharField(max_length = 150)
    videos = models.FileField(upload_to = 'Project_videos')


class FlutterProjectModel (models.Model):
    title = models.CharField(max_length = 150)
    videos = models.FileField(upload_to = 'Project_videos')


class JavascriptProjectModel (models.Model):
    title = models.CharField(max_length = 150)
    videos = models.FileField(upload_to = 'Project_videos')


