# react-create-app 으로 프로젝트 시작 시 오류 문제 해결방법

### 오류 화면
![create-react-app-error](/DM/React/images/create-react-app-error.png)

### 발생 상황
Visual Studio Code IDE 툴에서 TERMINAL 을 사용하여 create-react-app을 실행 시 혹은 다른 명령어 사용시 에러

### 오류 메시지  
```
create-react-app : 이 시스템에서 스크립트를 실행할 수 없으므로 ... (중략) ... 파일을 로드할 수 없습니다. 자세한 내용은 about_Execution_Policies(https://go.microsoft.com/fwlink/?LinkID=135170)를 
참조하십시오.
위치 줄:1 문자:1
+ create-react-app simple-todo-list
+ ~~~~~~~~~~~~~~~~
    + CategoryInfo          : 보안 오류: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```

### 해결 방법
1. `Windows PowerShell` 을 `관리자` 로 실행
2. `Get-ExecutionPolicy` 명령어 입력
3. 권한이 `RemoteSigned` 가 아니라면 `Set-ExecutionPolicy RemoteSigned` 를 입력
4. `예(Y)` 입력하여 선택
5. create-react-app 명령어 다시 입력하여 실행되는 것을 확인

### 해결 화면
![create-react-app-troubleshooting](/DM/React/images/create-react-app-troubleshooting.png)