from django.contrib.auth.models import User
from core.models import PhoneBook, PhoneNumberOwnerName
from rest_framework import serializers, exceptions
class RegistrationService():
    """
    This is responsible for all registration related services
    """
    @classmethod
    def register_user(self, phone_number, name, email, password):
        try:
            user = User.objects.create_user(phone_number, email, password)

            phone_book = None
            try:
                phone_book = PhoneBook.objects.get(phone_number=phone_number)
            except PhoneBook.DoesNotExist:
                phone_book = PhoneBook(phone_number=phone_number, user=user)
                phone_book.save()

            phone_book_owner_name = PhoneNumberOwnerName(phone_number=phone_book, name=name)
            phone_book_owner_name.save()
            return user
        except  Exception as e:
            raise exceptions.ValidationError("Unable to register user")
