#!/usr/bin/env python3
import os

from dotenv import load_dotenv

from aws_cdk import core

from cdk import AppStack

load_dotenv('secrets/local.env')

params = dict(
    root_dir=os.path.dirname(__file__),
    prefix='cdk-base',
    app_name='jpjp',
    env=dict(
        account=os.environ['AWS_ACCOUNT'],
        region=os.environ['AWS_REGION'],
    ),
    owner=os.environ['GITHUB_REPO_OWNER'],
    repo=os.environ['GITHUB_REPO_NAME'],
    branch=os.environ['GITHUB_REPO_BRANCH'],
)
app = core.App()

AppStack(app, f"{params['prefix']}-app-stack", params=params, env=params['env'])

app.synth()
