from aws_cdk import (
    core,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as cpations,
    pipelines,
)

from cdk.web_service import WebServiceStage


class PipelineStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, *, params: dict,
                 **kwargs):
        super().__init__(scope, id, **kwargs)

        source_artifact = codepipeline.Artifact(
            f"{params['prefix']}-source-artifact"
        )
        cloud_assymble_artifact = codepipeline.Artifact(
            f"{params['prefix']}-cloud-assymble-artifact"
        )

        pipeline = pipelines.CdkPipeline(
            self,
            f"{params['prefix']}-pipeline",
            cloud_assembly_artifact=cloud_assymble_artifact,
            pipeline_name=f"{params['prefix']}-pipeline",
            source_action=cpations.GitHubSourceAction(
                action_name='Github',
                output=source_artifact,
                oauth_token=core.SecretValue.secrets_manager('github-token'),
                owner='magnus255',
                repo='cdkpipeline',
                branch='lambda/django',
                trigger=cpations.GitHubTrigger.POLL,
            ),
            synth_action=pipelines.SimpleSynthAction(
                source_artifact=source_artifact,
                cloud_assembly_artifact=cloud_assymble_artifact,
                install_command='npm install -g aws-cdk && pip install -r requirements.txt',
                synth_command='cdk synth',
            )
        )
        # stage = pipeline.add_stage(stage_name='Wait')
        # stage.add_manual_approval_action(action_name='Wait')

        pipeline.add_application_stage(
            WebServiceStage(
                self,
                f"{params['prefix']}-stage",
                params=params,
                env=params['env'],
            ),
            # manual_approvals=True,
        )
