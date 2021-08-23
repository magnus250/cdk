from aws_cdk import (
    core,
)
from .rds_ns import RdsStack
from .backend_ns import BackendStack


class AppStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str,
                 *, params: dict, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.rds = RdsStack(self, f"{params['prefix']}-rds-stack", params=params)
        self.backend = BackendStack(self, f"{params['prefix']}-backend-stack", params=params)
        self.backend.add_dependency(self.rds)
