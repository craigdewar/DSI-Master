**Outline of steps in presentation and readme for EC2 setup.** 
Also see linked AWS tutorials, as things can change over time:

1. Start an account on Amazon Web Services. You'll need a user name and password.
2. Navigate to the AWS Console to choose "EC2" 
3. Launch "EC2" Instance with proper security group and ssh key. You are able to use existing or new ssh key
4. Upload SSH key for this instance in your ~/.ssh/ location in your local environment.
5. Set up property IAM profile for user
6. Check the rights/access to the file. If necessary 'chmod 400 ~/.ssh/[key].pem'
7. Open terminal or bash shell
8. Type the command: 'ssh -i [location of ssh key] [user]@[dns instance]
9. If necessary, install packages and services on EC2 instance

