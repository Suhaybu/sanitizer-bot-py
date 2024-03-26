# Sanitizer-bot

[![](https://img.shields.io/pypi/v/discord-py-interactions.svg?label=Interactions.py&logo=pypi)](https://github.com/interactions-py/interactions.py)
![](https://img.shields.io/badge/Python-3.12+-1081c1?logo=python)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![License](https://img.shields.io/badge/license-CC0_1.0-v1)](https://github.com/Suhaybu/Sanitizer-bot/blob/main/LICENSE)


## Introduction

Sanitizer is a simple bot that uses regex to identify links for social platforms and replaces them with discord embed friendly links that allows you to view the content of the link without ever having to leave the discord app. You might think this is a bot for lazy people, but I assure you, if you give it a try, you'll never want to go back.

The bot is developed in Python using the `interactions.py` library. Click [here](https://github.com/interactions-py/interactions.py) for their GitHub repo. This GitHub repo is utilized for version control and the assistance of GitHub Copilot has been used for creating examples of implementation from documentations.

## TODO

-   Add Reddit Support
-   Add User Installable commandds

## Features

-   **Supports Multiple platforms:** Currently works with Twitter, TikTok, Instagram. More to come!
-   **Automatic conversion:** Automatically fixes links from any of the supported platforms.
-   **Deleted original embed:** After successfully replying to the original message with fixed embed, automatically deletes original broken embed.
-   **Implemented QuickTock API:** Implemented QuickTock API to convert TikTok links into embeddable content in discord.
-   **Handels DMs:** You can DM Sanitizer with the link you want for it to convert.

## Getting Started

### Prerequisites

-   Python 3.12 or higher
-   Discord account and a server to test the bot

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/suhaybu/sanitizer-bot.git
    ```
2. **Setup virtual Python environment:**
    ```bash
    python3 -m venv .venv
    ```
3. Activate virtual Python environment:
   on Unix or MacOS
    ```bash
    source .venv/bin/activate
    ```
    on Windows
    ```bash
    .venv\Scripts\activate
    ```
3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Set up your Bot Token:**
   Add your Discord bot token to the `.env` file present in the root directory.

### Running the Bot

To run the bot, use the following command:

```bash
python main.py
```

## Usage

Once the bot is running and in your server, you can use the following commands:

-   `/credits`: To roll the credits

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Suhayb - [@suhayb_u](https://twitter.com/suhayb_u)

Project Link: [https://github.com/suhaybu/sanitizer-bot](https://github.com/suhaybu/sanitizer-bot)

## Acknowledgments
-   [interactions.py](https://github.com/interactions-py/interactions.py)
-   **Twitter:** Thanks to FixTweet's awesome [FxTwitter](https://github.com/FixTweet/FxTwitter) project
-   **Instagram:** Thanks to [Embedez](https://embedez.com/) reliable service (TODO)
-   **TikTok:** Thanks to [QuickVids](https://quickvids.win/) super fast API
