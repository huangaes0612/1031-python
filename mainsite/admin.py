from django.contrib import admin
from mainsite.models import Post, AccessInfo, Branch, StoreIncome, Country, City

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

admin.site.register(Post, PostAdmin)
admin.site.register(AccessInfo)

class BranchAdmin(admin.ModelAdmin):
    list_display = ('title', 'name')
admin.site.register(Branch, BranchAdmin)

class StoreIncomeAdmin(admin.ModelAdmin):
    list_display = ('branch', 'income_year', 'income_month', 'income')
admin.site.register(StoreIncome, StoreIncomeAdmin)

class CountryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
admin.site.register(Country, CountryAdmin)

class CityAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'country', 'population')
admin.site.register(City, CityAdmin)