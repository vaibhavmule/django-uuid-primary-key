import uuid

from django.db import models


class UUIDPrimaryKey(models.Model):
    """
    An abstract base class model that provides
    primary key id as uuid.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True
