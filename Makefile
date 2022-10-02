##################
# AWS SAM commands
##################

build:
	sam build
	
invoke:
	sam local invoke -e events/event.json $(f)

run: build invoke

deploy:
	sam deploy

################
# Test Commands
################
server:
	sam local start-lambda

test:
	pytest -rP

##################
# Utility Commands
##################

clean:
	docker images | grep 'public.ecr.aws' |  xargs docker rmi

format:
	isort nexus/ tests/
	autopep8 nexus/ tests/
