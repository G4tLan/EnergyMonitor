google.charts.load('current', {
  'packages': ['map']
});
google.charts.setOnLoadCallback(drawChart);
function drawChart() {
	var data = google.visualization.arrayToDataTable([
	  ['Lat', 'Long', 'Name'],
	  [-26.191284, 28.026925, 'Chamber of Mines'],
	  [-26.190574, 28.025481, 'Wits Science Stadium'],
	  [-26.192531, 28.030572, 'Senate House'],
	  [-26.189874, 28.030797, 'The matrix']
	]);

	var map = new google.visualization.Map(document.getElementById('map_view'));
	map.draw(data, {
	  showTooltip: true,
	  showInfoWindow: true
	});
}
