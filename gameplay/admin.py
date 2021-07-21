from django.contrib import admin
from gameplay.models import Game,Move
    # ,statusclass

# @admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['id','first_player','second_player','status','start_time']
    list_editable = ('status',)
# admin.site.register(Game)
admin.site.register(Game,GameAdmin)
# admin.site.register(Move)
# admin.site.register(statusclass)
@admin.register(Move)
class moveadmin(admin.ModelAdmin):
    list_display = ['x', 'y', 'comment', 'is_first_player','game']
