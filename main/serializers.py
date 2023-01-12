from rest_framework import serializers
from .models import Book, BookReviews


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookReviewSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    def create(self, validated_data):
        books_review = validated_data.pop('book')
        book = Book.objects.create(**validated_data)
        for book_review in books_review:
            BookReviews.objects.create(book=book,**book_review)
        return book

    # book = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())
    class Meta:
        model = BookReviews
        fields = '__all__'