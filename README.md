# RNN Twitter Bot :robot::pencil2:

[![Python 3.6 | 3.7](https://img.shields.io/badge/python-3.6%20|%203.7-yellowgreen)](https://www.python.org/downloads/release/python-379/)
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)
<span class="badge-buymeacoffee"><a href="https://www.buymeacoffee.com/awu2303" title="Donate to this project using Buy Me A Coffee"><img src="https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg" alt="Buy Me A Coffee donate button" /></a>
</span>

A Twitter bot written in Python. The recurrent neural network Twitter bot is deployed on AWS and tweets generated text with a temperature of 0.7 from the trained model.

---

### Table of Contents

- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
        - [To Train the Model](#to-train-the-model)
        - [To Run the Bot](#to-run-the-bot)
        - [To Host the Bot](#to-host-the-bot-on-aws)
- [Instructions](#instructions)
    - [File Structure](#file-structure)
- [Deployment](#deployment)
- [Creator / Maintainer](#creator-maintainer)
- [Acknowledgments](#acknowledgments)
- [Additional Information](#additional-information)

---


## Getting Started

Make sure to follow [Twitter's Automation Rules](https://help.twitter.com/en/rules-and-policies/twitter-automation) to avoid getting your account banned.

### Prerequisites

#### To Train the Model

- [textgenrnn Colaboratory Notebook](https://colab.research.google.com/drive/1mMKGnVxirJnqDViH7BDJxFqWrsXlPSoK) - easily train your own text-generating neural network of any size and complexity for free on a GPU using Colaboratory

#### To Run the Bot

- [Python 3](https://www.python.org/downloads/release/python-379/)
- [Pip](https://pypi.org/project/pip/) - a python package manager
    - Download this [file](https://bootstrap.pypa.io/get-pip.py), open a command prompt and navigate to the folder containing the `get-pip.py` installer, and run `python get-pip.py` to install
        - Run `pip --version` to check if it has installed correctly
- [Tweepy](http://docs.tweepy.org/en/latest/index.html) - an easy-to-use python library for accessing Twitter's API
    - Run `pip install tweepy`
- [textgenrnn](https://github.com/minimaxir/textgenrnn) - a python3 module to easily train your own text-generating neural network of any size and complexity on any text dataset with a few lines of code, or quickly train on a text using a pretrained model
    - Run `pip install textgenrnn`

#### To Host the Bot on AWS

- [Amazon Web Services EC2](https://aws.amazon.com/ec2/) - a web service that provides secure, resizable compute capacity in the cloud
- [PuTTY](https://www.putty.org/) - an open-source terminal emulator, serial console and network file transfer application
- [WinSCP](https://winscp.net/eng/download.php) - a client that allows secure file transfers between the client's local computer and the remote server

---

## Instructions

1. Apply for [Twitter Developer Access](https://developer.twitter.com/en/apply-for-access) with the account you want the bot to be used for.

2. Create a new [Twitter Application](https://developer.twitter.com/app/new) to generate your private keys, secrets, and tokens.

![Keys and Secrets](resources-for-readme/keys-secrets.png)

- Make sure the app settings has *Read and Write* permissions.

![App Permissions](resources-for-readme/app-permissions.png)

3. Create a file named `credentials.py` to hold your private information using the format below.
    - See [File Structure](#file-structure).

```
TWITTER_API_KEY="xxxx"
TWITTER_API_KEY_SECRET="xxxx"
TWITTER_ACCESS_TOKEN="xxxx"
TWITTER_ACCESS_TOKEN_SECRET="xxxx"
```

4. Adjustments you can make in `config.py` to tweak the bot to your liking. *(Make sure to follow [Twitter's Automation Rules](https://help.twitter.com/en/rules-and-policies/twitter-automation) to avoid getting your account banned.)*
    - **weights**, **vocab**, and **config** - (*MUST CHANGE*) Names of the weights and configuration files you downloaded from Colaboratory
    - **gen_file** - Name of text file to generate text to
    - **temperature** - Higher temperature will generate crazier text
    - **prefix** - Set a prefix if you want each generated text to start with a given seed text
    - **n** - Number of texts to generate
    - **max_gen_length** - Maximum number of characters for each text generated
    - **max_tweet_length** - Maximum number of characters for each tweet to have
        - If the generated text is too long, it will be split into multiple tweets at this length
        - Set to 280 (Twitter's character limit for tweets) if you are not adding anything to the end of the tweets
    - **add_to_tweet** - Optional if you want to add text to end of tweets
        - Set to None if you do not want to use
    - **delay** - Time to wait in between each tweet in seconds
    - **min_tweet_length** - Minimum number of characters in the tweet, will ignore tweets that are not long enough
        - Set to 0 if this is not relevant to you

5. Use the [textgenrnn Colaboratory Notebook](https://colab.research.google.com/drive/1mMKGnVxirJnqDViH7BDJxFqWrsXlPSoK) to train your RNN.
    - See [Additional Information](#additional-information) for more details. 

6. Download the weights and configuration files from the Colaboratory Notebook (as shown below) and put them in the `model` directory
    - See [File Structure](#file-structure).

![Download Weight and Config Files](resources-for-readme/download-files.png)

7. Install all required packages needed to run the script

```
pip install -r requirements.txt
```

8. Run the script. Enjoy your Twitter bot!
```
python twitter-ai-bot.py
```

### File Structure

```
RNN-Twitter-Bot
|-- model
|   |-- yourmodelname_config.json
|   |-- yourmodelname_vocab.json
|   `-- yourmodelname_weights.hdf5
|-- credentials.py
`-- twitter-ai-bot.py
```
---

## Deployment

1. Launch an EC2 instance on Amazon Web Services.
    - See [Additional Information](#additional-information) for more details.

![Launch EC2 Instance](https://media.giphy.com/media/RIBJvH1dyXCl4WGrNl/giphy.gif)

2. Load the key-pair file (.pem) into PuTTYgen (which was downloaded when you installed [PuTTY](https://www.putty.org/)) and save the private key as a private key file (.ppk).

![Generate PPK](https://media.giphy.com/media/iIGG5Pgf338zjaAHMr/giphy.gif)

3. Connect to your instance on [WinSCP](https://winscp.net/eng/download.php).
    - The host name is ubuntu@[public DNS here].
    - Click Advanced, go to Authentication under SSH, and load the previously generated private key file (.ppk).
    - Login to the session.

![Conenct to WinSCP](https://media.giphy.com/media/XDpwQS1KQA5ZyqmKaN/giphy.gif)

4. Use [WinSCP](https://winscp.net/eng/download.php) to transfer the following directory and files to the server.

```
model (directory)
credentials.py
config.py
twitter-ai-bot.py
requirements.txt
your_generated_text_file.txt
```

5. Connect to your instance on a bash command line using one of the following ways.
    - Use a bash shell with the example ssh command (I use [Git Bash](https://gitforwindows.org/)).
        - Make sure you are in the directory with the key-pair file (.pem).
    - Use [PuTTY](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html?icmpid=docs_ec2_console) with the public DNS and private key file (.ppk).
    
![Connect to Bash](https://media.giphy.com/media/JTDsQkn9CG0bkQTv7T/giphy.gif)

6. Install python and pip to the server on the bash command line.

```
sudo apt update 
sudo apt upgrade
sudo apt install python3
sudo apt install python3-pip
pip3 install update pip
```

- Check if python and pip have been installed correctly.
    
    ```
    python3 --version
    pip3 --version
    ```

7. Install all required packages needed to run the script on the server.
```
sudo python3 -m pip install -r requirements.txt
```

8. Run the script. Enjoy!.
```
python3 twitter-ai-bot.py
```

- See [Additional Information](#additional-information) for details on running the script continuously.
    - I used the *screen* option.

---

### Creator / Maintainer

Annie Wu ([@anniewu2303](https://github.com/anniewu2303)) 

This project was created for educational purposes of learning development, documentation, and deployment and for personal and open-source use.

Default values of the project are used to run the Twitter account [@dickinson_rnn](https://twitter.com/dickinson_rnn)

If you like my content or find this code useful, give it a :star: or support me by buying me a coffee :coffee::grinning:

<a href="https://www.buymeacoffee.com/awu2303" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

---

## Acknowledgments

- [Max Woolf](https://minimaxir.com/) 
    - creator of [textgenrnn](https://github.com/minimaxir/textgenrnn)
    - creator of the [textgenrnn Colaboratory Notebook](https://colab.research.google.com/drive/1mMKGnVxirJnqDViH7BDJxFqWrsXlPSoK) that allows us to quickly train the RNN with a GPU for free

---

## Additional Information

- textgenrnn
    - [Max Woolf's YouTube Video on Training a Text-Generating Neural Network for Free with textgenrnn](https://www.youtube.com/watch?v=RW7mP6BfZuY)
    - [Max Woolf's Blog Post on How to Quickly Train a Text-Generating Neural Network for Free](https://minimaxir.com/2018/05/text-neural-networks/)
    - [Max Woolf's Demo of using the Colaboratory Notebook](https://github.com/minimaxir/textgenrnn/blob/master/docs/textgenrnn-demo.ipynb)

- Amazon Web Services EC2
    - [Getting Started with Amazon EC2](https://aws.amazon.com/ec2/getting-started/)
    - [How to Continuously Run a Python Script on an EC2 Server](https://intellipaat.com/community/9361/how-to-continuously-run-a-python-script-on-an-ec2-server)

