from django.contrib import admin
from .models import OrgCategories, OrgSubCategories, OrgZone

# Register your models here.
class OrgCategoriesAdmin(admin.ModelAdmin):

    list_display = ['category', 'description', ]

    class Meta:
        model = OrgCategories
admin.site.register(OrgCategories, OrgCategoriesAdmin)

class OrgSubCategoriesAdmin(admin.ModelAdmin):

    list_display = ['sub_category', 'category', 'description', ]

    class Meta:
        model = OrgSubCategories
admin.site.register(OrgSubCategories, OrgSubCategoriesAdmin)

class OrgZoneAdmin(admin.ModelAdmin):

    list_display = ['zone', 'sub_category', 'description', ]

    class Meta:
        model = OrgZone
admin.site.register(OrgZone, OrgZoneAdmin)