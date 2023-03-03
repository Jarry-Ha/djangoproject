from django.contrib import admin

from .models import Choice, Question

# # 기본
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

# # 상세 표 나누기
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]

# QuestionAdmin에 ChoiceInline 추가하기
# class ChoiceInline(admin.StackedInline): # Stack형
class ChoiceInline(admin.TabularInline): # Tabular형 - 더 조밀함
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # 선택적 추가요소들
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')    
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice) # QuestionAdmin에 포함
