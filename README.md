# Reddit Image (meme) Grabber

This script allows you to download a random programming meme from the "ProgrammerHumor" subreddit and save it to your device.

## Prerequisites
Termux app installed on your Android phone. You can download it from the Google Play Store.

## Installation
1. Open Termux on your Android phone.

2. Run the following commands to set up the required dependencies:

```bash
pkg update
pkg install python python-pip git
```

3. Clone the GitHub repository:

```bash
git clone https://github.com/musawerfatih/reddit_meme_grabber
```
4. Change to the repository directory:

```bash
cd reddit_meme_grabber
```

5. Install the required Python packages:

```bash
pip install -r requirements.txt
```
6. Run the script:

```bash
python reddit_meme.py
```

## Usage
To run the script and download a random programming meme, follow these steps:

1. Open Termux on your Android phone.

2. Change to the repository directory:

```bash
cd reddit_meme_grabber
```

3. Run the script:

```bash
python reddit_meme.py
```

The script will fetch a random programming meme from the "ProgrammerHumor" subreddit and save it to the default download folder on your device.

## Note

Please note that the instructions provided assume that you have a fresh installation of Termux. If you have already installed Termux and configured it, you can skip the installation steps and directly clone the repository, install the required packages, and run the script.
