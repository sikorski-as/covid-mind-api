import datetime

from rest_framework import serializers

from .models import Activity, Category


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=20)
    color = serializers.CharField(max_length=10)

    class Meta:
        verbose_name_plural = 'Categories'
        model = Category
        fields = '__all__'

    def __str__(self):
        return f'{self.name} ({self.color})'


class ActivitySerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    date = serializers.DateField(initial=datetime.date.today)
    categories = CategorySerializer(many=True)
    link = serializers.URLField()

    class Meta:
        model = Activity
        exclude = ['visible']

    def __str__(self):
        return f'{self.title} ({self.date})'
