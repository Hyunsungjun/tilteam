# Arrow Function (화살표 함수)
> 다음 내용들은 [ECMAScript 2015 Language Specification](http://www.ecma-international.org/ecma-262/6.0/#sec-arrow-function-definitions) 을 참조하여 작성하였습니다.

화살표 함수는 `=>` 문법을 사용하는 축약형 함수이며 익명 함수입니다.  
Arrows는 표현식의 결과 값을 반환하는 표현식 본문(expression bodies)뿐만 아니라 상태 블럭 본문(statement block bodies)도 지원합니다.  
하지만 일반 함수의 자신을 호출하는 객체를 가리키는 `dynamic this`와 달리 arrows 함수는 코드의 상위 스코프(lexical scope)를 가리키는 `lexical this`를 가집니다.
  
[1. 문법](#1-문법-)   
[2. this](#2-this-)   
[3. 제약사항](#3-제약사항-)

<br/><br/>

---

## 1. 문법 [&#128285;](#Arrow-Function-화살표-함수)

기존 함수에서 function을 지우고 괄호 `()` 오른쪽에 화살표 `=>` 를 넣어줍니다.

**기존 함수**
```
var hello = function() {
  return "Hello World!";
}
```

**Arrow Function**
```
var hello = () => {
  return "Hello World!";
}
```

`return` 과 괄호 `{}` 를 생략하여 더 짧게 코드를 작성할 수 있습니다.
```
var hello = () => "Hello World!";
```

---

매개변수가 없을 경우에는 괄호가 필요합니다.
```
() => {}
```

매개변수가 하나일 경우에는 괄호를 생략할 수 있습니다.

```
(singleParam) => {}
singleParam => {}
```

---
## 2. this [&#128285;](#Arrow-Function-화살표-함수)

화살표 함수가 제안되기 전까지 모든 자바스크립트 함수는 그 함수를 위한 `this`라는 '내장' 객체가 바인드되어 있고 사용할 수 있었습니다.
하지만 화살표 함수는 자기 자신의 `this`가 바인드되지 않도록 설계되어 있습니다. 또한, 함수안의 `this`는 항상 상위 scope의 `this`를 가리키며, 이를 `Lexical This`라고 합니다.

```
const Person = () => {
  this.age = 0;
  console.log(this.age) // 0
  
  setTimeout(() => {
    this.age++;
    console.log(this.age);  // 1
  }, 1000);
}

Person();
```

---

## 3. 제약사항 [&#128285;](#Arrow-Function-화살표-함수)
여러가지 장점들이 있지만, 이미 언급했던 제약사항들 때문에 화살표 함수는 다음 상황에서는 사용하면 안 됩니다.

>1. 생성자(constructor)
>2. 프로토타입을 이용한 함수 정의
>3. 객체 메소드

화살표 함수를 객체 메소드로 사용하지 말아야 하는 이유는 제대로 된 this나 super를 이용할 수 없기 때문입니다.
생성자나 프로토타입과 같이 아예 사용할 수 없는 것과는 차이가 있습니다.
