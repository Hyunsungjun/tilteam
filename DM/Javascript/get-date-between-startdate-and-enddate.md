# 시작일과 종료일 사이의 날짜 구하기

```
var diffDate = function(startDate, endDate) {
    var listDate = [];
    var dateMove = new Date(startDate);
    var strDate = startDate;    

    if (startDate == endDate)   // 시작일과 종료일이 같을 경우
    {
        var strDate = dateMove.toISOString().slice(0,10);
        listDate.push(strDate);
    }
    else    // 아닐 경우
    {
        while (strDate < endDate)
        {
            var strDate = dateMove.toISOString().slice(0, 10);
            listDate.push(strDate);
            dateMove.setDate(dateMove.getDate() + 1);
        }
    }
    return listDate;
}

console.log(diffDate('2020-03-25', '2020-03-27'))   // ['2020-03-25', '2020-03-26', '2020-03-27']
```