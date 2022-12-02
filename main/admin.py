from django.contrib import admin
from .models import Book,BookReviews,IssueReport,LateReport,ReserveReport
# Register your models here.

admin.site.register(Book)
admin.site.register(BookReviews)
admin.site.register(IssueReport)
admin.site.register(LateReport)
admin.site.register(ReserveReport)
