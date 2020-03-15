# reactDom.render

`ReactDOM.render(element, container[, callback])`

- element
    - 렌더링할 리액트 엘리먼트
- container
    - 렌더링이 일어날 대상 DOM 노드
- React 엘리먼트를 container DOM에 렌더링하고 컴포넌트에 대한 참조를 반환

<hr/>

```
var dish = React.createElement("h1", null, "구운 연어")

ReactDOM.render(dish, document.getElementbyId('react-container'))
```

제목 엘리먼트를 DOM으로 렌더링하면 HTML에 정의해둔 react-container라는 id를 가지는 div의 자식으로 h1 엘리먼트가 추가됨.

결과는 하단과 같음

```
<body>
    <div id="react-container">
        <h1>구운 연어</h1>
    </div>
</body>
```