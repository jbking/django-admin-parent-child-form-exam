from django.contrib import admin

from myapp.models import Item, ItemHistory


class ItemAdmin(admin.ModelAdmin):
    pass


class ItemHistoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemHistory, ItemHistoryAdmin)

