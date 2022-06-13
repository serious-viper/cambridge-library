from django.db import models

# Create your models here.

COURSE_CHOICES = (
    ('BE', 'BE'),
    ('MCA', 'MCA'),
    ('MBA', 'MBA'),
    ('MTech', 'MTech')
)

class Book(models.Model):
    course = models.CharField(max_length=1000, choices=COURSE_CHOICES)
    title = models.CharField(max_length=5000, null=True, blank=True)
    author = models.CharField(max_length=1000, null=True, blank=True)
    edition = models.CharField(max_length=1000, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    publisher = models.CharField(max_length=2000, null=True, blank=True)
    department = models.CharField(max_length=1000, null=True, blank=True)
    count = models.IntegerField()

    def __str__(self) -> str:
        return self.title

