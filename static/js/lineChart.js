var B = null

function drawLine(building) {
    B = building
    var resData = $.ajax({
        url: "fetch/"+building+"/2018-03-01 14:30/2018-03-01 20:00",
        dataType: "json",
        async: false
    }).responseText;

    var data = new google.visualization.DataTable();
    data.addColumn('date', 'Time (hours)');
    data.addColumn('number', 'kVArh');
    data.addColumn('number', 'kWh');

    resData = JSON.parse(resData)
    for (var obj = 0; obj < resData.length; obj++) {
        if (resData[obj].kvarh >= 0 && resData[obj].kwh >= 0) {
            data.addRow([new Date(resData[obj].timeStamp), resData[obj].kvarh, resData[obj].kwh])
        }
    }
    
    var options = {
    chart: {
        title: 'Electricity Consumption of ' + building + ' in the last 24 hours',
        subtitle: 'Total number of occupants: N/A' + '\t Cost: R--,--'
    }
    };

    var line = new google.charts.Line(document.getElementById('curve_line'));

    line.draw(data, google.charts.Line.convertOptions(options));
}

$(window).resize(function () {
    drawLine(B);
});
