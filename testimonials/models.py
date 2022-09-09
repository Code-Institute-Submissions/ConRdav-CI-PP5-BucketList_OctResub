from django.db import models
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
    user = models.CharField(max_length=40, default="anonymous")
    pub_date = models.DateTimeField(auto_now=True,
                                    verbose_name='Publication Date')
    comment = models.TextField(max_length=1024, blank=False)
    value = models.IntegerField(choices=RATING_CHOICES, default=1)

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
        ordering = ['-pub_date']
