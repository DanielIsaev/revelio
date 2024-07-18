# Revelio

Revelio is a Python script which acts as a wrapper around a few tools used to enumerate a target website. 
The benefit with using Revelio is that it utilizes multi-threading in order to run the tools concurrently, while saving the output in a structured directory layout.

P.S Shoutout to Heath Adams for the idea!

## Features

- Locates and verifies subdomains.
- Takes a screenshot of each domain.
- Checks for potential subdomain takeovers.
- Pulls archive data from the wayback machine for each subdomain.
- Uses multi-threading for concurrency.
- Saves the resulsts in a structured directory tree.

## Integrated Tools

Revelio combines the following GO tools:                                                                                                                                  

-  [subfinder](https://github.com/projectdiscovery/subfinder)
-  [assetfinder](https://github.com/tomnomnom/assetfinder)
-  [httprobe](https://github.com/tomnomnom/httprobe)
-  [subjack](https://github.com/haccer/subjack)                                                                                                                       
-  [waybackurls](https://github.com/tomnomnom/waybackurls)
-  [gowitness](https://github.com/sensepost/gowitness)

## Dependencies and Installtion Guide

First you need to have GO installed on your system. This is fairly easy to do on Kali:

```bash
sudo apt install golang-go
```

If this doesnt work for you, I suggest following the action plan in [this medium blog post](https://medium.com/@yadav-ajay/go-lang-on-kali-linux-5cc40a78d7de).

Next, we need to have the above listed tools installed as well. Most of them can be easily installed using Kali's apt repositories:

```bash
sudo apt install subfinder
sudo apt install assetfinder
sudo apt install httprobe
sudo apt install gowitness
```

In order to install `waybackurls` you can run the following:

```bash
go install github.com/tomnomnom/waybackurls@latest
sudo cp ~/go/bin/waybackurls /usr/local/bin
```

This should get you all the core tools used be revelio.

At this point you can clone the repo to you machine:

```bash                                   
git clone https://github.com/DanielIsaev/revelio; cd revelio
pip install -r requirements.txt
```

At this point I should mention that revelio also uses the `colorama` Python module for colored output, If you dont want to install it on your system, I recommend setting an env and installing it there as such:

```bash
python3 -m venv py_venv
source py_venv/bin/activate
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
