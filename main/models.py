from django.db import models

# Create your models here.
from users.models import UserProfile

class Book(models.Model):
    ISBN = models.PositiveIntegerField(('ISBN'), primary_key=True, blank=False)
    Title = models.CharField(('Title'), max_length=255, blank=False)
    Description = models.TextField(blank=True)
    Category = models.CharField(blank=True, max_length=15)
    edition = models.CharField(blank=True, max_length=15)
    author = models.CharField(blank=False, max_length=15)
    availability = models.BooleanField(default=True)
    publisher = models.CharField(blank=False, max_length=15)

    def __str__(self):
        return self.Title


class BookReviews(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    headline = models.CharField(max_length=100)
    review = models.TextField(blank=True, max_length=256)
    review_date = models.DateField()

    def __str__(self):
        return self.headline

class CommonInfo(models.Model):
    ReportID = models.IntegerField(primary_key=True)
    ReportDate = models.DateField(blank=True)
    reader = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class IssueReport(CommonInfo):
    ReturnDate = models.DateField(blank=True)
    IssuedBy = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name= 'IssuedBy')

class LateReport(CommonInfo):
    DaysOverDue = models.IntegerField(blank=True)
    FinePaid = models.BooleanField(default=False)

class ReserveReport(CommonInfo):
    ReserveTime = models.DateTimeField(blank=True)
    

