# Revelio

Revelio is a Python script which acts as a wrapper around a few tools used to enumerate a target website. 
The benefit with using Revelio is that it uses multi-threading in order to run the tools concurrently, while saving the output in a structured directory layout.
                                                      

## Features

- Locates and verifies subdomains.
- Takes a screenshot of each domain.
- Checks for potential subdomain takeovers.
- Pulls archive data from the wayback machine for each subdomain

## Integrated Tools

Revelio combines the following GO tools:                                                                                                                                  

-  [subfinder](https://github.com/projectdiscovery/subfinder) (requires GO V1.19 and higher)
-  [assetfinder](https://github.com/tomnomnom/assetfinder)
-  [httprobe](https://github.com/tomnomnom/httprobe)
-  [subjack](https://github.com/haccer/subjack)                                                                                                                       
-  [waybackurls](https://github.com/tomnomnom/waybackurls)
-  [gowitness](https://github.com/sensepost/gowitness)
                                          

                                                                                                                                                                
Make sure you have all these tools installed, and you can find them on the command line.                                                                                  

                                                                                                                                                                      
Also, revelio uses the `colorama` python package, if you get `ModuleNotFound` error please use pip to install it, (i use python 3.11 and i didnt have to install it manually, running a clean env with no installs also works for me) If you dont want to install colorama on your system, you can spin off an env and install it there, then delete it:) 
                                          
P.S Shoutout to Heath Adams for the idea!                                            
                                                                                                                                                                          

## Installation                                                                      

Once you have all the above tools installed, Just copy the script to your current working directory.                                 

```bash                                   
git clone https://github.com/DanielIsaev/revelio; cd revelio
pip install -r requirements.txt
```                                                                          

## Usage                                  

Just supply the top level domain you wish to scan, and revelio will find all it's subdomains.                                                                             
(Make sure it fits the scope of your pentest)                                        

```bash                                   
python3 revelio.py example.org                                                       
```                                       

After about 5 min it should be done, the more CPU cores you have the better though.                 


## Contributing                           

Pull requests are welcome. For major changes, please open an issue first                                                                                                  
to discuss what you would like to change.                                            

Please make sure to update tests as appropriate.                                     


## Lets link up!                          

You can always reach me on my [Linkedin](https://www.linkedin.com/in/daniel-isaev-757593228/)  
