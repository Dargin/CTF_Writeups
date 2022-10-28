Lets run the file we got. We see that it says the ghost was trapped in a box and it's invisible can we read it?

For this one i just used strace and you can see the flag in the output.

```
strace -v -s 100 ./ghost
```
