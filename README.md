# How to start
First, set a new environment variable called 'NGROK' with your ngrok authtoken as the value. You'll get your authtoken [here](https://dashboard.ngrok.com).

Next, set another called 'DISCORD' with a discord bot token as the value. You can create a bot [here](https://discord.com/developers/applications).

Now, you need to start the server, run the file named 'start.bash' for a fully automated run. This includes hosting a local server with the server ip as the content, and your discord bot showing the ip as it's status.

**That's It! You server is up and running.**

# Author's Notes
This is designed for [gitpod.io](https://gitpod.io), so the jdk autoinstaller will only work there.
If you use other services, you will have to install a working jdk manually and remove the jdk autoinstaller in init.sh.

Only works on linux.