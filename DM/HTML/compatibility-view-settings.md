# HTML 호환성 보기 설정

```
<meta http-equiv="X-UA-Compatible" content="IE=edge">
```

### content 속성에 적용할 수 있는 값
- IE=5 : 관용모드(quirks mode)로 지정된 DOCTYPE에 상관없이 IE5 렌더링 방식을 사용합니다.
- IE=7 : IE7 표준모드로 지정된 DOCTYPE에 상관없이 IE7 표준 모드 렌더링 방식을 사용합니다.
- IE=EmulateIE7 : IE7 에뮬레이션 모드로 지정된 DOCTYPE에 따라 IE7 표준모드나 관용모드로 렌더링합니다.
- IE=8 : IE8 표준모드로 지정된 DOCTYPE에 상관없이 IE8 표준모드로 렌더링합니다.
- IE=EmulateIE8 : IE8 에뮬레이션 모드로 지정된 DOCTYPE에 따라 IE8 표준모드나 관용모드로 렌더링합니다.
- IE=edge : 최신모드로 지정된 DOCTYPE에 상관없이 IE8 이상 버전에서 항상 최신 표준 모드로 렌더링합니다.

### 가장 보편적으로 사용하는 태그
```
<meta http-equiv="X-UA-Compatible" content="IE=edge, chrome=1">
```
- 익스플로러에서만 작동하며, 최신 버전일때 호환성 보기 없이 페이지를 읽도록 해줍니다.
- 또한, 구형 버전일 시 크롬 프레임을 설치하여 페이지를 제대로 표시할 수 있도록 합니다.