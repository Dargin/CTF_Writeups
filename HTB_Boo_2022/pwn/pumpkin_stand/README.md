Executing the file we see that we got some pumpcoins and can buy a shovel or a laser. The laser is way out of our price range, so of course we gotta have it!

Trying to buy the laser tells we don't have enough coins, makes sense - but our coin also drops to 0 - that's annoying.
![image](https://user-images.githubusercontent.com/6153549/198418176-4983e89a-3748-44bb-8e70-120955ca8a9b.png)

Now try to buy some shovels and it lets us! Our coins are now negative.

![image](https://user-images.githubusercontent.com/6153549/198418219-53318779-d5ed-44a6-80e5-333bc4d5c4fc.png)
with this it seems like we're dealing with an integer overflow; so what i did was

```
1 (shovel)
80 (number of shovels)
2 (laser)
10000 (number of lasers)
```
and there goes our flag!
![image](https://user-images.githubusercontent.com/6153549/198418907-224853f0-9832-42bb-9988-6e22dedf7f45.png)
