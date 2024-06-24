from django.contrib import admin
from .models import User,OficinaAmbiente,Solicitud,Caso,TipoProcedimiento,SolucionCaso,SolucionCasoTipoProcedimientos

# Register your models here.
admin.site.register(User)
admin.site.register(OficinaAmbiente)
admin.site.register(Solicitud)
admin.site.register(Caso)
admin.site.register(TipoProcedimiento)
admin.site.register(SolucionCaso)
admin.site.register(SolucionCasoTipoProcedimientos)