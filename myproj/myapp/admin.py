from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from myapp.models import Item, ItemHistory


class ItemAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'add_history',
    ]

    def add_history(self, item):
        return format_html(
            '<a href="{}?{}">click</a>',
            reverse('admin:myapp_itemhistory_add'),
            # give the id with foreign key name `item`
            urlencode({'item': item.id}),
        )


class ItemHistoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemHistory, ItemHistoryAdmin)

