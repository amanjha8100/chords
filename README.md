<div align="center"><a href="https://hacktoberfest.digitalocean.com/"><img src="https://hacktoberfest.digitalocean.com/_nuxt/img/logo-hacktoberfest-full.f42e3b1.svg" alt="Banner" width="60%"/></a></div>

<!-- PROJECT LOGO -->
<br />
<p align="center">
    <img src="https://i.imgur.com/P0yZRLA.png" alt="Logo" width="60%">

  <h1 align="center">Chords</h1>

  <h3 align="center">
    On a mission to build the best Discord Music Bot
    <br />
    <br />
    <a href="https://github.com/amanjha8100/chords">View Demo</a>
    ·
    <a href="https://github.com/amanjha8100/chords/issues">Report Bug</a>
    ·
    <a href="https://github.com/amanjha8100/chords/issues">Request Feature</a>
  </h3>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#available-bot-commands">Bot Commands</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

Most of the Discord Music Bots are down. They got banned, unfortunately.\
So we thought of making our own Discord Music Bot for our Discord Community.

### Built With

- [Python](https://www.python.org/)
- [discord.py](https://discordpy.readthedocs.io/)
- [FFmpeg](https://www.ffmpeg.org/)
- [youtube_dl](https://pypi.org/project/youtube_dl/)

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

**You should have Pyhton and FFmpeg installed in your system**

- Download Python3 from [here](https://www.python.org/downloads/)
- Download FFmpeg from [here](https://www.ffmpeg.org/)

### Installation

1. Fork the project first

2. Clone the forked repo
   ```sh
   git clone https://github.com/your_name/chords.git
   ```
3. In the project directory, install the packages using

   ```sh
   pip install -r requirements.txt
   ```

4. Create a Bot from the Discord Developer Portal and copy the Bot token. Create a `.env` file and paste the Token.

   ```sh
   TOKEN = "Your Token"
   ```

5. Invite the Bot to your server and run

   ```sh
   python app.py
   ```

## Available Bot Commands
```
_p <song> : Plays the song with search keyword following the command
_s : skips the currently playing music
_q : shows the music added in list/queue
_l : commands the bot to leave the voice channel
_pn : Moves the song to the top of the queue
_r <index>: removes song from queue at index given
_help : shows all the commands of the bot.
```

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/amanjha8100/chords/issues) for a list of proposed features (and known issues). Feel free to raise new issues.

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch ( `git checkout -b feature/AmazingFeature` )
3. Add your Changes ( `git add .` )
4. Commit your Changes ( `git commit -m 'Add some AmazingFeature'` )
5. Push to the Branch ( `git push origin feature/AmazingFeature` )
6. Open a Pull Request

<!-- LICENSE -->

## License

Distributed under the MIT License. See [`LICENSE`]() for more information.
