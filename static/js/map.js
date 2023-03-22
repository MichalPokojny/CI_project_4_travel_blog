function initMap(){
    var map = new google.maps.Map(document.getElementById("map"), {
        zoom: 2, 
        center: {
            lat:17.619261,
            lng:-10.134766
        }
    });
    
    var labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZW";
    
    var locations = [
        {lat: -12.046374, lng:-77.042793},
        {lat: -13.163068, lng:-72.545128},
        {lat: -33.447487, lng:-70.673676},
        {lat: -34.603722, lng:-58.381592},
        {lat: -34.901112, lng:-56.164532},
        {lat: -22.908707, lng:-68.199716},
        {lat: -3.731862, lng:-38.526669},
        {lat: -12.974722, lng:-38.476665},
        {lat: 53.350140, lng:-6.266155},
        {lat: 51.509865, lng:-0.118092},
        {lat: 43.675819, lng:7.289429},
        {lat: 46.204391, lng:6.143158},
        {lat: 49.6106, lng:6.1328},
        {lat: 51.165691, lng:10.451526},
        {lat:40.416775, lng:-3.703790},
        {lat:38.736946, lng:-9.142685}
        
    ];
    
    var markers = locations.map(function(location, i) {
        return new google.maps.Marker({
            position: location,
            label: labels[i % labels.length]
        });
    });
    
    var markerCluster = new MarkerClusterer(map, markers,
        { imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m' });
    }