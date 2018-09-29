google.charts.load('current', {'packages':['treemap', 'map']});
google.charts.setOnLoadCallback(drawChart);
function drawChart() {
	var data = google.visualization.arrayToDataTable([
	  ['Location', 'Parent', 'Market trade volume (size)', 'Market increase/decrease (color)'],
	  ['America',   null,             0,                               0],
	  ['Brazil',    'America',            11,                              10],
	  ['USA',       'America',            52,                              31],
	  ['Mexico',    'America',            24,                              12],
	  ['Canada',    'America',            16,                              -23],

	]);

	var geoView = new google.visualization.DataView(data);
	geoView.setColumns([0]);

	var map =  new google.visualization.Map(document.getElementById('map_div'));
	map.draw(geoView, {showTip: true});

	tree = new google.visualization.TreeMap(document.getElementById('tree_div'));

	tree.draw(data, {
	  minColor: '#f00',
	  midColor: '#ddd',
	  maxColor: '#0d0',
	  headerHeight: 15,
	  fontColor: 'black',
	  showScale: true
	});
	google.visualization.events.addListener(tree, 'select', function() {
		map.setSelection(tree.getSelection()); 
	  });

}