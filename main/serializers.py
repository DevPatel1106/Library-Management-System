from rest_framework import serializers
from .models import Book, BookReviews


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookReviewSerializer(serializers.ModelSerializer):
    # book = BookSerializer()

    # def create(self, validated_data):
    #     # books_review = validated_data.pop('book')
    #     print(self.validated_data['book'])
    #     print('ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
    #     book = Book.objects.get(ISBN=self.validated_data['book'])
    #     # for book_review in books_review:
    #     #     BookReviews.objects.create(book=book,**book_review)
    #     rev=BookReviews.objects.create(book=book,**validated_data)
    #     return rev

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