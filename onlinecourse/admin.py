from django.contrib import admin
# Neue Modelle importieren
from .models import Course, Lesson, Instructor, Learner, Enrollment, Question, Choice, Submission

# Für Inline-Bearbeitung von Lesson im Kurs
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

# 🔹 Neue Inlines für Frage & Auswahl
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

# Registrierung
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Enrollment)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
