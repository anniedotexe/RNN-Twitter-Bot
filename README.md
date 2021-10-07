# RNN Twitter Bot :robot::pencil2:

[![Python 3.6 | 3.7](https://img.shields.io/badge/python-3.6%20|%203.7-yellowgreen)](https://www.python.org/downloads/release/python-379/)
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

A Twitter bot written in Python. The recurrent neural network Twitter bot tweets generated text with a temperature of 0.7 from the trained model.

---

### Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
    - [To Train the Model](#to-train-the-model)
    - [To Run the Bot](#to-run-the-bot)
- [Instructions](#instructions)
  - [File Structure](#file-structure)
- [Contributing](#contributing)
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

- [Python 3.6 or 3.7](https://www.python.org/downloads/release/python-379/)
- [Pip](https://pypi.org/project/pip/) - a python package manager
  - Download this [file](https://bootstrap.pypa.io/get-pip.py), open a command prompt and navigate to the folder containing the `get-pip.py` installer, and run `python get-pip.py` to install
    - Run `pip --version` to check if it has installed correctly
- [Tweepy](http://docs.tweepy.org/en/latest/index.html) - an easy-to-use python library for accessing Twitter's API
  - Run `pip install tweepy`
- [textgenrnn](https://github.com/minimaxir/textgenrnn) - a python3 module to easily train your own text-generating neural network of any size and complexity on any text dataset with a few lines of code, or quickly train on a text using a pretrained model
  - Run `pip install textgenrnn`

---

## Instructions

1. Apply for [Twitter Developer Access](https://developer.twitter.com/en/apply-for-access) with the account you want the bot to be used for.

2. Create a new [Twitter Application](https://developer.twitter.com/app/new) to generate your private keys, secrets, and tokens.

![Keys and Secrets](resources-for-readme/keys-secrets.png)

- Make sure the app settings has _Read and Write_ permissions.

![App Permissions](resources-for-readme/app-permissions.png)

3. Create a file named `credentials.py` to hold your private information using the format below.
   - See [File Structure](#file-structure).

```
TWITTER_API_KEY="xxxx"
TWITTER_API_KEY_SECRET="xxxx"
TWITTER_ACCESS_TOKEN="xxxx"
TWITTER_ACCESS_TOKEN_SECRET="xxxx"
```

4. Adjustments you can make in `config.py` to tweak the bot to your liking. _(Make sure to follow [Twitter's Automation Rules](https://help.twitter.com/en/rules-and-policies/twitter-automation) to avoid getting your account banned.)_

   - **model_name** - (_MUST CHANGE_) Name of the model used for the weights and configuration files you downloaded from Colaboratory.
     ![Model Name](resources-for-readme/model-name.png)
   - **temperature** - Level of randomness for the predicted text. Higher temperature will generate crazier text.
   - **prefix** - Set a prefix if you want each generated text to start with a given seed text.
   - **n** - Number of texts to generate.
   - **max_gen_length** - Maximum number of characters for each text generated.
   - **max_tweet_length** - Maximum number of characters for each tweet to have.
     - If the generated text is too long, it will be split into multiple tweets at this length.
     - Set to 280 (Twitter's character limit for tweets) if you are not adding anything to the end of the tweets.
   - **add_to_tweet** - Optional if you want to add text to end of every tweet.
     - Set to None if you do not want to use.
   - **delay** - Time to wait in between each tweet in seconds.
   - **min_tweet_length** - Minimum number of characters in the tweet, will ignore tweets that are not long enough.
     - Set to 0 if this is not relevant to you.

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

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.

### How To Contribute

1. Fork the repository to your own Github account.
2. Clone the project to your machine.
3. Create a branch locally with a succinct but descriptive name.
4. Commit changes to the branch.
5. Following any formatting and testing guidelines specific to this repo.
6. Push changes to your fork.
7. Open a Pull Request in my repository.

---

### Creator / Maintainer

Annie Wu ([anniedotexe](https://github.com/anniedotexe))

If you have any questions, comments, or concerns, feel free to contact me below.

<p align="left">
  <a href="mailto:anniewu2303@gmail.com"> 
    <img alt="Connect via Email" src="https://img.shields.io/badge/Gmail-c14438?style=flat&logo=Gmail&logoColor=white" />
  </a>
</p>

This project was created for educational purposes of learning development, documentation, and deployment and for personal and open-source use.

Default values of the project are used to run the Twitter account [@dickinson_rnn](https://twitter.com/dickinson_rnn), a bot that was trained to generate text with Emily Dickinson poems.

If you like my content or find this code useful, give it a :star: or support me by buying me a coffee :coffee::grinning:

<a href="https://www.buymeacoffee.com/anniedotexe" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

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
