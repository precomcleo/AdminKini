(function($) {
    // 日期倒數
    var DateDiff = function (sDate) {
        var fullDate = new Date();
        var yyyy = fullDate.getFullYear();
        var MM = (fullDate.getMonth() + 1) >= 10 ? (fullDate.getMonth() + 1) : ("0" + (fullDate.getMonth() + 1));
        var dd = fullDate.getDate() < 10 ? ("0"+fullDate.getDate()) : fullDate.getDate();
        var todayDate = new Date(yyyy + "/" + MM + "/" + dd);

        var endDate = new Date(sDate);
        var iDays = parseInt(Math.abs(todayDate - endDate) / 1000 / 60 / 60 / 24); // 把相差的毫秒數轉換為天數
        
        //如果已經結束
        if(endDate < todayDate){
            document.getElementById('last-days').style.fontSize = "x-large";
            return "Thank you for joining!";
       }

        return "Last "+ iDays + " Days.";
    };
        
    var GetDateDiff = DateDiff("2021/7/11");
    document.getElementById('last-days').innerText = GetDateDiff;
})(jQuery);