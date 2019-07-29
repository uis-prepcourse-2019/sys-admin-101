# Linux System Administration 101

## Introduction

## Prerequisite

## Task
In this task, the most important rule is working only in the terminal.

### Private Task
#### Scenario
Nora received the compressed file from Olav. There is a file that Nora should run using bash script.
However, Olav forgot where he put this script. Moreover, it is very possible that he made some typo.
#### Task
- Download the compressed file using (`wget` or `curl`) from the shell.
- Extract the file `task.tar.bz2`.
- Find the location of shell script file called `run.sh`.
- Fix the problem and successfully run the command `./run.sh`.

### Group Task 1
#### Scenario
Olav built the website for the group project. However, his teammate finds it challenging to deploy on their own machine. Therefore, Olav wants to make one bash file that can help his teammate to set up and run the website.
#### Task
- Download the folder called `group-task1`
- Complete the `start.sh` script.
- run `curl localhost:8080` and get the message.
- (bonus) Olav wants to run the website in the background using `screen`.

#### Hints/Notes
- Python version is 3.x
- It should be able to run `virtualenv` command in your working environment.
  - Otherwise use available machine or server.
  - Or you can install them
- Screen
  - https://linux4one.com/how-to-use-linux-screen-command-with-examples/
  - https://serverfault.com/questions/578608/start-unix-screen-run-command-detach
- Python virtualenv
  - https://virtualenv.pypa.io/en/latest/
  - https://flask.palletsprojects.com/en/1.1.x/installation/


### Group Task 2
