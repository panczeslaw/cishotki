from django.contrib import admin
from .models import Topic, Tag, TShirt, Rate



class RateInline(admin.TabularInline):
	model = Rate
	autocomplete_fields = ("user",)
	extra = 0


@admin.register(TShirt)
class TShirtAdmin(admin.ModelAdmin):
	list_display = ("id", "user", "topic_list", "tags_list",)
	filter_horizontal = ("topic", "tag",)
	autocomplete_fields = ("user",)
	inlines = [
		RateInline,
	]

	def topic_list(self, obj):
		return ", ".join([str(i) for i in obj.topics.all()])
	topic_list.short_description = "Topics"

	def tags_list(self, obj):
		return ", ".join([str(i) for i in obj.tags.all()])
	tags_list.short_description = "Tags"



@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
	pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	pass