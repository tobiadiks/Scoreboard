from django.db import models

class Score(models.Model):
	club1 = models.TextField()
	club2 = models.TextField()
	club1score = models.CharField(max_length = 2)
	club2score = models.CharField(max_length = 2)
	def __str__(self):
		return self.club1
		return self.club2
		return club1score
		return club2score

