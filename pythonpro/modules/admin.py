from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from pythonpro.modules.models import Section, Module, Chapter, Topic


class ModuleAdmin(OrderedModelAdmin):
    list_display = 'title slug order move_up_down_links'.split()


class SectionAdmin(OrderedModelAdmin):
    list_display = 'title slug module order move_up_down_links'.split()


class ChapterAdmin(OrderedModelAdmin):
    list_display = 'title slug section order move_up_down_links'.split()


class TopicAdmin(OrderedModelAdmin):
    list_display = 'title slug chapter order move_up_down_links'.split()


admin.site.register(Module, ModuleAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Topic, TopicAdmin)
