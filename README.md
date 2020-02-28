# Telegram-Chatbot
A simple Telegram chatbot written in Python using [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) and [Dialogflow](https://dialogflow.cloud.google.com/). 


* Links:
  
  * [Installation](#installation)
  * [Setup Dialogflow](#setup-dialogflow)


# Installation:
* Linux:
  * `sudo pacman -S python`
  * `pip install apiai python-telegram-bot json`
  * `git clone https://github.com/dmatviichuk/Telegram-Chatbot`
  * `cd Telegram-Chatbot/`
  * Change your api token from Dialogflow and Telegram
  * `python Chatbot.py`

* Windows:
  * Download Python 3.6 from [here](https://www.python.org/downloads/release/python-360/)
  * Launch installer, click `add python to PATH`
  * Open cmd or powershell
  * `pip install apiai python-telegram-bot json`
  * Change your api token from Dialogflow and Telegram
  * `python Chatbot.py`

# Setup Dialogflow:
First of all, go and register on Dialogflow (just log in using your Google account). Immediately after authorization, we get to the control panel.
![1](https://i.imgur.com/ZUVTIQo.jpg)
Click on the **Create agent** button and fill in the fields as you wish:
![2](https://i.imgur.com/khcw0DX.jpg)
Click on **Create**, than click on **Prebuilt Agents** and from the entire list select **Small Talk**:
![3](https://i.imgur.com/E0tqwyK.jpg)
Go to the **Settings** of your project and copy API token:
![4](https://i.imgur.com/Tspqt2F.jpg)