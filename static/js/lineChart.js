

function drawLine() {


    var resData = $.ajax({
        url: "//localhost:5000/fetch",
        dataType: "json",
        async: false
    }).responseText;
   
    var data = new google.visualization.DataTable();
    data.addColumn('date', 'Time');
    data.addColumn('number', 'kwh');
    data.addColumn('number', 'kvarh');

    resData = JSON.parse(resData)
    for (var obj = 0; obj < resData.length; obj++) {
        if (resData[obj].kvarh >= 0 && resData[obj].kwh >= 0) {
            data.addRow([new Date(resData[obj].timeStamp), resData[obj].kvarh, resData[obj].kwh])
        }
    }
    
    var options = {
    chart: {
        title: 'Box Office Earnings in First Two Weeks of Opening',
        subtitle: 'in millions of dollars (USD)'
    },
    width: 900,
    height: 500
    };

    var line = new google.charts.Line(document.getElementById('curve_line'));

    line.draw(data, google.charts.Line.convertOptions(options));
}

