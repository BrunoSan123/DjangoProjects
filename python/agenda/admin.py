from django.contrib import admin

from agenda.models import Usuarios,Reservas,CheckIn,CheckOut

class Usuario(admin.ModelAdmin):
    list_display=('id','nome','rg','email','data_de_cadastro')
    list_display_links=('id','nome')
    search_fields=('nome',)

admin.site.register(Usuarios,Usuario)



class Reserva(admin.ModelAdmin):
    list_display=('id','usuario','dias')
    list_display_links=('usuario','dias')
    search_fields=('usuario',)

admin.site.register(Reservas,Reserva)


class Checkin(admin.ModelAdmin):
    list_display=('id','usuario','quarto','servico_de_quarto')
    list_display_links=('usuario','quarto')
    search_fields=('quarto',)
admin.site.register(CheckIn,Checkin)


class Checkout(admin.ModelAdmin):
    list_display=('usuario','quarto','despesas')
    list_display_links=('usuario','despesas')
    search_fields=('usuario',)
admin.site.register(CheckOut,Checkout)



