from django.test import TestCase
from django.urls import reverse
from .models import Book

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = "title test",
            subtitle = "subtitle test",
            author = "author test",
            isbn = "123456",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "title test")
        self.assertEqual(self.book.subtitle, "subtitle test")
        self.assertEqual(self.book.author, "author test")
        self.assertEqual(self.book.isbn, "123456")

    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "title test")
        self.assertTemplateUsed(response, "book_list.html")
