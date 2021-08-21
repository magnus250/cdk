import json

from aws_cdk import (
    core,
    aws_cloudformation as cloudformation,
    aws_secretsmanager as secretsmanager,
    aws_rds as rds,
    aws_ec2 as ec2,
)
from aws_cdk.aws_rds import Credentials


class RdsStack(cloudformation.NestedStack):

    def __init__(self, scope: core.Construct, construct_id: str,
                 *, params: dict, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        prefix = f"{params['prefix']}-rds"

        # secrets manager for DB password
        self.credentials = secretsmanager.Secret(
            self,
            f"{prefix}-credentials",
            secret_name=f"{prefix}-credentials",
            generate_secret_string=secretsmanager.SecretStringGenerator(
                secret_string_template=json.dumps({"username": "postgres"}),
                exclude_punctuation=True,
                include_space=False,
                generate_string_key="password",
            ),
        )

        credentials = Credentials.from_secret(self.credentials)

        vpc = ec2.Vpc.from_lookup(
            self, f"{prefix}-vpc", is_default=True
        )

        # self.db_security_group = ec2.CfnSecurityGroup(
        #     self,
        #     f"{prefix}-security_group",
        #     group_name=f"{prefix}-security_group",
        #     vpc_id=vpc.vpc_id,
        #     group_description="Database security group",
        #     security_group_egress=[],
        #     security_group_ingress=[
        #         ec2.CfnSecurityGroup.IngressProperty(
        #             ip_protocol="tcp",
        #             to_port=5432,
        #             from_port=5432,
        #         )
        #     ],
        # )
        # self.db_security_group.security_group_ingress()

        self.db_config = dict(
            database_name=params['app_name'],
            engine=rds.DatabaseInstanceEngine.postgres(
                version=rds.PostgresEngineVersion.VER_12_7
            ),
            instance_type=ec2.InstanceType('t2.micro'),
            vpc=vpc,
            vpc_placement={
                'subnet_type': ec2.SubnetType.PUBLIC
            },
            storage_type=rds.StorageType.GP2,
            deletion_protection=False,
            port=5432,
            credentials=credentials,
            security_groups=[
                # self.db_security_group
            ]
        )

        self.instance = rds.DatabaseInstance(
            self, f"{prefix}-instance",
            instance_identifier=f"{prefix}-instance",
            **self.db_config,
        )

        self.instance.connections.allow_default_port_from_any_ipv4()
        self.instance.connections.allow_default_port_internally()

        core.CfnOutput(
            self, f"{prefix}-endpoint-address",
            export_name=f"{prefix}-endpoint-address",
            value=self.instance.db_instance_endpoint_address,
        )
        core.CfnOutput(
            self, f"{prefix}-endpoint-port",
            export_name=f"{prefix}-endpoint-port",
            value=self.instance.db_instance_endpoint_port,
        )