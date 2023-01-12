from rest_framework import serializers
from .models import Book, BookReviews, IssueReport, LateReport, ReserveReport
from users.models import UserProfile

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookReviewSerializer(serializers.ModelSerializer):

    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    class Meta:
        model = BookReviews
        fields = '__all__'

    def save(self):
        book =self.validated_data['book']
        print(book)
        review = BookReviews(
            book=Book.objects.get(Title=book),
            headline=self.validated_data['headline'],
            review_date=self.validated_data['review_date']
        )
        review.save()

class IssueSerializer(serializers.ModelSerializer):

    book = serializers.SlugRelatedField(
        queryset=Book.objects.all(),
        slug_field='ISBN'
    )
    reader = serializers.SlugRelatedField(
        queryset=UserProfile.objects.all(),
        slug_field='email'
    )
    IssuedBy = serializers.SlugRelatedField(
        queryset=UserProfile.objects.all(),
        slug_field='email'
    )

    class Meta:
        model = IssueReport
        fields = '__all__'

    def save(self, request):
        book =self.validated_data['book']
        reader = self.validated_data['reader']
        IssuedBy = self.validated_data['IssuedBy']

        report = IssueReport(
            book=Book.objects.get(Title=book),
            reader=UserProfile.objects.get(email=reader),
            IssuedBy=UserProfile.objects.get(email=IssuedBy),
            ReportID=self.validated_data['ReportID'],
            ReturnDate=self.validated_data['ReturnDate'],
            ReportDate=self.validated_data['ReportDate']
        )
        report.save()

class LateSerializer(serializers.ModelSerializer):

    book = serializers.SlugRelatedField(
        queryset=Book.objects.all(),
        slug_field='ISBN'
    )
    reader = serializers.SlugRelatedField(
        queryset=UserProfile.objects.all(),
        slug_field='email'
    )

    class Meta:
        model = LateReport
        fields = '__all__'

    def save(self, request):
        book =self.validated_data['book']
        reader = self.validated_data['reader']

        report = LateReport(
            book=Book.objects.get(Title=book),
            reader=UserProfile.objects.get(email=reader),
            ReportID=self.validated_data['ReportID'],
            DaysOverDue=self.validated_data['DaysOverDue'],
            FinePaid=self.validated_data['FinePaid']
        )
        report.save()

class ReserveSerializer(serializers.ModelSerializer):

    book = serializers.SlugRelatedField(
        queryset=Book.objects.all(),
        slug_field='ISBN'
    )
    reader = serializers.SlugRelatedField(
        queryset=UserProfile.objects.all(),
        slug_field='email'
    )

    class Meta:
        model = ReserveReport
        fields = '__all__'

    def save(self, request):
        book =self.validated_data['book']
        reader = self.validated_data['reader']

        report = ReserveReport(
            book=Book.objects.get(Title=book),
            reader=UserProfile.objects.get(email=reader),
            ReportID=self.validated_data['ReportID'],
            ReserveTime=self.validated_data['ReserveTime']
        )
        report.save()

