# Project to reproduce issue in [aws-lambda-powertools-python](https://github.com/awslabs/aws-lambda-powertools-python)

Related Issue: https://github.com/awslabs/aws-lambda-powertools-python/issues/1098

The project creates two HTTP API endpoints:
* GET - /pets/{name}
* GET - /pets/{name}/vets

The Lambda function uses the aws-lambda-powertools-python layer.

Calling `GET /pets/{name}` or `GET /pets/{name}/vets` should return a successful response with status code 200 when called with _"Chester Mall"_ or _"Chester%20Mall"_ (without ") as `name`.

Instead of a successful response a 404 "Not Found" is returned, with response body
``` json
{
    "statusCode": 404,
    "message": "Not found"
}
```

This repository provides a reproducible example and can be deployed with
```
serverless deploy
```
