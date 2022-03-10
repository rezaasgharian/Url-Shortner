from rest_framework import serializers

from main.models import ShortURL


class ShortURLSerializer(serializers.ModelSerializer):
    alias = serializers.SerializerMethodField()

    class Meta:
        model = ShortURL
        fields = (
            'url', 'alias', 'times_accessed', 'accessed_at', 'created_at'
        )

        read_only_fields = (
            'times_accessed', 'accessed_at', 'created_at'
        )

    def get_alias(self, short_url):
        request = self.context['request']
        hostname = request.META['HTTP_HOST']
        return f'{request.scheme}://{hostname}/r/?id={short_url.short_id}'

    def create(self, validated_data):
        request = self.context['request']

        if request.user.is_authenticated:
            author = request.user
        else:
            author = None

        return ShortURL.objects.create(
            author=author,
            **validated_data,
        )



