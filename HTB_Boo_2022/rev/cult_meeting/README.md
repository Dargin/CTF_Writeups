For this challenge we're given an executable file. I like to run them first just to see what's going on. In this case we're prompted for a password and putting in the wrong password prints a failure and closes the door.

![image](https://user-images.githubusercontent.com/6153549/198656648-a5ec25c0-582c-46f1-b838-253a354483e4.png)

I dropped the file in Ghidra and ran the analyze, it's pretty clear from here what the password is, just check out the main function!

![image](https://user-images.githubusercontent.com/6153549/198657196-7794b2c8-dbe2-4a10-be01-3d497f7df8dc.png)

The second part you'll notice is that if the password is right, it runs
```
system("/bin/sh");
```

So if you get the password right it drops you to a shell. From there just run

```
cat /flag.txt
```
