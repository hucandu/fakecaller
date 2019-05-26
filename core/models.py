from django.db import models
from django.contrib.auth.models import User
from helpers.mixins import SafeDeleteMixinExtended,BaseMixin


class PhoneBook(SafeDeleteMixinExtended, BaseMixin):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=30)


class PhoneNumberOwnerName(SafeDeleteMixinExtended, BaseMixin):
    phone_number = models.ForeignKey(PhoneBook, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)


class SpamMarker(SafeDeleteMixinExtended, BaseMixin):
    marked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    spammer = models.OneToOneField(PhoneBook, on_delete=models.CASCADE)
