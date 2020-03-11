# React Element

`React.createElement(type, props?, ...children)`

- type
    - Element의 타입 정의
    - Component Class 혹은 String이 올 수 있음
- props?
    - ? : Typescript의 optional 연산자로서 올 수도 있고 안 올 수도 있음
    - json 타입 혹은 null
- ...children
    - ... : 나머지 연산자
    - 여는 태그와 닫는 태그 사이에 들어가야 할 엘리먼트의 자식 노드

```
React.createElement("h1", null, "제목")

<h1>제목</h1>
```

```
React.createElement("h1", 
    {id:"recipe-0", data-type: "title"},
    "Baked Salmon"
)

<h1 data-reactroot id="recipe-0" data-type="title">Baked Salmon</h1>
```