FROM public.ecr.aws/lambda/python:3.8

ARG DJANGO_PROJECT='backend'

# Copy function code
#COPY lambda.py ${LAMBDA_TASK_ROOT}
COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip install -r requirements.txt --target ${LAMBDA_TASK_ROOT}

COPY backend ${LAMBDA_TASK_ROOT}

COPY lambda.py ${LAMBDA_TASK_ROOT}

WORKDIR ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lambda.handler" ]