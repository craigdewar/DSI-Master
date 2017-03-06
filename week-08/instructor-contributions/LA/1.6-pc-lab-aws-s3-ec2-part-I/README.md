---
title: AWS Amazon Web Services - Part I
duration: "1:15"
creator:
    name: Pauline Chow 
    city: LA
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) AWS: Amazon Web Services - Part I
Week 8 | Lesson 1.4

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- explain AWS offerings and which ones are relevant to data science
- understand the necessary configuration points for cloud computing
- store and download data from an S3 bucket
- be prepared to launch and connect to ec2 instance tomorrow!

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- students should have a credit card to sign up for AWS or have an AWS account
- login AWS console

### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Read in / Review any dataset(s) & starter/solution code
- Generate a brief slide deck
- Prepare any specific materials
- Provide students with additional resources

### ADDITIONAL CLOUD COMPUTING & BIG DATA PREP
This week requires additional prep in order to successfully run all lessons and labs provided:

This week: [Sign up for AWS Account & Credits](../AWS-instructions.md).
    - Note: Instructors will need to distribute individual URLs for the signup form. See linked instructions.
    - We will continue working out the details with AWS Education Accounts. Stay tuned! 


### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 min | [Opening](#opening) | Opening |
| 5 min | [AWS Setup](#opening) | Setting Up AWS Account |
| 15 min | [Introduction](#introduction) | Intro to AWS |
| 15 min | [Demo](#demo) | Elastic Compute Cloud [EC2] |
| 15 min | [Demo](#demo) | Simple Storage Service [S3] |
| 15 min | [Ind-practice](#ind-practice) | Simple Storage Service [S3] |
| 5 min | [Conclusion](#conclusion) | Conclusion |


<a name="opening"></a>
## Opening (5 min)

Today we are going to discover Amazon Web Services. In particular we will focus on those services that are mostly used in Data Science. AWS are cloud computing services, essentially virtual machines somewhere in a datacenter that you can access and pay only for the time you need them.

**Check:** What is a server?
> Answer: A server is a computer or software that performs administration or coordination functions within a network.

**Check:** What did the world look like before AWS and Google cloud?
> Answer: computation was expensive to set up, to access and to maintain => only large companies, governments and institutions had access to it. Now anyone can rent it for pennies.

<a name="opening"></a>
## Setting up AWS Account (5 min)

All users of AWS must set up an account connected to a credit card. Regardless of status as educator or students. The class will be using big data tools next week. 

You will not be charged if*:
- "free tier" usage applies to particluar product
- user is within usage constraints, such as time, size, volume
- user is a "new user," which is defined as the first 12 months of user lifetime
* Note: please check with each product and AWS policies 

The course producers will get more clarify from AWS on how to connect GA credits to each student accounts. Indidividuals can resubmit their applications.

Thank you for your patience!

**Check:** Who has signed up for an AWS account and is able to log into AWS Console? 

<a name="introduction"></a>
## Intro to AWS 

_Amazon Web Services (AWS)_, is a subsidiary of Amazon.com, which offers a suite of cloud computing services that make up an on-demand computing platform. These __services operate from 12 geographical regions across the world.__ The most central and best-known of these services arguably include Amazon Elastic Compute Cloud, also known as "EC2", and Amazon Simple Storage Service, also known as "S3". AWS now has more than __70 services__ that span a wide range including compute, storage, networking, database, analytics, application services, deployment, management, mobile, developer tools and tools for the Internet of things. Amazon markets AWS as a service to provide large computing capacity quicker and cheaper than a client company building an actual physical server farm. _(from wikipedia)_

Today we will explore two services that are relevant to a lot of big-data scenarios.

1. EC2 (Elastic Compute Cloud)
2. S3 (Simple Storage Service)

**Check:** What could be some advantages of using a server in the cloud instead of managing our own data center?

> Answer:
- Cost reduction: don't pay infrastructure costs when you don't need it
- Reliability: Servers are maintained and guaranteed by a company whose only job is to make sure they are available for you
- Scalability: Can add more computing power when necessary

<a name="ind-practice"></a>
## AWS Pricing 
## Cost Calculator

We've seen the simplest way to launch and terminate an instance in the cloud.

There's a lot more to it, that you'll discover in time, here are some pointers you may find useful:

[Pricing](https://aws.amazon.com/ec2/pricing/): EC2 pricing depends on the type of instance and on the chosen region. Make sure you understand the cost of the instance you request in order to avoid surprise bills. If you're in doubt you can use the convenient [Cost Calculator](http://calculator.s3.amazonaws.com/index.html) to get an exact forecast of your costs.

[Availability, Pricing, and Compute Power](https://aws.amazon.com/ec2/pricing/): Products at different EC2 pricing tiers relate to computational power and storage size. Availability is also determined by region. 

![](./assets/images/costcalculator.png)

**Check**: What is the smallest and largest EC2 instance? 

**Check**: Compare the compute power between two different types of instances, i.e. t2.nano and m3.medium.

**Check**: Compare the prices for these two instances, i.e. t2.nano and m3.medium.

<a name="ind-practice"></a>
## AWS Security Groups 

[Security Groups](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html): security groups are ways to open ports to the services running on our machine.

**Check:** can you give an example of a practical case?
> Answer: e.g. if we are running IPython notebook on the instance and want to reach it from a browser.

<a name="ind-practice"></a>
# AWS Elastic IPs  

[Elastic IPs](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html): we can rent a fixed IP address and associate it to our instance. This way we can configure tools to always connect to the same address, independently of which machine is behind it.

**Check:** can you give a practical use case?
> Answer: e.g. if we want to automate ssh connection with a configuration file.

<a name="demo"></a>
# Intro Elastic Compute Cloud [EC2] - About

The first service we will discover is _Elastic Compute Cloud_ or _EC2_. 

This service forms a central part of Amazon.com's cloud-computing platform by allowing users to **rent** virtual computers on which to run their own computer applications. Let's learn some terms first:

- **Instance**: virtual machine hosted in Amazon Cloud running the software we want

- **Amazon Machine Image (AMI)**: a snapshot of a configured machine that we can use as starting point to boot an instance. We can also save a running instance to a new AMI so that in the future we can boot a new machine with identical configuration.

- **SSH Key**: [pair of keys](https://en.wikipedia.org/wiki/Public-key_cryptography) necessary to connect to an instance remotely. The private key will be downloaded to our laptop, the matching public key will be automatically configured on the instance.
    - Directions for moving your AWS key pair into .ssh directory
    ```bash
    mkdir -p ~/.ssh  # Only if .ssh/ does not exist
    mv [downloaded key.pem location] ~/.ssh/ 
    chmod 400 [key.pem]
    ```
The main conceptual shift from using a laptop to running an instance in the cloud is that we should __think of computing power as ephemeral.__ We can request computing power when we need it, do a calculation and dismiss that power as we are done. Input and output will not be stored on the machine, rather stored somewhere else in the cloud (hint: S3). In this sense, computing power is a commodity that we purchase and use in the amount and time that we need.

<a name="introduction"></a>
## Intro to EC2 - Setup Steps Overview

Let's run conceptionalize what we will be setting up tomorrow:

Outline of steps in presentation and readme for EC2 setup. Also see linked AWS tutorials, as things can change over time:

1. Start an account on Amazon Web Services. 
2. Navigate to the AWS Console to choose "EC2"
3. Launch "EC2" Instance with (a) security group and (b) ssh key. 
5. Set up IAM profile for each user, so they can access information about AWS from the command line
6. Open terminal or bash shell
7. Connect to the AWS EC2 instance:
  ```bash
  'ssh -i [location of ssh key] [user]@[dns instance] 
  ```
**** Celebrate! Do a little dance! Yay! 
Now you are in your brand spanking new instance. Scale up and down as your needs change. ****

> Instructor note: Draw diagram on the board.

<a name="ind-practice"></a>
## Review Elastic Compute Cloud [EC2] Documentation

Let's review the [tutorial for EC2](https://aws.amazon.com/getting-started/tutorials/launch-a-virtual-machine/)

<a name="ind-practice"></a>
# Create an IAM Profile for User

#### Step 1: Create an AWS IAM User

In order to use the AWS command line we will have to configure a set of access credentials on our laptop. It's very important to create a separate identity with limited permissions instead of using our root account credentials.

This is a good [IAM Tutorial](https://aws.amazon.com/getting-started/tutorials/backup-to-s3-cli/) within the context of being able to interact with s3 from the command line

**Check:** why is this so important?
> Answer: so that we can limit the damage a user could do if he/she were to obtain our credentials

![](./assets/images/identitymanager.png)

**Note:** When attaching a Policy you can be more restrictive and only give the user permission to use the services you intend him/her to use.

<a name="demo"></a>
# Intro Simple Storage Service [S3] (5 min)

Let's learn how we can store data in the cloud too.

Amazon S3 (Simple Storage Service) is an online file storage. It provides storage through web services interfaces (REST, SOAP, and BitTorrent) using an _object storage architecture_. According to Amazon, S3's design aims to provide scalability, high availability, and low latency at commodity costs.

Objects are organized into buckets (each owned by an Amazon Web Services account), and identified within each bucket by a unique, user-assigned key. Buckets and objects can be created, listed, and retrieved using either a REST-style HTTP interface or a SOAP interface. Additionally, objects can be downloaded using the HTTP GET interface and the BitTorrent protocol.

<a name="ind-practice"></a>
## Independent Practice and Lab with S3
## Simple Storage Service [S3] (5 min)

Let's navigate from the AWS console to S3 product in the Storage category. 

Complete the two tasks below in groups: 

In pairs: go ahead and follow the [tutorial for S3](https://aws.amazon.com/getting-started/tutorials/backup-files-to-amazon-s3/).
    The steps should be straight-forward to follow. Any questions?

    **Check:** what's a practical case you can envision using S3 for?
    > Answer: storing input dataset, storing result tables. It's like Dropbox
    
    **Bonus 1:** Create a folder in our bucket and upload a csv file
    **Bonus 2:** Delete folders and buckets in the AWS cosole

<a name="conclusion"></a>
# Conclusion (5 min)

In this lesson we have learned about 2 fundamental Amazon web services: Elastic Cloud Compute and Simple Storage Service. These 2 services are so common because they provide on demand computation and storage at a very affordable cost.

Tomorrow, we will launch your first "Computing as a Service" instance. 

### ADDITIONAL RESOURCES

- [AWS FAQ](https://aws.amazon.com/ec2/faqs/)
- [EC2](https://aws.amazon.com/ec2/?nc2=h_m1)
- [S3](https://aws.amazon.com/s3/?nc2=h_m1)
- [Tutorials](https://aws.amazon.com/getting-started/tutorials/)
- [AWS CLI Tutorial](http://www.joyofdata.de/blog/guide-to-aws-ec2-on-cli/)
