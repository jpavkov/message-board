from django.db import models

# Post is a new database model, text is a new field, 
# and TextField is the type of field
class Post(models.Model): 
    text = models.TextField()

    def __str__(self):
        return self.text[:50]