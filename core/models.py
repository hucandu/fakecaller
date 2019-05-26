from django.db import models
from django.contrib.auth.models import User
from helpers.mixins import SafeDeleteMixinExtended,BaseMixin


class PhoneBook(SafeDeleteMixinExtended, BaseMixin):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=30)


class PhoneNumberOwnerName(SafeDeleteMixinExtended, BaseMixin):
    phone_number = models.ForeignKey(PhoneBook, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    @property
    def get_profile(self):
        profile_dict = {
            "name" : "",
            "email" : "",
            "phone_number" : "",
            "is_spam" : ""
        }
        profile_dict["name"] = self.name
        profile_dict["email"] = self.phone_number.user.email
        profile_dict["phone_number"] = self.phone_number.phone_number
        profile_dict["is_spam"] =  len(self.phone_number.user.spammarker_set.all()) > 0
        return profile_dict


class SpamMarker(SafeDeleteMixinExtended, BaseMixin):
    marked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    spammer = models.OneToOneField(PhoneBook, on_delete=models.CASCADE)
