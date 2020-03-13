# caps lock 체크
대소문자를 가리는 비밀번호 입력 시 caps lock이 눌려있는지 모를 때가 있습니다.  
(IE의 경우 자동 체크 되지만, Chrome의 경우 체크되지 않습니다.)

이럴 경우, keypress 이벤트를 이용하여 caps lock 감지하여 알려주면 유용합니다.

```
// html
<input type="password" value="" onkeypress="capsLock(this)">

// js
function capsLock(e){
  var keyCode = 0;
  var shiftKey=false;
  keyCode=e.keyCode;
  shiftKey=e.shiftKey;

  if (((keyCode >= 65 && keyCode <= 90)&& !shiftKey)||((keyCode >= 97 && keyCode <= 122)&& shiftKey))
  {
    alert("CapsLock이 켜져 있습니다");
    return;
  }
}
```
