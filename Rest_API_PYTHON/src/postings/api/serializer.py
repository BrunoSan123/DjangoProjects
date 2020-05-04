from rest_framework import serializers

from postings.models import ApiPost


class ApiPostSerializer(serializers.ModelSerializer):
    url =serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = ApiPost
        fields =[
            'url',
            'pk',
            'user',
            'title',
            'content',
            'timestamp'
        ]
        read_only_field=['user']
        extra_kwargs = {'user': {'required': False}}

    
    def get_url(self,obj):
        request =self.context.get("request")
        return obj.get_api_url(request=request)

    
    def valida_titulo(self,value):
        qs =ApiPost.objects.filter(title__iexact=value)
        if self.instance:
            qs=qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("Title tem que ser unico")
        return value