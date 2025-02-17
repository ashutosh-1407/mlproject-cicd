## End to End Machine Learning Project

Different ways of deploying to Cloud

AWS - 

Method 1 (Probably the "EASIEST WAY"):
1. Create a folder called ".ebextensions" and a file inside called "python.config" with the lines shown below (for web server in a container).
    option_settings:
    "aws:elasticbeanstalk:container:python":
        WSGIPath: app:app
2. Make sure to give the correct WSGIPath.
3. Go to AWS Elastic Beanstack and create an application, wait for it to get created.
4. Create a Code Pipeline using AWS CodePipeline, link it your github account.
5. This will create a CD pipeline. That means as soon as you push some changes, you will see a button to "Release change" to deploy the changes to AWS Elastic Beanstalk.
