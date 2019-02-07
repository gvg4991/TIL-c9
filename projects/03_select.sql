SELECT 영화이름 FROM movies WHERE 상영시간>=150;
SELECT 영화이름,영화코드 FROM movies WHERE 장르=='애니메이션';
SELECT 영화이름 FROM movies WHERE 제작국가=='덴마크' AND '장르'=='애니메이션';
SELECT 영화이름, 누적관객수 FROM movies WHERE 누적관객수>1000000 AND 관람등그=='청소년관람불가';
SELECT * FROM movies WHERE 개봉연도>=20000101 AND 개봉연도<=20091231;
SELECT 영화이름 FROM movies WHERE 상영시간>=150;
SELECT DISTINCT 장르 FROM movies;