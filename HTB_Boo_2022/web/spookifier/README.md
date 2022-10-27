Same as the others, download the files which include the source code and a docker image. Spinning up the docker image we see a page that translates our test into spooky test. Another one that seems pretty straightforward with funcationlity. Lets take a look at the code and see what we can figure out.

We see in the routes.py that we call a function in the util.py. One of the first things we see in the util.py is a long mapping of font's. This is important because if there is not a map for a character it will get turned into a space. Font4 is the only one that has special characters and those are limited.

![image](https://user-images.githubusercontent.com/6153549/198296504-6e43f80b-e8c8-456f-8f1d-0e2aad5849a7.png)

so the spookify and change_font seem to just take our text and convert it to the font; so looks like a pretty striaghtfoward injection attack with a limited character set. These applications are written in Flask which means they also use templates to populate data. You can see this by looking in the templates folder at the index.html. Around line 26 you'll see that our output is being called as a variable and injected into the template page.

![image](https://user-images.githubusercontent.com/6153549/198296913-b02a37f3-8528-4099-b250-34873930ba44.png)

So knowing this lets try a basic SSTI (ServerSide Template Injection) to see if it works and then also to try and determine what the language might be. Most of the write-ups will talk about using {{ variable }} -- however as we see in the template, that's not the format being used here. So lets modify the basic injection like this:

${7*'7'}

we see that gives us 7777777 in the output, telling us our injection worked and that the site is using Jinja2. From here we know we can execute python commands, I spent a lot time trying to get injections working from various write-ups but either things weren't loaded (such as config.items()) or they had characters that were not in our list (I'm looking at you _ and []).

Finally after thinking for a bit and clicking that it's just Python I used the same payload as Evaluation deck and boom.

![image](https://user-images.githubusercontent.com/6153549/198299697-4565f237-ed5e-4b96-88eb-6507ab467a05.png)
