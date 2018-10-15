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
    console.log(buildings)
    for (var i = 0; i < buildings.length; i++) {
        var option = $('<option></option>');
        option.attr('value', buildings[i]);
        option.text(buildings[i]);
        var ID = '#' + id
        $(ID).append(option);
    }
}