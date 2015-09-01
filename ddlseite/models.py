# Encoding: utf-8
from django.db import models

# Create your models here.
class Status(models.Model):
    stat = models.CharField(max_length=50, verbose_name='Status')
    hexcol = models.CharField(max_length=6, verbose_name='Hex-Farbe')
    def __unicode__(self):
        return self.stat
    class Meta:
        verbose_name='Status'
        verbose_name_plural='Status'

class Project(models.Model):
    name = models.CharField(max_length=200,verbose_name='Projektname')
    image = models.URLField(max_length=300,verbose_name='Projektbild')
    genre = models.CharField(max_length=200,verbose_name='Genre')
    number_of_episodes = models.CharField(max_length=4,verbose_name='Gesamtfolgen')
    progress = models.CharField(max_length=4,verbose_name='Fortschritt')
    state = models.ForeignKey(Status,help_text="Status im Status-Bereich hinzufügen/ändern.", verbose_name='Status')
    listinindex = models.BooleanField(default=True,verbose_name='In Indexliste zeigen?')
    torrentbatch = models.URLField(max_length=300,blank=True,verbose_name='Torrent-Batch Override')
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name='Projekt'
        verbose_name_plural='Projekte'
        
class Nick(models.Model):
    nickname = models.CharField(max_length=200,help_text="Für Aufgabenverteilung nötig.",verbose_name='Nickname')
    #realname = models.CharField(max_length=200,blank=True,verbose_name='richtiger Name')
    def __unicode__(self):
        return self.nickname
    class Meta:
        verbose_name='Nick'
        verbose_name_plural='Nicks'

class Episode(models.Model):
    project = models.ForeignKey(Project,verbose_name='Projekt')
    number = models.CharField(max_length=4,verbose_name='Episode')
    title = models.CharField(max_length=100,verbose_name='Titel')
    date = models.DateField(verbose_name='Datum')
    filesize = models.DecimalField(max_digits=6, decimal_places=2,verbose_name='Dateigröße')
    ddl = models.CharField(max_length=300,verbose_name='DDL')
    torrent = models.URLField(max_length=300,verify_exists=False,verbose_name='Torrent')
    XDCCHaruhi = models.CharField(max_length=5,blank=True,verbose_name='XDCC|Haruhi')
    XDCCYoumu = models.CharField(max_length=5,verbose_name='XDCC|Youmu')
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name='Episode'
        verbose_name_plural='Episoden'
        
class table_title(models.Model):
    project = models.ForeignKey(Project,verbose_name='Projekt')
    table_title_name = models.CharField(max_length=200,verbose_name='Tabellentitel')
    table_title_link = models.URLField(max_length=300,blank=True,verbose_name='Titellink')
    def __unicode__(self):
        return self.table_title_name
    class Meta:
        verbose_name='Tabellentitel'
        verbose_name_plural='Tabellentitel'
        
class Who_did_what(models.Model):
    project = models.ForeignKey(Project,verbose_name='Projekt')
    nick = models.ForeignKey(Nick)
    what = models.CharField(max_length=200, verbose_name='Aufgaben')
    def __unicode__(self):
        return self.nick.__unicode__()
    class Meta:
        verbose_name='Aufgabenverteilung'
        verbose_name_plural='Aufgabenverteilung'

# EOF models.py