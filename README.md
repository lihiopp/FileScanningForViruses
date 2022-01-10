# FileScanningForViruses
Scans downloaded files for viruses by using VirusTotal.com 's API.
____________________________________________________________________

Note: This project is aimed to improve my semestrial grade in the Cyber subject.

# How it works
 - A client-server type of network.
 - Reports importing from VirusTotal.com.
The client is constantly checking for changes in the download directory, specifically for the creation of new files there.
It sends every file that had downloaded to the server, which sends it to VirusTotal.com.
The server gets the results from the site, and sends it back to the client, which saves them in answers.txt.

# Remarks
The whole thing happens simultaneously, but in a "first come - first serve" approach; 
the client is checking for changes in the directory all the time, and sends the files once it notices them.
The server handles a queue for these files, sends them to VirusTotal.com, gets the answer and sends it back to the client - each file, turn by turn. That way no file gets lost in the way.
