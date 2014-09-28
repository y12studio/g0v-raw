var Docker = require('dockerode');
var dk = new Docker({
		host : '192.168.59.103',
		port : 2375
	});

function listContainers() {
	dk.listContainers({
		all : true
	}, function (err, containers) {
		console.log('ALL: ' + containers.length);
		containers.forEach(function (c) {
			console.log(c);
		});
	});
}

function runContainer() {
	copt = {
		"Image" : 'y12docker/g0v-ivod'
	}
	dk.createContainer(copt, function (err, container) {
		if (err) {
			console.log(err);
		} else {
			console.log(container);
			// [Docker Remote API v1.13 - Docker Documentation](https://docs.docker.com/reference/api/docker_remote_api_v1.13/#create-a-container)
			sopt = {
				"PortBindings" : {
					"9680/tcp" : [{
							"HostIp" : "0.0.0.0",
							"HostPort" : "9680"
						}
					]
				}
			}

			container.start(sopt, function (err, data) {
				console.log(err == null ? data : err);
			});

		}

	});
}
runContainer();
listContainers();
