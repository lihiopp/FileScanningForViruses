# Virus Detection in Downloaded Files
Scans downloaded files for viruses by using VirusTotal.com 's API.
____________________________________________________________________

## Implementation
 - A client-server type of network (TCP connection).
 - Scanning is done on VirusTotal.com, which provides a report.

The client is constantly looking for changes in the 'Downloads' directory, particulary for the creation of new files.
It sends every file that had downloaded to the server, which sends it to VirusTotal.com.
The server gets the results from the site, and sends it back to the client, which saves them in answers.txt.

## Description & Details
 - **Server.py:** gets files from the client, uses vtScanning.py functions to send them to VirusTotal.com and get the result. Then it sends it back to the client.
 - **vtScanning.py:** contains functions called and executed by the server. These use VirusTotal.com's API to send files and get the site's report on them in JSON format. The site runs multiple antivirus programs on the file, if one or more return a positive result then the file is probably malicious. A public API key is needed to perform the process, it is given after registrying to the site.
 - **Client.py:** 
   1) In order to not lose any file that is downloaded while the client is sending files to the server, it runs a thread that executes NotifyChanges.py. The thread passes a list of files as an argument, the executed program constantly adds its output - the downloaded files' names - to the list. This is a 'queue' of files that are waiting to be sent to the server. 
   
   2) In the main thread the client sends the files', one by one, to the server, while removing them from the queue. Only after it gets the result for one, it goes on to send another. Videlicet, the client is constantly monitoring the directory, while sending files at the same time.
 - **NotifyChanges.py:** gets the files queue. It monitors the 'Downloads' directory for changes in file names (and creation of new ones) using ```win32file.readdirectorychanges()```. Each time there is one (or more) it saves the new file's name in queue.


## Remarks
The whole thing happens simultaneously, but also in a ***FIFO*** approach - it is both synchronous and Asynchronous;
the client is checking for changes in the directory all the time, handles a queue of the downloaded files and keeps sending them one by one.
The server sends them to VirusTotal.com, gets the answer and sends it back to the client - only after the result for a file is received, the client sends another. That way no file gets lost on the way. Also, installing the pywin package is needed.

![image](https://user-images.githubusercontent.com/93098326/149233964-c55d83eb-6e7f-41a2-aa13-5a2b8e7469e4.png)

