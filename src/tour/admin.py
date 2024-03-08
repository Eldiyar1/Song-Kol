from django.contrib import admin

from tour.models import (
    TourDates,
    TourProgram,
    Tips,
    Price,
    TourAdd,
    BookingGroupTour,
    BookingPrivateTour,
    PriceDetail, Location,
    TourProgramDay,
    Image
)

admin.site.register(Image)
admin.site.register(TourDates)
admin.site.register(TourProgram)


class PriceDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'person', 'per_person', 'in_com')
    list_display_links = ('id', 'per_person')
    readonly_fields = ('in_com',)


class LocationInline(admin.StackedInline):
    model = Location
    extra = 1


class PriceInline(admin.StackedInline):
    model = Price
    extra = 1


class TipsInline(admin.StackedInline):
    model = Tips
    extra = 1


class TourDatesInline(admin.StackedInline):
    model = TourDates
    extra = 1


class PriceDetailInline(admin.TabularInline):
    model = PriceDetail
    extra = 1


class ImageInline(admin.TabularInline):
    model = Image
    extra = 5


@admin.register(TourAdd)
class TourAdmin(admin.ModelAdmin):
    model = TourAdd
    inlines = (
        PriceInline,
        LocationInline,
        TipsInline,
        TourDatesInline,
        PriceDetailInline,
        ImageInline,
    )


admin.site.register(BookingGroupTour)
admin.site.register(BookingPrivateTour)
admin.site.register(PriceDetail, PriceDetailsAdmin)
admin.site.register(TourProgramDay)
