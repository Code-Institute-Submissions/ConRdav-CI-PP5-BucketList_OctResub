from django.db import models
from django.contrib.auth.models import User
from adventures.models import Country

# Create your models here.


RATING_CHOICES = (
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    )


class Testimonial(models.Model):
    """
    Model for the testimonial posts 
    """

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='testimonials')
    pub_date = models.DateTimeField(auto_now=True,
                                    verbose_name='Publication Date')
    comment = models.TextField(max_length=1024, blank=False)
    value = models.IntegerField(choices=RATING_CHOICES, default=1)

    def __str__(self):
        return  f'User {self.user} commented {self.comment} '
        f'with a rating of {self.rating}'

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
        ordering = ['-pub_date']
