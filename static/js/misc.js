function getChartTypes(id) {

    var graphs = $.ajax({
        url: "fetchGraphTypes",
        dataType: "json",
        async: false
    }).responseText;
    
    graphs = JSON.parse(graphs)
    
    for (var i = 0; i < graphs.length; i++) {
        var option = $('<option></option>');
        option.attr('value', graphs[i][1]);
        
        option.text(graphs[i][0]);
        var ID = '#' + id
        $(ID).append(option);
    }
}

function getBuildings(id) {
    var buildings = $.ajax({
        url: "fetchBuildings",
        dataType: "json",
        async: false
    }).responseText;

    buildings = JSON.parse(buildings)
    for (var i = 0; i < buildings.length; i++) {
        var option = $('<option></option>');
        option.attr('value', buildings[i]);
        option.text(buildings[i]);
        var ID = '#' + id
        $(ID).append(option);
    }
}
var Ranks = 0;
function getBuildingRanking() {
    var ranks = $.ajax({
        url: "ranking",
        dataType: "json",
        async: false
    }).responseText;

    Ranks = ranks;
    
}

function printBuildings(option) {
    ranks = Ranks
    ranks = JSON.parse(ranks)
    if (option == 0) {
        worst = ranks.Worst
        for (var i = 0; i < worst.length; i++) {
            document.write('<a href="javascript:drawLine(\'' + worst[i].building  +'\')" class="list-group-item  breadcrumb">' + worst[i].building + '<span class="badge">' + worst[i].average + ' kwh</span></a>')
        }
    } else if (option == 1) {
        best = ranks.Best
        for (var i = 0; i < best.length; i++) {
            document.write('<a href="javascript:drawLine(\''+ best[i].building + '\')" class="list-group-item  breadcrumb">' + best[i].building + '<span class="badge">' + best[i].average + ' kwh</span></a>')
        }
    }
}