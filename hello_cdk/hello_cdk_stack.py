import aws_cdk as aws_cdk
import aws_cdk.aws_s3 as aws_s3

from constructs import Construct

class HelloCdkStack(cdk.Stack):

    def __init__(self, scope: cdk.App, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        bucket = s3.Bucket(self, "MyFirstBucket", versioned=True)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "HelloCdkQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
