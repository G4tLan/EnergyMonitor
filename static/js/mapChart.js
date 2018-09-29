google.charts.load('current', {
  'packages': ['map']
});
google.charts.setOnLoadCallback(drawChart);
function drawChart() {
	/*
	var data = google.visualization.arrayToDataTable([
	  ['Lat', 'Long', 'Name', 'Energy Usage'],
	  [-26.191284, 28.026925, 'Chamber of Mines', 1300],
	  [-26.190574, 28.025481, 'Wits Science Stadium', 200],
	  [-26.192531, 28.030572, 'Senate House', 2500],
	  [-26.189874, 28.030797, 'The matrix', 2000]
	]);*/
	
	 var data = google.visualization.arrayToDataTable([
          ['Country', 'Popularity'],
          ['Germany', 200],
          ['United States', 300],
          ['Brazil', 400],
          ['Canada', 500],
          ['France', 600],
          ['RU', 700]
        ]);
	
	var options = {};
	var map = new google.visualization.Map(document.getElementById('map_view'));
	map.draw(data, options);
}
