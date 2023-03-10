from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models as model_gis



class User(AbstractUser):
    """
    Default custom user model for InterpolationGTD.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class CrossPointField(model_gis.Model):
    """CrossPointField is a Point relation which crosses django app boundary.

    In the near future, when django apps are converted into microservices,
    this foreign key will be broken. We declare them as CrossOneToOne
    to have these identified more clearly.

    """
    point = model_gis.PointField(
        "Localización Entities", help_text="Lat/Long", srid=4326, blank=True, null=True
    )

