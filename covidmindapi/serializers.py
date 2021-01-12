import datetime

from rest_framework import serializers

from .models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    date = serializers.DateField(initial=datetime.date.today)
    categories = serializers.SerializerMethodField(read_only=True)

    def get_categories(self, instance):
        return [category.name for category in instance.categories.all()]

    link = serializers.URLField()

    class Meta:
        model = Activity
        exclude = ['visible']

    def __str__(self):
        return f'{self.title} ({self.date})'
