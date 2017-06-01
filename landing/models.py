from django.db import models

# Create your models here.
class Subscriber(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()


    def __str__(self):
        return "User %s: %s" % (self.name, self.email,)

    class Meta:
        verbose_name = 'MySubscriber'
        verbose_name_plural = 'A lot of Subscriber'
