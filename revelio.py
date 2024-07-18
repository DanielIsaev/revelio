#!/usr/bin/python3

from colorama import init as colorama_init
from colorama import Fore
import os
import signal
import sys
import subprocess
from multiprocessing import Pool
import re

try:
    domain = sys.argv[1]
except IndexError:
    print_banner()
    print(f'Usage: {sys.argv[0]} <domain>')
    sys.exit()

def sigint_handler(signal, frame):
    os.system(f'rm -rf {domain}')
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

colorama_init()

# Print banner
def print_banner():
    print('\n')
    print(f'{Fore.RED}@@@@@@@  @@@@@@@@ @@@  @@@ @@@@@@@@ @@@      @@@  @@@@@@')
    print(f'{Fore.RED}@@!  @@@ @@!      @@!  @@@ @@!      @@!      @@! @@!  @@@')
    print(f'{Fore.RED}@!@!!@!  @!!!:!   @!@  !@! @!!!:!   @!!      !!@ @!@  !@!')
    print(f'{Fore.RED}!!: :!!  !!:       !: .:!  !!:      !!:      !!: !!:  !!!')
    print(f'{Fore.RED} :   : : : :: :::    ::    : :: ::: : ::.: : :    : :. :') 
    print(f'{Fore.WHITE}\n')

print_banner()

# Create the output directory tree
print(f'{Fore.BLUE}[+] {Fore.WHITE}Bulding output directory layout')
root_dir = os.path.join(os.getcwd(), domain)
if not os.path.exists(root_dir):
    os.mkdir(root_dir)

alive_dir = os.path.join(root_dir, 'alive')
if not os.path.exists(alive_dir):
    os.mkdir(alive_dir)

jack_dir = os.path.join(root_dir, 'potential_takeovers')
if not os.path.exists(jack_dir):
    os.mkdir(jack_dir)

wayback_dir = os.path.join(root_dir, 'waybackurls')
if not os.path.exists(wayback_dir):
    os.mkdir(wayback_dir)

extensions_dir = os.path.join(wayback_dir, 'extensions')
if not os.path.exists(extensions_dir):
    os.mkdir(extensions_dir)

parms_dir = os.path.join(wayback_dir, 'parameteres')
if not os.path.exists(parms_dir):
    os.mkdir(parms_dir)



def hunt_callback(subs):
    '''
    Hunt callback function, clean the url's,
    remove duplicates and add to final result.
    '''

    subs = [url.strip() for url in subs if not url.startswith('*')]
    subs = [url for url in subs if url.endswith(domain)]
    
    for url in subs:
        prefix = url.find('//')
        url = url[prefix+2:]
        if url not in alive:
            alive.append(url)


def hunt(command, *args):
    '''
    Main function to hunt down subdomains  with both assetfinder and subfinder. 
    pass the result to httprob for validation and aggregate the results.
    '''

    global domain

    subs = subprocess.Popen([command, *args], stdout=subprocess.PIPE)
    probed = subprocess.run(['httprobe', '-c', '50', '-t', '500'], 
                            stdin=subs.stdout, stdout=subprocess.PIPE)
     
    return probed.stdout.decode('utf-8').split('\n')


def waybackurls_callback(arch):
    '''
    waybackurls callback function. flatten the list of lists, remove duplicates,
    parse the urls for url parameters and file extensions.
    '''

    def flatten(iterable):
        for item in iterable:
            if isinstance(item, list):
                yield from flatten(item)
            else:
                yield item
    
    arch = [url for url in flatten(arch) if url != ' ']
    arch = list(set(arch))

    parms = [url for url in arch if re.match(r'.+\?.+=', url)]

    for url in arch:
        idx = url.rfind('.')
        suffix = url[idx+1:]
        if suffix in extensions.keys():
            extensions[suffix].append(url)

    archives.extend(arch)
    parameters.extend(parms)


def waybackurls(url):
    '''
    Query the archive machine for inforamtion about all varifed url's. 
    '''

    arch = subprocess.run(['waybackurls'], input=url, stdout=subprocess.PIPE, encoding='utf-8')    
    arch = arch.stdout.split('\n')
    
    return arch


def gowitness(url):
    '''
    Take a screenshot of every verfied url.
    '''

    url = 'https://' + url
    subprocess.run(['gowitness', 'single', url, '--disable-db', '--disable-logging'])


# Create the data strucutres used by the above functions. 
extensions = {'js': [], 'html': [], 'json': [], 'php': [], 'aspx': [], 'txt': []}
parameters = []
archives = []
nmaped = []
alive = []


# Inistiate the deamon pool to run assetfinder and subfinder simultaneosly. 
print(f'{Fore.YELLOW}[+] {Fore.WHITE}Hunting for subdomains...')
with Pool(None) as subs_pool:
    assetfinder = subs_pool.apply_async(hunt, ('assetfinder', domain), 
                                        callback=hunt_callback)

    subfinder = subs_pool.apply_async(hunt, ('subfinder', '-silent', '-d', domain), 
                                     callback=hunt_callback)
    assetfinder.wait()
    subfinder.wait()


# Write the alive subdomains. 
os.chdir(alive_dir)
with open('alive.txt', 'w') as file:
    for url in sorted(alive):
        file.write(url + '\n')


# Run subjack to verify taken-over subdomains.
print(f'{Fore.YELLOW}[+] {Fore.WHITE}Verifying subdomain takeovers...')
jacked = subprocess.run(['subjack', '-w', 'alive.txt', '-t', '100',
                         '-timeout', '30', '-ssl', '-a', '-c', 
                         '/usr/share/subjack/fingerprints.json'], 
                         stdout=subprocess.PIPE)

jacked = jacked.stdout.decode('utf-8')

print(f'{Fore.YELLOW}[+] {Fore.WHITE}Capturing site screenshots...')
print(f'{Fore.YELLOW}[+] {Fore.WHITE}Pulling archive data...')
print('\n')

os.chdir(root_dir)

gowitness_pool = Pool(None)
wayback_pool = Pool(50)

gowitness_task = gowitness_pool.map_async(gowitness, alive)
wayback_task = wayback_pool.map_async(waybackurls, alive, callback=waybackurls_callback)

gowitness_task.wait()
wayback_task.wait()

gowitness_pool.close()
wayback_pool.close()

# Write script results. 
print(f'{Fore.BLUE}[+] {Fore.WHITE}Writing output')

os.chdir(wayback_dir)
with open('archives.txt', 'w') as file:
    for url in sorted(archives):
        file.write(url + '\n')

os.chdir(parms_dir)
with open('parameters.txt', 'w') as file:
    for url in sorted(parameters):
        file.write(url + '\n')

os.chdir(extensions_dir)
for k,v in extensions.items():
    with open(f'{k}_extensions.txt', 'w') as file:
        for url in sorted(v):
            file.write(url + '\n')

if jacked:
    os.chdir(jack_dir)
    with open('potential_takeovers', 'w') as file:
        for line in subjack:
            file.write(line + '\n')
else:
    os.rmdir(jack_dir)

print(f'{Fore.BLUE}[+] {Fore.WHITE}All done! Happy {Fore.RED}hacking:)')
