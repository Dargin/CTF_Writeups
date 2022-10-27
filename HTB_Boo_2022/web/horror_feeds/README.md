As the same with the others; download the files and lets take a look. Spinning up the docker we see a page asking for login and then allowing us to register. Registering a user lets us login and see the camera feeds. Nothing to crazy, lets dig into the code.

Looking at database.py we can see the function for logging in and registering a user. The login is turning the username into a string and the first part of the register is doing the same, however we can see when it creates the user the command is not sanitizing our input, that looks like our injection point.

After trying with a few different UPDATE statements that didn't work (it gave errors that you cannot mix those types of sql commands); did some research and found that INSERT INTO will overwrite values.

Next issue was that trying to insert a password it would fail if it wasn't in the right format, you can see this util.py verify_hash; where when logging in it has to decrypt the password. To get the password I registered and account but got it to leak the password with:

```
{"username":"test1\"","password":"123"}
```

As the password is hashed first, then attempted to be injected, this will leak the hashed password vaule for 123

![image](https://user-images.githubusercontent.com/6153549/198417340-0eb4cc41-5462-4338-9f8d-ecd513245818.png)

After working around that started to get an error about duplicate key and found that with insert into, if there is a duplicate key you can force the variable to be something specific. So my final payload looked like:
```
{
"username":"gs3\",\"$2b$12$HS6k7taSvyvJc6RqqCBZ/OfEfkf3OyGgr0MhgkFXnh69gcSulPDp.\"),(\"admin\",\"$2b$12$HS6k7taSvyvJc6RqqCBZ/OfEfkf3OyGgr0MhgkFXnh69gcSulPDp.\") ON DUPLICATE KEY UPDATE password=\"$2b$12$HS6k7taSvyvJc6RqqCBZ/OfEfkf3OyGgr0MhgkFXnh69gcSulPDp.\" --",
"password":"123"
}
```
This sends two things to get inserted, one for my user gs3, and one for admin, setting both to a password of 123. If a duplicate key is found (i.e. admin) then update it's password.

login as admin and get your flag!
