import time

from django.db.models import Model, ImageField, CharField, TextField, EmailField

from apps.tasks import task_send_email


class Workers(Model):
    image = ImageField(upload_to='workers/images/', default='workers/images/default.jpg')
    username = CharField(max_length=255)
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    email = EmailField()
    bio = TextField(null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        emails: list = [self.email]
        start = time.time()
        task_send_email.delay("Saytimizga xush kelibsiz !", self.username, list(emails))
        end = time.time()
        print(end - start, 's -- vaqt ')

    def __str__(self):
        return self.username
