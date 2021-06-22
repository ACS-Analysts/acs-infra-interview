# Lead Interview Questions
## Behaviorial
* Tell me about your professional life. How does your experiences and career ambitions make you a good fit for this position?
* Tell me about a cloud based program where you were responsible for architecture and/or code development. What tools, methods and coding languages were utilized and why?
* Please give an example of a complex cloud problem effecting a production environment you have solved. What was the problem? What was your role? How did you go about solving it? What were the favorable outcomes as a result of your involvement?
* Please describe a technically innovative initiative where you were integral part in the design, build and/or implementation. What was the project? What was innovative about it? What was your role? What was the outcome?
* In this role, sometimes unrealistic requests are made of us. It could be functionally impossible or overly aggressive timeline given resources available. Help us understand how you go about managing expectations with leaders in your company when they ask the impossible.
* This is a remote position and team members are spread across ACS and client sites through several timezones.  What is your experience working within a remote team? What techniques and technologies do you use to collaborate successfully in this type of environment?

## Technical
### Container Demo
* Have the candidate build the image (docker build -t image hello .)
* Have the candidate run the image (docker run hello)
* Have the candidate show the logs (docker logs)
### General
* What is immutable infrastructure / benefits of? 
    * Immutable infrastructure can't be updated in place
    * Candidate should be able to explain pros/cons of immutable vs. having to maintain running infra
* How do Edge Computing and IoT relate to one another / benefits of Edge Computing?
    * IoT is the Internet of Things and refers to the myriad of inter-connected devices that can be used in a solution and edge computing brings computational power closer to the devices
    * Candidate should describe the benefits of Edge Computing (eg. cost/latency by processing data at the edge)
* What is CloudFormation / benefits of?
    * Declarative IaC provided by AWS to automate resource provisioning
    * Candidate should be able to describe common features and benefits like using JSON/YAML, templating, customization through parameters, etc.
* What's a circular dependency in AWS CloudFormation and how would you address that?
    * Resource X is dependent on Resource Y, and Resource Y is dependent on Resource X.
    * The first step is to examine the resources that are outlined and make sure that AWS CloudFormation can determine what resource order it should take.
    * To resolve a dependency error, add a DependsOn attribute to resources that depend on other resources in your template.
* What is a CI/CD pipeline and when should you use one?
    * Continuous Integration / Continuous Delivery (or Deployment) is a set of best practices that ensure code changes are validated and deployed frequently.
    * CI triggers the build process whenever new code changes are detected and would include unit tests to find defects as early in the process as possible.
    * Continuous Delivery begins _after_ CI and is concerned with deploying code to particular environments.  It could be thought of as an automated release process.
    * Continuous Deployment goes one step further than Continuous Delivery and would be a fully automated pipeline that deploys and validates all the way through production.

# Developer Interview Questions
## Behaviorial
* Tell me about your professional life. How does your experiences and career ambitions make you a good fit for this position?
* Tell me about a cloud based program where you were responsible for architecture and/or code development. What tools, methods and coding languages were utilized and why?
* Please give an example of a complex cloud problem effecting a production environment you have solved. What was the problem? What was your role? How did you go about solving it? What were the favorable outcomes as a result of your involvement?
* Please describe a technically innovative initiative where you were integral part in the design, build and/or implementation. What was the project? What was innovative about it? What was your role? What was the outcome?
* In this role, sometimes unrealistic requests are made of us. It could be functionally impossible or overly aggressive timeline given resources available. Help us understand how you go about managing expectations with leaders in your company when they ask the impossible.
* This is a remote position and team members are spread across ACS and client sites through several timezones.  What is your experience working within a remote team? What techniques and technologies do you use to collaborate successfully in this type of environment?

## Technical
### Container Demo
* Have the candidate build the image (docker build -t image hello .)
* Have the candidate run the image (docker run hello)
* Have the candidate show the logs (docker logs)
* Create another Docker image called `hello_input` with an updated script that prompts the user for input (docker build -t hello_input .)
* How would you obtain a shell prompt on the container after it's launched?
    * In this case you can't because once the script completes the container stops
    * You would need to modify the script to not exit or rerun the image as follows ```docker run -it --entrypoint bash hello```
* How would you set the container up to allow interaction with the local filesystem?
    * Use the -v flag to define the local mount point and where it should appear in the container
### General
* What is immutable infrastructure / benefits of? 
    * Immutable infrastructure can't be updated in place
    * Candidate should be able to explain pros/cons of immutable vs. having to maintain running infra
* How do Edge Computing and IoT relate to one another / benefits of Edge Computing?
    * IoT is the Internet of Things and refers to the myriad of inter-connected devices that can be used in a solution and edge computing brings computational power closer to the devices
    * Candidate should describe the benefits of Edge Computing (eg. cost/latency by processing data at the edge)
* What is CloudFormation / benefits of?
    * Declarative IaC provided by AWS to automate resource provisioning
    * Candidate should be able to describe common features and benefits like using JSON/YAML, templating, customization through parameters, etc.
* What's a circular dependency in AWS CloudFormation and how would you address that?
    * Resource X is dependent on Resource Y, and Resource Y is dependent on Resource X.
    * The first step is to examine the resources that are outlined and make sure that AWS CloudFormation can determine what resource order it should take.
    * To resolve a dependency error, add a DependsOn attribute to resources that depend on other resources in your template.
* What is a CI/CD pipeline and when should you use one?
    * Continuous Integration / Continuous Delivery (or Deployment) is a set of best practices that ensure code changes are validated and deployed frequently.
    * CI triggers the build process whenever new code changes are detected and would include unit tests to find defects as early in the process as possible.
    * Continuous Delivery begins _after_ CI and is concerned with deploying code to particular environments.  It could be thought of as an automated release process.
    * Continuous Deployment goes one step further than Continuous Delivery and would be a fully automated pipeline that deploys and validates all the way through production.