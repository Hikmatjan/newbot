from django.db import models


# Create your models here.


class Region(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'regions'
        ordering = ('name',)

    def __str__(self):
        return self.name


class District(models.Model):
    region = models.ForeignKey(Region, models.PROTECT, verbose_name="Viloyat nomi")
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "tumans"
        ordering = ("region",)

    def __str__(self):
        return f"{self.region.name}  {self.name}"


class Tugarak(models.Model):
    regio = models.ForeignKey(District, models.PROTECT, verbose_name="Tuman nomi")
    name = models.CharField("To'garak nomi", max_length=255)



    class Meta:
        db_table = 'tugaraks'

    def __str__(self):
        return f"{self.regio.name}    {self.name}"



# class Yunalish(models.Model):
#     regio=models.ForeignKey(Tugarak,models.PROTECT,verbose_name="To'garak nomi")
#     name=models.CharField("yo'nalish nomi",max_length=255)
#     description = models.TextField()
#     phone_number = models.CharField("Aloqa nomeri", max_length=255)
#
#
#
#     class Meta:
#         db_table='yunalish'
#
#     def  __str__(self):
#         return f"{self.regio.name} {self.name}"

