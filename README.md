# Chatbot With Emoji's

## Requirements:

Create a virtual environment

```
$ python3 -m venv venv
$ . venv/bin/activate
```

Install dependencies

```
$ (venv) pip install Flask torch torchvision nltk
```

Install nltk package

```
$ (venv) python
>>> import nltk
>>> nltk.download('punkt')
```

Modify `intents.json` with different intents and responses for your Chatbot

Run

```

$ (venv) python train.py
$ (venv) python chat.py
```
