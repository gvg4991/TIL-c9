from django.shortcuts import render, get_object_or_404
from .models import Music, Artist, Comment
from rest_framework.decorators import api_view
from .serializers import MusicSerializer, ArtistSerializer, ArtistDetailSerializer, CommentSerializer
from rest_framework.response import Response

@api_view(['GET']) #리스트 안의 요청으로만 처리하겠다
def music_list(request):
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True) #music이 많이 들어있단걸 알려줘야함(리스트 생김)
    return Response(serializer.data) #serializer.data에 정보가 들어가 있음
    
    # Serializer : return 데이터를 문자형을 뽑아서 정리된 형태로 반환
    
    
@api_view(['GET'])
def music_detail(request,music_id): #url의 동적주소에 1이 들어오면 music_id에 1이 들어옴
    music = get_object_or_404(Music,id=music_id) #music 하나만 들어있어서 many=True 안해줘도됨
    serializer = MusicSerializer(music)
    return Response(serializer.data)
    
    
@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists,many=True)
    return Response(serializer.data)
    

@api_view(['GET'])  
def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    serializer = ArtistDetailSerializer(artist)
    return Response(serializer.data)
    
    
@api_view(['POST'])  
def comment_create(request, music_id):
    serializer = CommentSerializer(data=request.data) #시리어즈에 있는 현재의 데이터를 가지고와서 작성
    if serializer.is_valid(raise_exception=True): # 요청이 잘못됐는지 이 줄에서 알려줌
        serializer.save(music_id=music_id)
        return Response(serializer.data)
        
        
@api_view(['PUT','DELETE'])    
def comment_update_and_delete(request, music_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id) # 댓글 오브젝트를 하나 가지고옴
    if request.method == 'PUT':
        serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message':'수정 완료'})
    else: #delete라면
        comment.delete()
        return Response({'message':'삭제 완료'}) #삭제되어 보여 줄 정보가 없음