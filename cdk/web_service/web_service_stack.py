import os

from aws_cdk import (
    core,
    aws_lambda as lmb,
    aws_apigateway as apigw,
)


class WebServiceStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str,
                 *, params: dict, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        handler = lmb.DockerImageFunction(
            self,
            f"{params['prefix']}-lambda-image",
            code=lmb.DockerImageCode.from_image_asset(
                os.path.join(params['root_dir'], 'app')
            ),
        )

        base_api = apigw.RestApi(
            self,
            f"{params['prefix']}-rest-api",
            rest_api_name=f"{params['prefix']}-rest-api-name",
        )

        get_widgets_integration = apigw.LambdaIntegration(
            handler,
            request_templates={"application/json": '{ "statusCode": "200" }'}
        )

        base_api.root.add_method("GET", get_widgets_integration)  # GET /

        core.CfnOutput(
            self, f"{params['prefix']}-url",
            value=base_api.url,
            export_name=f"{params['prefix']}-url"
        )
