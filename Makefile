build:
	docker-compose build

up:
	docker-compose up

sh:
	docker-compose exec app-consumer bash

consumer:
	docker-compose exec app-consumer bash -c "python3 src/consumer.py"

producer:
	docker-compose exec app-consumer bash -c "python3 src/producer.py"