from django.db import models

class WordPuzzle(models.Model):
    title = models.CharField(max_length=100)
    words = models.TextField(help_text="Enter the words separated by commas.")
    grid_size = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.title

