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

##################
# Utility Commands
##################

clean:
	docker images | grep 'public.ecr.aws' |  xargs docker rmi

