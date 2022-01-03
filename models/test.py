from tortoise.models import Model
from tortoise import fields


class Session(Model):
   id = fields.IntField(pk=True,)
   name = fields.TextField()
   
   class Meta:
      table = 'sessions'