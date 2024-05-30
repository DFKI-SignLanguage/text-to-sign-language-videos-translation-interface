from django.db import models

class Translation(models.Model):
    source_text = models.TextField()
    #video_url = models.CharField(max_length=255)
    translation = models.TextField()
    # eval_score_general = models.IntegerField()
