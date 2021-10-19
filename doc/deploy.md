# Deploying the music bot to a server

This article will follow the steps to deploy the bot to heroku. You can choose to deploy it on any other server you wish. Feel free to add a documentation if you want to deploy it on other hosting services.

## Deployment To Heroku

Before deploying we need our bot token which you can get after creating a new bot for yourself from [Discord Developer Portal](https://discord.com/developers/applications).

Once you have secured your token in a safe place let's move on to deploy our application.

Login to your heroku account and follow the steps :-

1. Fork the project and drop a star :star: .
2. Create a project and name it whatever you want in heroku dashboard.
3. Connect your heroku to your github repository.
4. Set up environmental variables that is your **bot token**.
   1. Go to **settings** --> **config vars** --> Under name add **token** --> paste your token there.
5. Adding buildpacks to heroku,
   1. For this bot you will require three buildpacks.
      1. Python Buildpack (You will get this as an option while choosing buildpack)
      2. [ffmpeg](https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest)
      3. [Opus](https://github.com/xrisk/heroku-opus)
6. Now under the **deploy** section --> choose the repo branch (main in this case) --> click on **deploy branch**.
7. Wait for the build to be successful.
8. To check if everything went as expected, you can click on the left corner dropdown of **more** --> **view logs**.
9. Then go to **Resources** and add appoint your project to a resource.

If you follow the steps, you must have deployed the bot hopefully.

## Currently Available Commands

```
_p, _play : Plays the song with search keyword following the command 
_pn : Moves the song to the top of the queue
_pause : Pause the currently playing song
_resume : Resume the currently playing song
_cp: Shows the currently playing song
_q, _queue : Shows the music added in list/queue
_qt : Shows the total time of music in the list/queue
_cq _clear : Clears the entire queue of songs
_shuffle : Shuffles the entire queue of songs
_s, _skip : Skips the currently playing music
_r, _remove : removes song from queue at index given.
_l, _leave : Commands the bot to leave the voice channel
 _voteskip : Initiates voting from the voice members to skip a song.
_h, _help : shows all the commands of the bot.
_rep : Repeats the current playing song
```

Working on more **new features** such as **seek**, **clearqueue** as I build more.
