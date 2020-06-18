from django.contrib import admin

from api.models import User, Agent, Event, Group, GroupUser


class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_login', 'email', 'password')


class AgentModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'env', 'version', 'address')


class EventModelAdmin(admin.ModelAdmin):
    def name_agent(self, obj):
        return obj.agent.name

    name_agent.short_description = 'Agente'

    def name_user(self, obj):
        return obj.user.name

    name_user.short_description = 'Usuário'

    list_display = ('id', 'level', 'data', 'arquivado', 'date', 'name_agent', 'name_user')


class GroupModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class GroupUserModelAdmin(admin.ModelAdmin):
    def name_group(self, obj):
        return obj.group.name

    name_group.short_description = 'Grupo'

    def name_user(self, obj):
        return obj.user.name

    name_user.short_description = 'Usuário'

    list_display = ('id', 'name_user', 'name_group')


admin.site.register(User, UserModelAdmin)
admin.site.register(Agent, AgentModelAdmin)
admin.site.register(Event, EventModelAdmin)
admin.site.register(Group, GroupModelAdmin)
admin.site.register(GroupUser, GroupUserModelAdmin)
