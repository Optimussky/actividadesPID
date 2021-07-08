from django.db import models

# Create your models here.
class Tipo_area(models.Model):
    idTipoArea  = models.AutoField(primary_key=True)
    tipo_area   = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.tipo_area)

    def save(self):
        self.tipo_area = self.tipo_area.upper()
        super(Tipo_area,self).save()

    class Meta:
        verbose_name_plural = "Tipo_areas"


class Sector(models.Model):
    idSector = models.AutoField(primary_key=True)
    sector   = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return '{}'.format(self.sector)
    
    def save(self):
        self.sector = self.sector.upper()
        super(Sector,self).save()

    class Meta:
        verbose_name_plural = "Sectores"


class Area(models.Model):
    idArea      = models.AutoField(primary_key=True)
    area        = models.CharField(max_length=120)
    idTipoArea  = models.ForeignKey(Tipo_area, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.area,self.idTipoArea)

    class Meta:
        verbose_name_plural = "Areas"
        ordering = ["area"]

class Usuario_activo(models.Model):
    idUsuarioActivo = models.AutoField(primary_key=True) 
    estado          = models.CharField(max_length=10)

    def __str__(self):
        return '{}'.format(self.estado)
    
    def save(self):
        self.estado = self.estado.upper()
        super(Usuario_activo,self).save()

    class Meta:
        verbose_name_plural = "Usuarios_activos"

class Usuario(models.Model):
    idUsuario         = models.AutoField(primary_key=True) 
    usuario           = models.CharField(max_length=60)
    id_tipo_area      = models.ForeignKey(Tipo_area, on_delete=models.CASCADE)
    id_area           = models.ForeignKey(Area, on_delete=models.CASCADE)
    id_usuario_activo = models.ForeignKey(Usuario_activo, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.usuario)
    

    def save(self):
        self.usuario = self.usuario.upper()
        super(Usuario,self).save()
    
    class Meta:
        verbose_name_plural = "Usuarios"

class Actividad(models.Model):
    idActividad = models.AutoField(primary_key=True) 
    actividad   = models.CharField(max_length=60)

    def __str__(self):
        return '{}'.format(self.actividad)
    

    def save(self):
        self.actividad = self.actividad.upper()
        super(Actividad,self).save()

    class Meta:
        verbose_name_plural = "Actividades"

class Estatus_actividad(models.Model):
    idEstatusActividad  = models.AutoField(primary_key=True) 
    estatus             = models.CharField(max_length=15)

    def __str__(self):
        return '{}'.format(self.estatus)
    

    def save(self):
        self.estatus = self.estatus.upper()
        super(Estatus_actividad,self).save()

    class Meta:
        verbose_name_plural = "Estatus_actividades"

class Turno(models.Model):
    idTurno  = models.AutoField(primary_key=True) 
    turno    = models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.turno)
    

    def save(self):
        self.turno = self.turno.upper()
        super(Turno,self).save()

    class Meta:
        verbose_name_plural = "Turnos"

class Registro_actividad(models.Model):
    idRegistroActividad = models.AutoField(primary_key=True) 
    idUsuario           = models.ForeignKey(Usuario,verbose_name="Usuario", on_delete=models.CASCADE)
    descripcion         = models.TextField(verbose_name="Descripción")
    idActividad         = models.ForeignKey(Actividad,verbose_name="Actividad", on_delete=models.CASCADE)
    #idArea              = models.ForeignKey(Area,verbose_name="Área que nos llama", on_delete=models.CASCADE)
    idEstatusActividad  = models.ForeignKey(Estatus_actividad,verbose_name="Estatus", on_delete=models.CASCADE)
    idTurno             = models.ForeignKey(Turno,verbose_name="Turno", on_delete=models.CASCADE)
    fechaRegistro       = models.DateField(auto_now=True, verbose_name="Fecha",auto_now_add=False) 

    def __str__(self):
        return '{} / {} / {} / {}'.format(self.fechaRegistro,self.idActividad,self.idUsuario,self.idTurno)
    

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Registro_actividad,self).save()

    class Meta:
        verbose_name_plural = "Registro_actividades"
        ordering = ['-fechaRegistro']