# nexus-app
Serverless app built using AWS Serverless Application Model (SAM). 

## Technologies
1. `python3.9`
1. `API Gateway`
1. `Lambda`
1. `docker`
1. `AWS CLI`
1. `AWS Serverless Application Model (SAM)`
1. `pytest`

## Initial Setup
1. Install dependencies
    - Docker
    - AWS CLI
    - AWS SAM
1. Configure `~/.aws/credentials` with `AWS_ACCESS_KEY_ID` / `AWS-SECRET_ACCESS_KEY`
1. `make build`
1. `make deploy`

## Usage
1. Perform initial setup
1. Create appropriate usage plan and API key
1. Invoke API gateway endpoint(s)

## Testing
1. `make test`
    - runs pytest unit tests
1. `make server`
    - starts local lambda mock server to run integration tests against
1. `make mocktest`
    - runs pytest integration tests with mock server

## Miscellaneous
1. `make format`
    - runs autopep8 + isort across directories
