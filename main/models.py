from django.db import models

# Create your models here.
# from users.models import Reader,Staff

class Book(models.Model):
    Title = models.CharField(('Title'), max_length=255, blank=False)
    ISBN = models.PositiveIntegerField(('ISBN'), primary_key=True, max_length=16, blank=False)
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
    ReportID = models.IntegerField(primary_key=True, max_length=10)
    ReportDate = models.DateField(blank=True)
    #reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class IssueReport(CommonInfo):
    ReturnDate = models.DateField(blank=True)
    #IssuedBy = models.ForeignKey(Staff, on_delete=models.CASCADE)

class LateReport(CommonInfo):
    DaysOverDue = models.IntegerField(max_length=10)
    FinePaid = models.BooleanField(default=False)

class ReserveReport(CommonInfo):
    ReserveTime = models.DateTimeField(blank=True)
    

