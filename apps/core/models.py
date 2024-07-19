from django.db.models import Model, DateTimeField


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True, editable=False)
    last_update = DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True
