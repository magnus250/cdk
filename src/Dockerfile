FROM public.ecr.aws/lambda/python:3.8

ARG DJANGO_PROJECT='backend'

# Copy function code
#COPY lambda.py ${LAMBDA_TASK_ROOT}
COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip install -r requirements.txt --target ${LAMBDA_TASK_ROOT}

COPY . ${LAMBDA_TASK_ROOT}

# Unpack django to level + 1
RUN mv ${DJANGO_PROJECT}/${DJANGO_PROJECT}/ ${LAMBDA_TASK_ROOT}/tmp_${DJANGO_PROJECT}/
RUN mv ${DJANGO_PROJECT}/* ${LAMBDA_TASK_ROOT}/
RUN rm -r ${DJANGO_PROJECT}/
RUN mv ${LAMBDA_TASK_ROOT}/tmp_${DJANGO_PROJECT}/ ${LAMBDA_TASK_ROOT}/${DJANGO_PROJECT}/

RUN ls
WORKDIR ${LAMBDA_TASK_ROOT}


# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lambda.handler" ]