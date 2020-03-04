# Classes
class 문법에는 class 표현식과 class 선언 두가지 방법이 있다.

[1. class 선언](#1-class-선언-)   
[2. class 표현식](#2-class-표현식-)   
[3. constructor](#3-constructor-)
<br/><br/>

---

## 1. class 선언 [&#128285;](#class-선언)  
class를 정의하는 한 가지 방법은 class 선언을 이용하는 것입니다. class를 선언하기 위해서는 클래스의 이름과 함께 class 키워드를 사용해야 합니다.

```
class Polygon {
    constructor(height, width) {
        this.height = height;
        this.width = width;
    }
}
```

함수 선언과 달리 클래스 선언은 호이스팅(Hoisting)이 일어나지 않기 때문에, 클래스를 사용하기 위해서는 먼저 선언을 해야합니다. 그렇지 않으면 `ReferenceError` 가 발생합니다.

```
const p = new Person()  // ReferenceError

class Person {

}
```
<br/><br/>

---

## 2. class 표현식 [&#128285;](#class-선언)
class 표현식은 class를 정의 하는 다른 방법입니다. Class 표현식은 이름을 가질 수도 있고, 갖지 않을 수도 있습니다. 이름을 가진 class 표현식의 이름은 클래스의 body에 대해 local scope에 한해 유효합니다.

```
const Person = class Person {
    constructor(name) {
        this.name = name;
    }

    introduce() {
        console.log('My name is ' + this.name);
    }
}

const Person = class {
    constructor(name) {
        this.name = name;
    }

    introduce() {
        console.log('My name is ' + this.name);
    }
}
```
<br/><br/>

---

## 3. constructor [&#128285;](#class-선언)

constructor는 클래스 인스턴스를 생성하고 생성한 인스턴스를 초기화하는 역할을 합니다. new Person() 코드를 실행하면 Person.prototype.constructor가 호출됩니다. 이를 default constructor라고 하며 constructor가 없으면 인스턴스를 생성할 수 없습니다.

```
const Person = class Person {
    constructor(name) {
        this.name = name;
    }

    introduce() {
        console.log('My name is ' + this.name);
    }
}

const person = new Person('CHOIDAMI');
```

>**호출된 constructor가 인스턴스를 생성하여 반환하면 new 연산자가 받아 new를 실행한 곳으로 반환하는 과정은 다음과 같습니다.**
>1. new Person('CHOIDAMI')을 실행  
>2. new 연산자가 constructor를 호출하면서 파라미터 전달  
>3. constructor에 작성한 코드를 실행하기 전에 빈 Object 를 생성  
>4. constructor 코드를 실행  
>5. 생성한 Object(인스턴스)에 property 할당 (인스턴스를 먼저 생성했기 때문에 this로 Object 참조 가능
>6. 생성한 Object 반환