# Container image that runs your code
FROM amazon/aws-cli:2.2.9

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY update_coundfront_distribution.py /update_coundfront_distribution.py

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["python", "/entrypoint.sh"]
