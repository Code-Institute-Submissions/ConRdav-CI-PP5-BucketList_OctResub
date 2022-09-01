from django.db import models
from django.contrib.auth.models import User
from adventures.models import Country

# Create your models here.


class Testimonial(models.Model):
    """
    Model for blog posts and all the fields included
    """

    RATING_CHOICES = (
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    )

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='blog_posts')
    pub_date = models.DateTimeField(auto_now=True,
                                    verbose_name='Publication Date')
    comment = models.TextField(max_length=1024)
    value = models.IntegerField(choices=RATING_CHOICES, default=1)

    def __str__(self):
        return '{0}/{1} - {2}'.format(self.country.name, self.user, self.value)

    class Meta:
        verbose_name = "Testimnoial"
        verbose_name_plural = "Testimonials"
        ordering = ['-pub_date']
