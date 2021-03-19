from django.db import models
from django.utils.timezone import now
from user.models import NepUser

# Create your models here.


class NepDiskFile(models.Model):
    total_count = models.IntegerField(default=0)
    code = models.CharField(max_length=10, null=True)
    upload_time = models.DateTimeField(default=now)
    upload_ip = models.CharField(max_length=16, null=True)
    file = models.FileField(upload_to='disk')
    name_display = models.FileField()
    owner = models.ForeignKey(NepUser, on_delete=models.CASCADE)

    def delete(self, using=None, keep_parents=False):
        storage, path = self.file.storage, self.file.path
        storage.delete(path)
        super(NepDiskFile, self).delete()

    class Meta:
        managed = True
        db_table = 'nep_disk_file'
        permissions = [('upload_file', 'Can upload file to disk')]
