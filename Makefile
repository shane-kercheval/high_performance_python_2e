####
# DOCKER
####
docker_build:
	docker compose -f docker-compose.yml build

docker_rebuild:
	docker compose -f docker-compose.yml build --no-cache

docker_run:
	docker compose -f docker-compose.yml up

jupyter:
	open 'http://127.0.0.1:8888/?token=d4484563805c48c9b55f75eb8b28b3797c6757ad4871776d'

zsh:
	docker exec -it high_performance_python_2e-bash-1 /bin/zsh

####
# Project
####
linting:
	flake8 --max-line-length 99 .

main:
	python main.py
