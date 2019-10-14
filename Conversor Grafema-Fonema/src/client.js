/*
var ws;
function init(){
	ws = new WebSocket("http://localhost:4444");

	ws.onopen = function() {
		output("Javascript Client Connected");
	};

	ws.onmessage = function(e) {
		var a = document.getElementsByName("phoneme");
		a[0].value = e.data;
	};

	ws.onerror = function(e) {
		output("Error");
		console.log(e);
	};
}

function onSubmit() {
	var input = document.getElementsByName("grapheme");
	ws.send(input[0].value);
	output("Sent:" + input[0].value);
}

function onCloseClick() {
	ws.close();
}

function output(str) {
	console.log(str);
}

function onClick(){
	onSubmit();
}

init();
*/

fetch('/hello')
	.then(function (response) {
			return response.text();
	})
	.then(function (text) {
		console.log('GET response text:');
    console.log(text); // Print the greeting as text
	});

fetch('/hello')
	.then(function (response) {
		return response.json(); // But parse it as JSON this time
	})
	.then(function (json) {
		console.log('GET response as JSON:');
		console.log(json); // Here’s our JSON object
	})
