from rest_framework import serializers
from .models import Music, Artist, Comment

#위에서 정의되어야 밑에서 쓸수 있기때문에 가장 위로 올림(comment)
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','content',]

# 통역의 역할
class MusicSerializer(serializers.ModelSerializer):
    artist_name = serializers.CharField(source='artist.name') #아티스트 이름으로 보여주기
    comment_set = CommentSerializer(many=True)
    class Meta:
        model = Music
        fields = ['id','title','artist_name','comment_set',]
        
        
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
        
        
