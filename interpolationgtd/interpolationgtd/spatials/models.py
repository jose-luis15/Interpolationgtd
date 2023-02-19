from django.contrib.gis.db import models as model_gis

class CrossPointField(model_gis.Model):
    point = model_gis.PointField(
        "Localización Entities", help_text="Lat/Long", srid=4326, blank=True, null=True
    )


