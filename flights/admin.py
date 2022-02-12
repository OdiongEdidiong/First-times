from django.contrib import admin
from .models import Classes, entry,students,book,airport,flights
# Register your models here.
admin.site.register(Classes)
admin.site.register(entry)
# admin.site.register(students)##
# to create the table in the site
# 1 make migrations
# 2 migrate
# 3 sqlmigrate "name of app" and "migration code"(to see the sql code of the class)
 
def delete_student(modeladmin, request, queryset):
    for student in queryset:
        class_= student.class_name
        class_.no_of_studs -= 1
        student.delete()
        class_.save()

@admin.register(students)
class studentinfo(admin.ModelAdmin):
    list_display = ["Name","class_name"]
    ordering = ["Name"]
    actions = [delete_student]


def Update(modeladmin, request, querySet):
    for book in querySet:
        if book.published == "yes":
            book.published = "no"
        else:
            book.published = "yes"
        book.save()


@admin.register(book)
class books(admin.ModelAdmin):
    list_display = ["Name","published"]
    ordering = ["Name"]
    actions = [Update]

admin.site.register(flights)
admin.site.register(airport)