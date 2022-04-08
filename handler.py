import aws_lambda_powertools.event_handler.api_gateway
from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler import APIGatewayHttpResolver
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.logging.logger import set_package_logger

logger = Logger()
app = APIGatewayHttpResolver()

# Add to code to handle whitespaces in path parameters
# aws_lambda_powertools.event_handler.api_gateway._UNSAFE_URI = "%<> \[\]{}|^"
# aws_lambda_powertools.event_handler.api_gateway._NAMED_GROUP_BOUNDARY_PATTERN = rf"(?P\1[{aws_lambda_powertools.event_handler.api_gateway._SAFE_URI}{aws_lambda_powertools.event_handler.api_gateway._UNSAFE_URI}\\w]+)"

set_package_logger()


@app.get("/pets/<name>")
def get_petname(name):
    return {"name": name}


@app.get("/pets/<name>/vets")
def get_petname(name):
    return {"pet_name": name, "vets": []}


@logger.inject_lambda_context(
    correlation_id_path=correlation_paths.API_GATEWAY_HTTP, log_event=True
)
def lambda_handler(event, context):
    return app.resolve(event, context)
