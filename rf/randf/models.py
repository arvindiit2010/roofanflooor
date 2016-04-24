from django.db import models

# Create your models here.


class MovieRating(models.Model):
    valid_rating = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),

    )

    name = models.CharField(null=False, max_length=255)
    rating = models.PositiveIntegerField(null=False, choices=valid_rating)
    comment = models.CharField(null=True, max_length=255)


    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'movie information'
        db_table = 'movie_rating'
    app_label = 'randf'


class CustomUser(models.Model):
  user_name = models.CharField(unique=True,max_length=255,default='ram')
  contact = models.PositiveIntegerField(unique=True,)
  email = models.EmailField(unique=True,default='ram@gmail.com')
  first_name =models.CharField(max_length=50,default='ram')
  last_name = models.CharField(max_length=50, default='raja')

