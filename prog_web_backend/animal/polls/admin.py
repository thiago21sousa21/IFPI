from django.contrib import admin
from polls.models import Animal, Atendimento, Tutor


class AnimalAdmin(admin.ModelAdmin):
    pass
   
class TutorAdmin(admin.ModelAdmin):
    pass
    
class AtendimentoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Animal, AnimalAdmin)
admin.site.register(Atendimento, AtendimentoAdmin)
admin.site.register(Tutor, TutorAdmin)