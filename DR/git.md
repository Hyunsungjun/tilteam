```
git_branch_생성_확인_삭제_변경_다른브랜치연결

#
깃 접속 git init
깃 연결 git remote add origin 깃주소
깃 가져오기 git clone
깃 전체 파일 추가하기 git add .

# 커밋 3단계
vscode에서
1. 스테이지에 파일 올리고
2. 커밋메시지 적은다음 컨트롤 엔터로 커밋하고
3. 푸쉬해줘야 깃에 올라감

파일 추가 git add 파일명
커밋 git commit -m "메세지"
푸쉬 git push -u origin master

# git에 commit후 push 하려하는데 오류메세지 : can't push refs to remote. try running 'pull' first to integrate your changes
1. git remote add origin 깃주소
2. git pull origin master
3. git push origin master
해결 : pull 한다음 push 하면 성공


# 깃헙 브랜치 생성 및 확인

깃 클론
https://github.com/깃주소

깃 이름,이메일 변경 
git config --global user.name 내이름
git config --global user.email 내이메일@gmail.com

나의 브랜치 경로 확인 (master로 되어있음)
git branch

새로운 브랜치 저장소 생성
git checkout -b 브랜치명

나의 브랜치 경로 확인 (브랜치명 으로 되어있음)
git branch

생성한 브랜치저장소를 원격 저장소에(깃헙) 푸쉬
git push origin 브랜치명

원격저장소 리스트 목록을 업데이트
git fetch -p origin

원격저장소 리스트 확인 (브랜치명 이 리스트에 업데이트 되어있는것을 볼수있음)
git branch -r



# 브랜치 원격저장소를 삭제하고 싶으면
   우선 나의 브랜치 경로가 마스터에 있어야함

마스터로 브랜치 이동 
git checkout 브랜치명

마스터 브랜치로 이동을 잘 했는지 확인
git branch

원격저장소 삭제
git push origin --delete 브랜치명
git push origin :브랜치명

로컬브랜치 삭제
git branch -D 브랜치명



# 로컬브랜치 및 원격브랜치 목록을 전체 확인할수 있음
git branch -a


# 브랜치 이름 변경하기
git branch -m 기존이름 새로운이름

# 다른사람의 브랜치를 내 프로젝트에 가져오기
git pull origin 다른브랜치명

가져와서 내 파일 수정하고 나의 원격브랜치에(브랜치명 에) 푸쉬해서 업데이트
git push origin 브랜치명


마지막으로 깃헙에서 푸쉬 잘 되어있는지 확인하고
잘되었으면 성공!



* 여기에도 브랜치 코드가 정리 잘되어있음 https://www.tuwlab.com/ece/22216






# 다른 사람의 브랜치를 내 프로젝트에 가져오기 (병합)
git pull origin 다른브랜치명

가져왔는데 다른사람이 만든 파일이 추가되어있으면
vscode에서 소스컨트롤에 staged changes에 다른사람이 작업한 새로운 파일이 뜨고

가져왔는데 다른사람 파일명하고 내 파일명이 동일하지만 코드 내용이 다르면
vscode에서 소스컨트롤에 merge changes에 동일한 파일이 있음

동일한 파일명을 클릭해보면 변경된걸 합칠수있는 옵션이 네가지로 뜨는데
이렇게 -> accept current change  /  accept incoming change  / accept both changes / compare changes
먼저 compare 을 누르면 내파일하고 다른사람의 파일이 어떤부분이 수정되어있는지 확인할 수 있음
그리고 current 를 누르면 내 파일로 적용하고
incoming 을 누르면 다른사람파일로 바꾸고
both를 누르면 모든 변경된 사항을 수락하는 내용임

3개중에 선택해서 저장하고 다시 스테이지에 파일 올리고 커밋하면 됨

혹시 잘못 눌러서 머지를 취소하고싶으면 다른사람의 저장소를 pull로 받아오기 전으로 취소됨
git merge --abort



# 기존에 있던 브랜치에서 새로운 브랜치를 연결해서 생성하려면
git checkout -b 새로운브랜치명 -f 기존브랜치명

# 다른 브랜치에서 커밋된 헤드에서 브랜치를 연결해서 생성하려면
git checkout -b 새로운브랜치명 -f 헤드아이디 입력하거나 헤드에 있던 태그를 입력

# 헤드에 연결된 브랜치 리스트 목록 확인
git log --graph --full-history --all --color --pretty=format:"%x1b[31m%h%x09%x1b[32m%d%x1b[0m%x20%s"

위에 명령어가 너무 길어서 윈도우 cmd명령어로 등록해두면 편함 (난 bl로 등록할 예정 (branch log))
git config --global alias.bl 'git log --graph --full-history --all --color --pretty=format:"%x1b[31m%h%x09%x1b[32m%d%x1b[0m%x20%s"'

이제 git bl 을 입력하면
헤드에 브랜치된 브랜치들 목록이 쭉 나오면 성공!


