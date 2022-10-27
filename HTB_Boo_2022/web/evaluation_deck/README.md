For this web challenge we are given the code and docker image to test with. If we spin up the docker image we see a card game, flipping the cards will either give you more or less life. Hooking up the site to Burp will also help understand the calls, in this case there is only one to /api/get_health that is passing a json payload with your current health, attack power, and an operator (+ or -). You can modify the operator to always give you health, but doing that doesn't win the game.

So now that we know what the application is doing lets take a quick look at the code. The main area we'll want to focus on is the routes.py - this file shows us what's going on behind the scenes, so lets look at the /get_health call.

![image](https://user-images.githubusercontent.com/6153549/198292197-f733520b-bf3c-4172-a881-3fb02cb6aa36.png)

So we see the data getting pulled from the JSON, and if we look at the code = line we can see that the current_health and attack_power are forced to be an integer, however the operator is not.

What exec() does in python is execute a string, so basically it's building a string, executing that string and the result is equal to the result. So by default the string will be something like:

current_health = 45
attack_power = 30
operator = '+'
result = 45 + 30

So this is a clear python injection. We can seperate commands with the ';' operator. However, if we do something like:

result = 45;open('/flag.txt');30

result will be set to 45 and the flag will open but not be assigned to anything. Again this is python so we can just set the result again like:

result = 45;result = open('/flag.txt');30

On this screen this will now show that result is equal to a file object but not print the line, we'll lets do one last modification to read the file.

![image](https://user-images.githubusercontent.com/6153549/198293217-f87dbee7-fd19-4b15-bf2e-077ba820ab66.png)
