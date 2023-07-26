import requests
def update():
    global token
    head={'Host': 'web2.temp-mail.org','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0','Accept': 'application/json','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate',
        'Authorization': f'Bearer {token}','Origin': 'https://temp-mail.org','Referer': 'https://temp-mail.org/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','Te': 'trailers','Connection': 'close'}
    while True:
        req=requests.get(f'https://web2.temp-mail.org/messages',headers=head)
        print(req.text)
def Crate_Email():
    global token
    head={'Host': 'web2.temp-mail.org','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0','Accept': 'application/json','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Authorization': 'Bearer','Origin': 'https://temp-mail.org','Referer': 'https://temp-mail.org/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','Content-Length': '0','Te': 'trailers','Connection': 'close'}
    req=requests.post(f'https://web2.temp-mail.org/mailbox',headers=head)
    #token=str(req.json()['token'])
    print(req.text)
def main():
    print('By @team1577 ')
main()
