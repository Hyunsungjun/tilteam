#include <stdio.h>
#include <string.h>

//학생 정보를 저장하는 student 구조체를 정의합니다.

struct student
{
    char name;
    int age;
 };


int main()
{
    //학생 3명의 정보를 저장할 student를 선언하며 값을 초기화합니다.
    //김하하 17, 박호호 19, 최히히 18
    struct student s1 = {"김하하",17};
    struct student s2 = {"박호호",19};
    struct student s3 = {"최히히",18};
    
    //세 학생의 정보를 차례대로 출력합니다. 각 학생의 정보는 줄내림으로 구분합니다.
    for(char s=1;s<=3;s++)
    {
        printf("%c",s);
    }
  
}