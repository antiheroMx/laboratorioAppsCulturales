from django.db import models

class Artista(models.Model):
    nombre        = models.CharField(max_length=30)
    apellido_p    = models.CharField(max_length=30)
    apellido_m    = models.CharField(max_length=30)
    sexo          = models.CharField(max_length=20)
    correo        = models.CharField(max_length=50)
    nombre_artis  = models.CharField(max_length=30)
    curriculum    = models.CharField(max_length=500)
    nombre_com    = models.CharField(max_length=30)
    cargo         = models.CharField(max_length=30)
    semblanza     = models.CharField(max_length=500)
    dir_usu       = models.CharField(max_length=50)
    dir_com       = models.CharField(max_length=50)
    foto_per      = models.CharField(max_length=400)
    foto_com      = models.CharField(max_length=400)
    red_soc_per   = models.CharField(max_length=400)
    red_soc_com   = models.CharField(max_length=400)
    web           = models.CharField(max_length=400)

    def __str__(self):
        return '%s %s %s' % (self.nombre, self.apellido_p, self.apellido_m)

class Programador(models.Model):
    nombre     = models.CharField(max_length=30)
    apellido_p = models.CharField(max_length=30)
    apellido_m = models.CharField(max_length=30)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido_p)


class Coleccionista(models.Model):
    nombre     = models.CharField(max_length=30)
    apellido_p = models.CharField(max_length=30)
    apellido_m = models.CharField(max_length=30)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido_p)


class Pieza(models.Model):
    nombre          = models.CharField(max_length=30)
    descripcion     = models.CharField(max_length=30)
    tecnica         = models.CharField(max_length=30)
    tipo_prod       = models.CharField(max_length=30)
    disciplina      = models.CharField(max_length=30)
    sinopsis        = models.CharField(max_length=500)
    ano_creac       = models.IntegerField()
    num_pers_prod   = models.IntegerField()
    num_pers_tal    = models.IntegerField()
    tipo_foro       = models.CharField(max_length=30)
    aforo_obra      = models.CharField(max_length=30)
    tipo_financ     = models.CharField(max_length=30)
    foto_cartel     = models.CharField(max_length=400)
    url_video       = models.CharField(max_length=400)
    observaciones   = models.CharField(max_length=400)
    artista         = models.ForeignKey(Artista)
    coleccionista   = models.ForeignKey(Coleccionista)

    def __str__(self):
        return '%s - %s' % (self.nombre, self.descripcion)


class Sede(models.Model):
    nombre_sede     = models.CharField(max_length=30)
    tipo_sede       = models.CharField(max_length=30)
    financiamiento  = models.CharField(max_length=30)
    ubicacion       = models.CharField(max_length=30)
    direccion       = models.CharField(max_length=30)
    ano_present     = models.IntegerField()
    tipo_gestion    = models.CharField(max_length=30)
    Caract          = models.CharField(max_length=400)
    num_presen      = models.IntegerField()

    def __str__(self):
        return '%s %s' % (self.nombre_sede, self.tipo_sede)

class Registro(models.Model):
    pieza           = models.ForeignKey(Pieza)
    programador     = models.ForeignKey(Programador)
    sede            = models.ForeignKey(Sede)

    def __str__(self):
        return '%s %s' % (self.pieza, self.sede)
