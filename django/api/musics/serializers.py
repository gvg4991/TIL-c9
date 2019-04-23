from rest_framework import serializers
from .models import Music, Artist, Comment


# 통역의 역할
class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['id','title','artist',]
        
        
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id','name',]
        
        
# 아티스트와 맺어진 1:N 모든 음악 정보를 가지고옴        
class ArtistDetailSerializer(serializers.ModelSerializer):
    music_set = MusicSerializer(many=True) #music_set은 정해져있는 이름, 시리얼라이저 되어있지 않아 따로 정의해줘야됨!
    class Meta:
        model = Artist
        fields = ['id','name', 'music_set',]
        
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','content',]