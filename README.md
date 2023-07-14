# Instagram post counter
## Setting up
---
### 1 - Create config.py

Create python file named **config.py**.

You are going to create 2 string variables.
- ```username```(Instagram username). 
- ```password```(Instagram password).

---
### 2 - Configure **gyms.csv**

The format of **gyms.csv** is the following.

**Instagram Username**, **Location link**

- **Instagram username**: Can be changed for a name just to identify.
- **Location link**: Is esential to count the number of posts.

**You can add as much pages as you want to record.**

---
### 3 - Install requirements.

If you do not have python installed, you can download it here.

[Download Python](https://www.python.org)

Here it is a guide, if you do not have installed pip.

[Guide pip](https://pip.pypa.io/en/stable/installation/)

As well here it is how to install requirements.txt.

``` 
pip install -r requirements.txt
``` 
---
## Running scripts.
---
### 4 - Run **main.py**
I will start recording posts, between each link it is going to sleep 5 minutes. Be patient or Instagram is going to ban your account.

After recording, the recording is going to be saved in a file named **linksRecorded.csv**, with the following format.

**Instagram Username**, **Location link**, **Quantity of posts**
- **Instagram username**: Can be changed for a name just to identify.
- **Location link**: Is esential to count the number of posts.
- **Quantity of posts**: The record of posts of each link.
### 5 - Run **wC.py**(Optional)
You can run this python script to create a Word Cloud, that way you can compare which of the links got more posts, and viseversa.

---

## **Any question you can contact me on:**
<p align='center'>
  <a href="https://www.linkedin.com/in/cesar-qui-270236205/"><img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://mail.google.com/mail/?view=cm&fs=1&to=cesarquimora07@gmail.com"><img src="https://img.shields.io/badge/Gmail-D14836?&style=for-the-badge&logo=gmail&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
</p>