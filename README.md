<div align="center"><a href="https://hacktoberfest.digitalocean.com/"><img src="https://hacktoberfest.digitalocean.com/_nuxt/img/logo-hacktoberfest-full.f42e3b1.svg" alt="Banner" width="60%"/></a></div>

<!-- PROJECT LOGO -->
<br />
<p align="center">
    <img src="./Logo/icon.png" alt="Logo" width="40%">

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
    .
    <a href="https://github.com/amanjha8100/chords/blob/main/doc/deploy.md">Deploy Walkthrough</a>
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
    <li><a href="#configuration---discord-developer-portal">Configuration - Discord Developer Portal</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
<img align="left" src="https://github.com/Yoda-Canada/chords/blob/issue-32/icon/Toicon-icon-fandom-annoy.svg.png" width="50px" height="50px" />

## About The Project

Most of the Discord Music Bots are down. They got banned, unfortunately.\
So we thought of making our own Discord Music Bot for our Discord Community.

<img align="left" src="https://github.com/Yoda-Canada/chords/blob/issue-32/icon/note.png" width="30px" height="30px" />

### Built With

- [Python](https://www.python.org/)
- [discord.py](https://discordpy.readthedocs.io/)
- [FFmpeg](https://www.ffmpeg.org/)
- [youtube_dl](https://pypi.org/project/youtube_dl/)

<!-- GETTING STARTED -->
<img align="left" src="https://github.com/Yoda-Canada/chords/blob/issue-32/icon/Toicon-icon-fandom-charm.svg.png" width="50px" height="50px" />

## Getting Started

To get a local copy up and running follow these simple steps.

<img align="left" src="https://github.com/Yoda-Canada/chords/blob/issue-32/icon/note.png" width="30px" height="30px" />

### Prerequisites

  **You should have Python and FFmpeg installed in your system if not then don't worry the installation file will get you everything if you are using a windows machine**
- Active internet connection through out installation (Must)
- Python3   (Must for Other Users)
- FFmpeg    (Must for Other Users)

<img align="left" src="https://github.com/sagarkumar3105/chords/blob/1bb1bd0e28adabdd1d76ee3bbbc40f3befc2314e/icon/1.png" width="30px" height="30px" />

### Installation for Windows users

1. Download the installation file from this [link](https://downgit.github.io/#/home?url=https://github.com/sagarkumar3105/chords/blob/e1d9a2aa24a5f2bca807466e3f08ee1eca72aa4e/installer.bat).
2. Right click on the downlaoded file and run it as administrator.
3. Create a Bot from the Discord Developer Portal and copy the Bot token. Create a `.env` file and paste the Token.

   ```sh
   TOKEN = "Your Token"
   ```

4. Invite the Bot to your server and run

   ```sh
   python app.py
   ```
*\*Incase you are unable to install with above instructions then follow the Instructions for other users*

<img align="left" src="https://github.com/sagarkumar3105/chords/blob/b29d6e853ad9a70a33efdffd4da4c7763b96cbb6/icon/linux-logo.png" width="30px" height="30px" />

### Installation for other users

1. Fork the project first

2. Clone this repo on your local machine
   ```sh
   git clone https://github.com/amanjha8100/chords
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
 
<!-- CONFIGURATION - DISCORD DEVELOPER PORTAL -->
<img align="left" src="https://github.com/Yoda-Canada/chords/blob/issue-32/icon/Toicon-icon-fandom-steal.svg.png" width="50px" height="50px" />

## Configuration - Discord Developer Portal

Go to the [Discord Developer Portal](https://discord.com/developers/docs/intro) to create your application and bot. You must give the following permissions:

- Server Members Intent ✔️
- Text Permissions:
  - Send Messages ✔️
  - Read Message History ✔️

<img align="left" src="https://github.com/Yoda-Canada/chords/blob/issue-32/icon/Toicon-icon-fandom-rap.svg.png" width="50px" height="50px" />

## Available Bot Commands

```
_p : Plays the song with search keyword following the command
_cp: Shows the currently playing song
_pn : Moves the song to the top of the queue
_pause : Pause the currently playing song
_resume : Resume the currently playing song
_q : Shows the music added in list/queue
_qt : Shows the total time of music in the list/queue
_s : Skips the currently playing music
_r : removes song from queue at index given.
_l : Commands the bot to leave the voice channel
_help : shows all the commands of the bot.
_rep : Repeats the current playing song
_sleep : To set timer.
```
<!-- REQUIRED ROLES -->
 <img align="left" src="https://github.com/Yoda-Canada/chords/blob/issue-32/icon/Toicon-icon-fandom-submerge.svg.png" width="50px" height="50px"  />

## Required roles

To run some of the commands, the user must have some specific roles. The following table illustrates the roles which are necessary for running specific commands. If a command is ticked for more than one role, then this means that both roles have the permission for running the command.

| Command | DJ  |
|:-|:-:|
| `play` | |
| `playing` | |
| `queue` | |
| `clear` | |
| `shuffle` | |
| `skip` | |
| `voteskip` | |
| `leave` | :white_check_mark: |
| `pn` | :white_check_mark: |
| `pause` | :white_check_mark: |
| `resume` | :white_check_mark: |
| `remove` | :white_check_mark: |
| `restart` | :white_check_mark: |
| `queuetime` | :white_check_mark: |
| `help` | |

<!-- ROADMAP -->
 <img align="left" src="https://github.com/Yoda-Canada/chords/blob/issue-32/icon/Toicon-icon-fandom-drop.svg.png" width="50px" height="50px"  />

## Roadmap

See the [open issues](https://github.com/amanjha8100/chords/issues) for a list of proposed features (and known issues). Feel free to raise new issues.

<!-- CONTRIBUTING -->
 <img align="left" src="https://github.com/Yoda-Canada/chords/blob/issue-32/icon/Toicon-icon-fandom-shred.svg.png" width="50px" height="50px" />

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch ( `git checkout -b feature/AmazingFeature` )
3. Add your Changes ( `git add .` )
4. Commit your Changes ( `git commit -m 'Add some AmazingFeature'` )
5. Push to the Branch ( `git push origin feature/AmazingFeature` )
6. Open a Pull Request

<!-- LICENSE -->
 <img align="left" src="https://github.com/Yoda-Canada/chords/blob/issue-32/icon/Toicon-icon-fandom-sound.svg.png" width="50px" height="50px" />

## License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.
