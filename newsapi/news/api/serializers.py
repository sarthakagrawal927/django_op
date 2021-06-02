from rest_framework import serializers
from ..models import Article


class ArticleSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    location = serializers.CharField()
    body = serializers.CharField()
    publication_date = serializers.DateField()
    created_at = serializers.DateField(read_only=True)
    updated_at = serializers.DateField(read_only=True)
    active = serializers.BooleanField()

    def create(self, validated_data):
        print(validated_data)
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get(
            'description', instance.description)

        instance.body = validated_data.get('body', instance.body)
        instance.location = validated_data.get('location', instance.location)

        instance.publication_date = validated_data.get(
            'publication_date', instance.publication_date)

        instance.create_at = validated_data.get(
            'create_at', instance.create_at)

        instance.updated_at = validated_data.get(
            'updated_at', instance.updated_at)

        instance.active = validated_data.get(
            'active', instance.active)
