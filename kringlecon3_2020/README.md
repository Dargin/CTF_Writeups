Table of Contents
=========================
<!--ts-->
  * [Uncover Santa's Gift List](#uncover-santas-gift-list)
  * [Investigate S3 Bucket](#investigate-s3-bucket)
  * [Point-of-sale Password Recovery](#point-of-sale-password-recovery)

<!--te-->

# Main Story

## Uncover Santa's Gift List

As you show up at the bottom of the mount, wide eyed and ready to meet Santa, you eye the festive gondola with baited breath. However, before going you first talk to Jingle Ringford to get a bit of information. He tells you there is a Wishlist hidden on the billboard next to the road! You have to know what everyone wants! You download the image by clicking on the billboard and see that there is a swirl over the Wishlist. No fear, you're a cybersecurity expert and these things happen. You start up GIMP and open the image. Being the lazy slacker you are, instead of using the select tool you just simply crop out everything you don't want. Now utilizing the Whril and Pinch distoration feature (found under Filters -> Distorts -> Whirl and Pinch), you begin to spin the image noticing that you need to go negitve on the whirl to get the image to spin in the right direction. Landing on a whirl of -330.4 you finally can read the wishlist and see that Josh Wright is wishing for Proxmark

![image](https://user-images.githubusercontent.com/6153549/116789179-9c9a7680-aa7b-11eb-8517-5696ef7ac6f4.png)

## Investigate S3 Bucket

Now that you've arrived on the mountain you see Santa, bowl full of jelly and all, but he's not laughing. After helping Shinny Upatree he tells you about an issue with the Wrapper3000 and points you to the table beside him. Time to work on some S3 buckets!

Logging into the console we see that the Wrapper3000 is on the fritz (Oh No!), but luckily the bucket finder script is ready to go. First we do a 'cd bucket_finder' and take a look. We see the ruby file and a wordlist. An initial run shows three buckets but all are access denied (sigh). Well looking back at the initial hint, lets add wrapper3000 to the word list. Alright! We see there is a bucket called wrapper3000 and it's open to the public. Now lets run the command './bucket_finder.rb --download wordlist' to download the files from the wrapper3000 bucket.

Now we cd to the wrapper3000 folder and see a file called package. We start by running 'file package' and see it's an ASCII text file, well lets cat that and see what we get. Looking at the text we can identify it as base64, luckily linux lets you decrypt base64 from the console 'cat package | base64 -d' -- this gives us some binary data, looking at the first part for the magic bit we see PK which tells us it's a zipped file. So lets output the results to a file 'cat package | base64 -d > file' -- then we can unzip with 'unzip file'

These give us a new file 'package.txt.Z.xz.xxd.tar.bz2' -- so lets now use 'bzip2 -d package.txt.Z.xz.xxd.tar.bz2' to unzip this new file and get a tar file. Well more unwrapping 'tar -xvf package.txt.Z.xz.xxd.tar'

Now we got an interesting file that ends in xxd - a quick google search tells us this is hex file an there is a specific xxd command, we use that to reverse the file 'xxd -r package.txt.Z.xz.xxd package.txt.Z.xz' and we've got another zipped file, we utilize the xz command to unzip this one 'xz -d package.txt.Z.xz' and we get a final .Z file which is a compressed file. Almost there, one last unwrap with the command 'uncompress package.txt.Z' and we can read the file!
North Pole: The Frostiest Place on Earth

![image](https://user-images.githubusercontent.com/6153549/116791626-93b0a180-aa89-11eb-92e2-7a8b7b4990f1.png)

## Point-of-sale Password Recovery

How terrible! Sugarplum Mary has been locked out of the PoS. Luckily there is an offline copy of the file.

Download it to a linux box, and in Kali right click the file and open with the archive manager!

![image](https://user-images.githubusercontent.com/6153549/117227692-6fd0c100-ade5-11eb-89fa-83e9831cccd2.png)

this will show you files, on the top click "extract" and pick where to save. To make it easier rename the $PLUGINSDIR to something else. Now go into that folder and extract the app-64.7z file.

now go into the new folder and browse into resources, in here you'll find the app.asar

in Kali from the command prompt run 'sudo apt install npm' to install npm if it's not already, then run the command 'sudo npm install -g asar' to install asar, now in the command prompt cd into the directory with the app.asar and run 'asar -extract app.asar sourcecode' - this will give you the source code. Now take a look at the main.js and see the password.

![image](https://user-images.githubusercontent.com/6153549/117227733-824afa80-ade5-11eb-99a5-c6dfc001d37f.png)
