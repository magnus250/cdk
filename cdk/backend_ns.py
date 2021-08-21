import os

from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    aws_cloudformation as cloudformation,
)


class BackendStack(cloudformation.NestedStack):

    def __init__(self, scope: core.Construct, construct_id: str,
                 *, params: dict, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        prefix = f"{params['prefix']}-backend"
        handler = _lambda.DockerImageFunction(
            self,
            f"{prefix}-lambda-image",
            code=_lambda.DockerImageCode.from_image_asset(
                os.path.join(params['root_dir'], 'src')
            ),
        )

        base_api = apigateway.RestApi(
            self,
            f"{prefix}-rest-api"
        )

        get_widgets_integration = apigateway.LambdaIntegration(
            handler,
            request_templates={"application/json": '{ "statusCode": "200" }'}
        )

        base_api.root.add_method("GET", get_widgets_integration)  # GET /

        core.CfnOutput(
            self, f"{prefix}-api-url",
            value=base_api.url
        )
