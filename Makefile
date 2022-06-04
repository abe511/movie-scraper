# DOCKER COMPOSE
up:
	docker compose up -d
stop:
	docker compose stop
down:
	docker compose down --volumes

# DOCKERFILE (builds python app only)
build:
	docker build -t movie --rm .
run:
	docker run --name movieapp -p 5000:5000 movie
it:
	docker start movieapp
	docker exec -it movieapp bash
clean:
	docker stop movieapp
	docker rm movieapp
fclean:
	docker stop movieapp || true
	docker rm movieapp || true
	docker rmi movie