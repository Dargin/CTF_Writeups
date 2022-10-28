Alright download the pcap and lets get started. We see some web traffic, with smaller pcaps like this I like to start by following the tcp stream and then cycle through them to see what's intresting.

![image](https://user-images.githubusercontent.com/6153549/198419536-ca67b6a5-ed10-4236-9940-f6ec8240195f.png)

![image](https://user-images.githubusercontent.com/6153549/198419571-08c96f6f-2826-491b-b556-e18cb78fca56.png)

we can see in stream 0 some web traffic going to /spookhouse/home and the respone. On the bottom right we can cycle through the streams until we come to an interesting one in stream 14. This looks like commands that were ran!

![image](https://user-images.githubusercontent.com/6153549/198419716-fc3f848d-a4fd-4f58-b79f-8084b12f5816.png)

The last part here with the socat shows running a command and exporting it, the echo looks like base64 and it's piped to 'rev' which is reverse.

So reverse that back and base64 decode for the string.
