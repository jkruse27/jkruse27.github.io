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
