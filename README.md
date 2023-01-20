# NoraAI - Url opener AI

Nora AI is built using Whisper. Whisper is an open-source, multilingual, general-purpose speech recognition model by OpenAI. The Nora AI is a skeleton project to demonstrate how one can Open url on the default browser without typing any URL in the browser. Just say "Nora open google.com" and it ✨Magically ✨opens the website.

Run the required files and start interacting with the AI. Tell the NoraAI to open google.com

## Installation

NoraAI requires Python 3.8 and above.

Clone repo and create virtual env. Virtual environment creation for Windows

```sh
py -3 -m venv .venv
.venv\scripts\activate
```

Virtual environment creation for macOS/Linux

```sh
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies

```sh
pip install -r requirements.txt
```

## Prerequisites

Before we start with the transcription and comparison of the two models, we have to make sure that a few prerequisites are met.

Install ffmpeg
To be able to read audio files, we have to install a command line tool named ffmpeg first. Depending on your OS, you have the following options:

```sh
# Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

## Config File

In the config file add your open AI Key
replace COMMAND_WORD value with your AI name

## Run

Run the below files

| File Name        | command                   |
| ---------------- | ------------------------- |
| transcriber.py   | python .\transcriber.py   |
| websiteopener.py | python .\websiteopener.py |
| recorder.py      | python .\recorder.py      |

## Config file

## License

MIT

**Free Software, Hell Yeah!**

[//]: # "These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax"
[openai]: https://beta.openai.com/
[towarddatascience]: https://towardsdatascience.com/transcribe-audio-files-with-openais-whisper-e973ae348aa7
