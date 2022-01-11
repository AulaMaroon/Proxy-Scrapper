import requests
import os


def setting():
    print('Enter Proxy Type')
    print()
    os.system('cls')
    proxy_type = input('HTTP, SOCKS4, SOCKS5, All (Default HTTP) : ').lower()
    accepted_type = ['http', 'socks4', 'socks5', 'all']
    if not proxy_type:
        proxy_type = 'http'
    else:
        if proxy_type in accepted_type:
            proxy_type = proxy_type
        else:
            raise Exception('Invalid Type')
           
    os.system('cls')
    max_timeout = input('Enter Maximum Timeout (Default 10000) : ')

    if not max_timeout:
        max_timeout = '10000'
    else:
        max_timeout = int(max_timeout)
        if max_timeout > 10000:
            raise ValueError('Maximum Timeout Exceeded Expeded 10000')
        else:
            max_timeout = str(max_timeout)
    
    os.system('cls')
    print('Anonymity Type')
    print('1. Elite')
    print('2. Anonymous')
    print('3. Transparent')
    print('4. All')
    print()
    anonymity_type = input('Select Anonymity Type (Default All) : ')
    if not anonymity_type:
        anonymity_type = 'all'
    else:
        anonymity_type = int(anonymity_type)
        if anonymity_type == 1:
            anonymity_type = 'elite'
        if anonymity_type == 2:
            anonymity_type = 'anonymous'
        if anonymity_type == 3:
            anonymity_type = 'transparent'
        if anonymity_type == 4:
            anonymity_type = 'all'
        if anonymity_type > 4:
            raise ValueError('Expected  Input 1 - 4')
    os.system('cls')
    return proxy_type, max_timeout, anonymity_type

def grabber():
    proxy_type, max_timeout, anonymity_type = setting()
    if proxy_type == 'all':
        http = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout='+ max_timeout +'&country=all&ssl=all&anonymity=' + anonymity_type)
        socks4 = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout='+ max_timeout +'&country=all&ssl=all&anonymity=' + anonymity_type)
        socks5 = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout='+ max_timeout +'&country=all&ssl=all&anonymity=' + anonymity_type)
        if (http.status_code == 200):
                with open('http.txt', 'wb') as f:
                    f.write(http.content)
        if (socks4.status_code == 200):
                with open('socks4.txt', 'wb') as f:
                    f.write(socks4.content)
        if (socks5.status_code == 200):
                with open('socks5.txt', 'wb') as f:
                    f.write(socks5.content)
    else:
        response = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol='+ proxy_type +'&timeout='+ max_timeout +'&country=all&ssl=all&anonymity=' + anonymity_type)
        if (response.status_code == 200):
            with open(proxy_type + '.txt', 'wb') as f:
                f.write(response.content)   

grabber()