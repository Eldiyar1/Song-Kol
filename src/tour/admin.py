from django.contrib import admin

from tour.models import (
    TourDates,
    TourProgram,
    Tips,
    Price,
    Photo,
    TourAdd,
    BookingGroupTour,
    BookingPrivateTour,
    PriceDetail, Location,
    TourProgramDay
)


class PriceDetailsAdmin(admin.ModelAdmin):
    list_display = "id person in_com per_person".split()
    list_display_links = "id per_person".split()


class TourProgramInline(admin.StackedInline):
    model = TourProgram
    extra = 0


class LocationInline(admin.StackedInline):
    model = Location
    extra = 0


class PriceInline(admin.StackedInline):
    model = Price
    extra = 1


class TipsInline(admin.StackedInline):
    model = Tips
    extra = 0


class TourDatesInline(admin.StackedInline):
    model = TourDates
    extra = 0


class PriceDetailInline(admin.TabularInline):
    model = PriceDetail
    extra = 0


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1


@admin.register(TourAdd)
class TourAdmin(admin.ModelAdmin):
    model = TourAdd
    inlines = (
        PriceInline,
        TourProgramInline,
        LocationInline,
        TipsInline,
        TourDatesInline,
        PriceDetailInline,
        PhotoInline,
    )


admin.site.register(BookingGroupTour)
admin.site.register(BookingPrivateTour)
admin.site.register(PriceDetail, PriceDetailsAdmin)
admin.site.register(TourProgramDay)
