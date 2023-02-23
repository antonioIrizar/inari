local.build:
	docker-compose build

local.start:
	docker-compose up --build --detach

local.stop:
	docker-compose stop
