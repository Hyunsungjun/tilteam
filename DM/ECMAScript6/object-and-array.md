# 객체와 배열

ES6에서는 구조 분해, 객체 리터럴 개선, 스프레드 연산자 등의 객체와 배열을 다루는 방법과 객체와 배열 안에서 변수의 영역을 제한하는 방법을 제공합니다.

[1. 구조 분해를 사용한 대입](#1-구조-분해를-사용한-대입-)   
[2. 객체 리터럴 개선](#2-객체-리터럴-개선-)   
[3. 스프레드 연산자](#3-스프레드-연산자-)
<br/><br/>

---

## 1. 구조 분해를 사용한 대입 [&#128285;](#객체와-배열)  

구조 분해*destructuring*를 사용하면 객체 안에 있는 필드 값을 원하는 변수에 대입할 수 있습니다.

sandwich를 분해해서 bread, meat 필드를 같은 이름의 변수를 넣어줍니다. 두 변수의 값은 sandwich에 있는 같은 이름의 필드 값으로 초기화 되지만, 두 변수를 변경해도 원래의 필드 값은 바뀌지 않습니다.

```
var sandwich = {
    bread : "식빵",
    meat : "소시지",
    cheese: "체다",
    toppings: ["상추", "토마토", "머스타드"]
}

var {bread, meat} = sandwich

console.log(bread, meat)    // 식빵 소시지

bread = "플랫 브레드"
meat = "닭가슴살"

console.log (bread, meat)   // 플랫 브레드 닭가슴살

console.log (sandwich.bread, sandwich.meat) // 식빵 소시지
```

객체를 분해해서 함수의 인자로 넘길 수도 있습니다.

```
var notify = person => {
    console.log(`그녀의 이름은 ${person.firstname} 입니다.`)
}

var person = {
    firstname: "다미",
    lastname: "최"
}

notify(person)  // 그녀의 이름은 다미 입니다.

// 객체의 필드에 접근하기 위해 점`.`과 같은 필드 이름을 사용하는 대신 `person`에서 값을 구조 분해로 가져올 수도 있습니다.

var notify = ({person}) => {
    console.log(`그녀의 이름은 ${firstname}`)
}

console.log(person) // 그녀의 이름은 다미
```

배열을 구조해서 원소의 값을 변수에 대입할 수도 있습니다.  
불필요한 값을 콤마`,`를 사용해 생략하는 리스트 매칭*list matching*을 사용할 수도 있습니다. 무시하고 싶은 원소 위치에 콤마를 넣으면 리스트 매칭됩니다.
```
var [first] = ["가", "나", "다"]
console.log(first)  // 가

var [,,third] = ["가", "나", "다"]
console.log(third)  // 다
```
<br/><br/>

---

## 2. 객체 리터럴 개선 [&#128285;](#객체와-배열)  
객체 리터럴 개선*object literal enhancement*은 구조 분해의 반대라 할 수 있습니다.객체 리터럴 개선은 구조를 다시 만들어내는 과정 또는 내용을 한데 묶는 과정이라 할 수 있습니다.  
객체 리터럴 개선을 사용하면 현재 영역에 있는 변수를 객체의 필드로 묶을 수 있습니다.

```
var name = "한라산"
var elevation = 1950

var hike = {name, elevation}

console.log(hike)   // {name: "한라", elevation: 1950}
```

객체 리터럴 개선 또는 객체 재구축으로 객체 메서드를 만드는 것도 가능합니다.
객체 메서드를 정의할 때는 더 이상 function 키워드를 사용하지 않아도 됩니다.

```
const skier = {
    name,
    sound,
    powderYell() {
        let yell = this.sound.toUpperCase()
        console.log(`${yell} ${yell} ${yell}`)
    },
    speed(mph) {
        this.speed = mph
        console.log('속력(mph):', mph)
    }
}
```
<br/><br/>

---

# 3. 스프레드 연산자 [&#128285;](#객체와-배열)  
스프레드 연산자*spread operator* 는 세 개의 점`...` 으로 이루어진 연산자 입니다.

먼저 스프레드 연산자를 사용해 배열의 내용을 조합할 수 있습니다.
```
var peaks = ["대청봉", "중청봉", "소청봉"]
var canyons = ["천불동계곡", "가야동계곡"]
var seoraksan = [...peaks, ...canyons]

console.log(seoraksan.join(',')) // 대청봉,중청봉,소청봉,천불동계곡,가야동계곡
```

스프레드 연산자를 사용하면 원본 배열을 변경하지 않고 복사본을 만들어 뒤집을 수 있습니다.
```
// Array.reverse 사용 시

var peaks = ["대청봉", "중청봉", "소청봉"]
var [last] = [...peaks].reverse()

console.log(last)   // 소청봉
console.log(peaks.join(','))    // 대청봉,중청봉,소청봉
```

스프레드 연산자를 사용해 배열의 나머지 원소를 얻을 수도 있습니다.

```
var peaks = ["대청봉", "중청봉", "소청봉"]
var [first, ...rest] = peaks

console.log(rest.join(',')) // 중청봉,소청봉
```

스프레드 연산자를 객체에 사용할 수도 있습니다.

```
var morning = {
    breakfast: "미역국",
    lunch: "삼치구이와 보리밥"
}

var dinner = "스테이크 정식"

var backpackingMeals = {
    ...morning,
    dinner
}

console.log(backpackingMeals)   // {breakfast: "미역국", lunch: "삼치구이와 보리밥", dinner: "스테이크 정식"}
```