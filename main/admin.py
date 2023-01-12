from django.contrib import admin
from .models import Book,BookReviews,IssueReport,LateReport,ReserveReport
# Register your models here.

class CustomBookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('Title','ISBN','Description','Category','edition','author','availability','publisher')
    list_filter = ('Title','availability',)
    search_fields = ('Title','availability',)
    ordering = ('Title','availability',)

class CustomBookReviewAdmin(admin.ModelAdmin):
    model = BookReviews
    list_display = ('book','headline','review','review_date')
    list_filter = ('book',)
    search_fields = ('book',)
    ordering = ('book',)

class CustomIssueReportAdmin(admin.ModelAdmin):
    model = IssueReport
    list_display = ('book','reader','ReportDate','ReportID','ReturnDate','IssuedBy')
    list_filter = ('book',)
    search_fields = ('book',)
    ordering = ('book',)

class CustomLateReportAdmin(admin.ModelAdmin):
    model = LateReport
    list_display = ('book','reader','ReportDate','ReportID','DaysOverDue','FinePaid')
    list_filter = ('book',)
    search_fields = ('book',)
    ordering = ('book',)

class CustomReserveReportAdmin(admin.ModelAdmin):
    model = ReserveReport
    list_display = ('book','reader','ReportDate','ReportID','ReserveTime')
    list_filter = ('book',)
    search_fields = ('book',)
    ordering = ('book',)

admin.site.register(Book, CustomBookAdmin)
admin.site.register(BookReviews, CustomBookReviewAdmin)
admin.site.register(IssueReport, CustomIssueReportAdmin)
admin.site.register(LateReport, CustomLateReportAdmin)
admin.site.register(ReserveReport, CustomReserveReportAdmin)
