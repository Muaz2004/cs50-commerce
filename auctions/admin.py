from django.contrib import admin
from .models import active_lising, bids, comment,Watchlist


admin.site.register(active_lising)
admin.site.register(bids)
admin.site.register(comment)
admin.site.register(Watchlist)
