from aws_cdk import core
from aws_cdk.core import DefaultStackSynthesizer

from .web_service_stack import WebServiceStack


class WebServiceStage(core.Stage):
    def __init__(self, scope: core.Construct, id: str, *, params: dict,
                 **kwargs):
        super().__init__(scope, id, **kwargs)

        WebServiceStack(
            self,
            f"{params['prefix']}-service-stack",
            params=params,
            synthesizer=DefaultStackSynthesizer()
        )
