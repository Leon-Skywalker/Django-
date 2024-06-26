from django.db import models


class BaseModel(models.Model):
    create_time = models.DateTimeField('创建时间', help_text='创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', help_text='更新时间', auto_now=True)
    is_delete = models.BooleanField('是否逻辑删除', help_text='是否逻辑删除', default=False)

    class Meta:
        abstract = True