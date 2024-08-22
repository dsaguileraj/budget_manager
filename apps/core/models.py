from datetime import datetime
from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True


class AuditModel(BaseModel):
    create_at: datetime = models.DateTimeField(
        auto_now_add=True, editable=False)
    update_at: datetime = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True
