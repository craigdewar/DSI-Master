#Outline of steps in presentation and readme for EC2 setup.

###BRAND NEW SETUP STEPS
1. Start an account on Amazon Web Services. You'll need a user name and password.
2. Navigate to the AWS Console to choose "EC2" 
3. Launch "EC2" Instance with proper security group and ssh key. You are able to use existing or new ssh key
4. Upload SSH key for this instance in your ~/.ssh/ location in your local environment.
5. Set up property IAM profile for user
6. Check the rights/access to the file. If necessary 'chmod 400 ~/.ssh/[key].pem'
7. Open terminal or bash shell
8. Type the command: 'ssh -i [location of ssh key] [user]@[dns instance]
9. If necessary, install packages and services on EC2 instance

###EXISTING USER SETUP STEPS (not first time using AWS)
####UBUNTU INSTANCES EXERCISE
1. Log into Amazon Web Services with your username and password.
2. Navigate to the AWS Console to choose "EC2". 
3. Launch "EC2" Ubuntu Free Tier Instance with proper security group and ssh key. See [tutorial](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)
7. Open terminal or bash shell
8. Type the command: 'ssh -i [location of ssh key] Ubuntu@[dns instance]
9. Copy and paste first_install_ubuntu.sh into "nano $filename.sh" OR pipe the file into your ec2
- find github repo and install script: https://github.com/PowChow/knn_athletes 
- run the install script: "bash first_install_ubuntu.sh"
11. Run "python ~/knn_athletes/Exercise_KNN_Classifier_Solution.py" (Note: Use absolute or relative path)
