from django.db import models

class UserMember(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    voice_recording = models.FileField(upload_to='voice_recordings/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
