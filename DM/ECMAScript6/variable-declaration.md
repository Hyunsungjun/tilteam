# 변수 선언
ES6 이전에는 `var` 키워드가 변수를 선언하는 유일한 방법이었습니다. ES6 부터는 `const`, `let`, `var`을 사용합니다.

[1. const](#1-const-)   
[2. let](#2-let-)   
<br/><br/>

---

## 1. const [&#128285;](#변수-선언)  
상수(constant)는 값을 변경할 수 없는 변수입니다. 상수에 값을 재설정 하는 것은 불가능하며, 값을 변경하려 하면 콘솔 오류가 발생합니다.

```
const pizza = true
pizza = false   // Error
```
<br/><br/>

---

## 2. let [&#128285;](#변수-선언)  
let 키워드를 사용하면 변수 영역을 코드 블록 안으로 한정시킬 수 있습니다. 그러므로 글로벌 변수의 값을 보호할 수 있습니다.

```
function test() {
    let x = "a"
    if (true) {
        let x = "b"
        console.log(x);  // b
    }
    console.log(x);     // a
}
```
