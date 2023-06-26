# Revelio

Revelio is a Python tool for web pentesting.                                                                                                        
As the name suggest, it reveals subdomains, verifies thier are alive, takes screenshots,                                                                                  
checks for potential subdomain takeovers, and finally it pulls archive data for each subdomain.                                                                           
                                     
Revelio combines the following GO tools:                                                                                                                                  
                                                                                                                                                                          
<>  subfinder     https://github.com/projectdiscovery/subfinder (requires GO V1.19 and higher)                                                                            
<>  assetfinder   https://github.com/tomnomnom/assetfinder                                                                                                                
<>  httprobe      https://github.com/tomnomnom/httprobe                                                                                                                   
<>  subjack       https://github.com/haccer/subjack                                                                                                                       
<>  waybackurls   https://github.com/tomnomnom/waybackurls                                                                                                                
<>  gowitness     https://github.com/sensepost/gowitness                                                                                                                  
                                          
                                                                                                                                                                
Make sure you have all these tools installed, and you can find them on the command line.                                                                                  

                                                                                                                                                                      
Also, revelio uses the 'colorama' python package, if for some reason you get 'ModuleNotFound'                                                                             
error please use pip to install it, (i use python 3.11 and i didnt have to install it manually,                                                                           
running a clean env with no installs also works for me) If you dont want to install colorama                                                                              
on your system, you can spin off an env and install it there, then delete it:)                                                                                            
                                                                                                                                                                       
                                          
P.S Shoutout to Heath Adams for the idea!                                            
                                                                                                                                                                          

## Installation                                                                      
                                          
Just copy the script to your current working directory.                                                                                                                   

```bash                                   
wget https://github.com/DanielIsaev/revelio/revelio.py                                                                                                                    
```                                       

chmod it.                                 

```bash                                   
chmod +x revelio.py                       
```                                       

And you should be good to go.                                                        


## Usage                                  

Just supply the top level domain you wish to scan, and revelio will find all it's subdomains.                                                                             
(Make sure it fits the scope of your pentest)                                        

```bash                                   
python3 revelio.py example.org                                                       
```                                       

After about 5 min it should be done, the more cores you have the better though.                                                                                           


## Contributing                           

Pull requests are welcome. For major changes, please open an issue first                                                                                                  
to discuss what you would like to change.                                            

Please make sure to update tests as appropriate.                                     


## Lets link up!                          

You can always reach me on my [Linkedin](https://www.linkedin.com/in/daniel-isaev-757593228/)  
