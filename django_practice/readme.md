Folder 구조에 대한 설명 <br>
shrinkers 폴더 안에 
1. shrinkers folder는 프로젝트 폴더
2. shortner folder는 앱 폴더 

---
<b> DB modeling에 대해서 </b> <br>
어떤 item에 속성 데이터를 사전에 정의하는 것. (data format을 정의)

<b>예시_ job table</b> <br>
|산업|연봉|근무지|
|---|---|---|
|it|2000|seoul|

django modeling에는 id는 기본 값(PK) 자동 정의<br>
왜래키(FK)를 사용하면 뒤에 xxx_id를 자동으로 생성

django 3.0 이상이 되면서 DB column 타입이 다양해짐
- Textfield, EmailField, JsonField 등 다양함
- PK에서 사용되는 타입은 BigAutoField가 되었다고 함 (Auto Incerment) / 원하면 AutoField 사용 가능

---
