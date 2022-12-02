from django.contrib import admin
from .models import Book,BookReviews,IssueReport,LateReport,ReserveReport
# Register your models here.

class CustomBookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('Title','ISBN','Description','Category','edition','author','availability','publisher')
    list_filter = ('Title','availability',)
    search_fields = ('Title','availability',)
    ordering = ('Title','availability',)


admin.site.register(Book, CustomBookAdmin)
# admin.site.register(BookReviews)
# admin.site.register(IssueReport)
# admin.site.register(LateReport)
# admin.site.register(ReserveReport)
