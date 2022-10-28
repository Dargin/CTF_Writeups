For this challenge we're given another pcap file. Opening it up we see a bunch of dns request.
![image](https://user-images.githubusercontent.com/6153549/198596839-9c378e22-7278-4561-a412-f1ac47a3f85d.png)
The first thing i noticed with this is that the first part looks like HEX, so i took the firs string and put it into hex to ascii translator to see it starts with PK - if we look up magic bytes we see that this generally maps to a zip file.

![image](https://user-images.githubusercontent.com/6153549/198597750-036ab17a-aebe-4c6d-9a14-13e51ac93970.png)

So the thought was we need to get the first part of the dns query, link it all together, then convernt the hex to a file. In Wireshark i first applied a filter to only show me the source IP (if you look you get a response for each query duplicating data, so by doing this i remove the duplicates.

![image](https://user-images.githubusercontent.com/6153549/198598437-f2de90fa-9809-41ef-a278-f858a4a5ddfd.png)

Then export the data into csv format (export packet dissections)

![image](https://user-images.githubusercontent.com/6153549/198599457-772ad389-a7ce-424d-8ac4-aaca5c608ae0.png)

Export the displayed packets into CSV format. Next we neeed to cut out just the first part of each dns query, remove any extra spaces, and remove the new line so we just get a string of hex. Here is what I did.

```
awk -F "," '{print $7}' test.csv | awk -F "." '{print $1}' | sed -e 's/^"//' | tr -d '\n\ >> hex.txt
```

This gave me just a string of hex, now using XXD converted it to a zip file.

```
xxd -r -p hex.txt file.zip
```

After looking at the zip you'll see some xls data; and looking back at the magic bytes - those can be for zip or for excel files, this looks like excel so do it one more time then open and read the file.

```
xxd -r -p hex.txt file.xls
```
