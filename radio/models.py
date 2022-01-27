from cProfile import label
from django.db import models

# All Seasons

class All_Season(models.Model):
    season_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.season_name)

# All Episodes

class Episodes(models.Model):
    link            = models.ForeignKey(All_Season , on_delete=models.CASCADE)
    episode_name    = models.CharField(max_length=100)
    episode_name_en = models.CharField(max_length=100)
    episode_image   = models.ImageField(upload_to="static/img/episode" , blank = True , null = True)
    episode_url     = models.URLField()

  
