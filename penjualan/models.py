from django.db import models

class Distrik(models.Model):
    id_distrik = models.IntegerField(primary_key=True)
    distrik = models.CharField(max_length=30)

    class Meta:
        ordering = ['id_distrik']

    def __str__(self):
        return self.distrik

class Kampung(models.Model):
    id_kampung = models.IntegerField(primary_key=True)
    distrik = models.ForeignKey(Distrik, related_name='kampungs', on_delete=models.CASCADE)
    kampung = models.CharField(max_length=30)

    class Meta:
        unique_together = ['distrik','id_kampung']
        ordering = ['id_kampung']

    def __str__(self):
        return self.kampung

class Nelayan(models.Model):
    id_nelayan = models.AutoField(primary_key=True)
    nama_nelayan = models.CharField(max_length=150)
    distrik = models.ForeignKey(Distrik, on_delete=models.CASCADE)
    kampung = models.ForeignKey(Kampung, on_delete=models.CASCADE)
    status_nelayan = models.CharField(max_length=20)
    perahu = models.CharField(max_length=20)
    tgl_lahir = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.nama_nelayan
