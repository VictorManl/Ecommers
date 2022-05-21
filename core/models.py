from django.db import models


# Create your models here.

class producto(models.Model):
    prod_id = models.AutoField('Id', primary_key=True)
    prod_nombre = models.CharField('Nombre', max_length=100, null=False, blank=False)
    prod_descripcion = models.CharField('Descripcion', max_length=200, null=False, blank=False)
    prod_cantidad = models.IntegerField('Cantidad', null=False, blank=False)
    prod_img = models.ImageField('Imagen', upload_to='Productos/')
    prod_precio = models.IntegerField('Precio', null=False, blank=False)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['prod_id']

    def __str__(self):
        texto = "{0} - {1} - ${2}"
        return texto.format(self.prod_nombre, self.prod_cantidad, self.prod_precio)
