var Docker = require('dockerode');
var dk = new Docker({
		host : '192.168.59.103',
		port : 2375
	});

exports.list = function (cb) {
	dk.listContainers({
		all : true
	}, cb);
}

listx = function () {
	dk.listContainers({
		all : true
	}, function (err, containers) {
		console.log('ALL: ' + containers.length);
		containers.forEach(function (c) {
			console.log(c);
		});
	});
}

listz = function (data) {
    this.data = data;
    this.callback = function (err, containers) {
		console.log('ALL: ' + containers.length);
		containers.forEach(function (c) {
			console.log(c);
            this.data.push(c);
		});
	}
    
	dk.listContainers({
		all : true
	}, this.callback);
}
