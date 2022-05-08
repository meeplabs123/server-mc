# How to start
First, use the `./ngrok authtoken <your authtoken>` command to log-in to ngrok. You'll get your authtoken [here](https://dashboard.ngrok.com), after this step, type `./ngrok tcp 25565` and the tunneling is ready-to-use.

Now, you need to start the server jar, it's named `paper.jar`, to start it, just use the JVM command, `java -jar (jarName).jar`.

The server IP will starts with `tcp://<ip here>`, remove the `tcp://` and share it to your friends.

**If you use Minecraft non-official from Mojang, set `online-mode` to false in `server.properties` file.**
