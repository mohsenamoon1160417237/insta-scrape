import requests

response = requests.get("https://i.instagram.com/api/v1/feed/user/nasa/username/?count=12", headers={
    "Cookie": 'mid=YmmiJQAEAAEXpsOpiZ5yDoo2jDGX; ig_did=D16C8886-440C-4EF7-8900-4DB0AF88296F; fbm_124024574287414=base_domain=.instagram.com; datr=U66oYlOl5cYlUBdFMPgnlaj0; dpr=2; shbid="3795\05421521616339\0541696946478:01f7e2fcf3e262a6238b5e45a9159f5f6ced47f9496540c5751d1316ecab27016d4ec011"; shbts="1665410478\05421521616339\0541696946478:01f7d8285d1ad743de3688999a9788f7158f3ca6b29a695d77373d452e58cbea659dfa93"; rur="ASH\05450013247083\0541697000324:01f7226487d6a95ddb15edb5cbad08480294810639a1dd127d88211d6a4673f37e0ee48c"; csrftoken=0KKy0xOBB3wk2qLWgSqmAJMGdHQSZdOV; ds_user_id=50013247083; sessionid=50013247083%3ArpHDLWGxkyjPNQ%3A26%3AAYfR27xUPpNViFrCwJic9T1Bi64j5iP8SMca4cx7gg',
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0",
    "X-CSRFToken": "0KKy0xOBB3wk2qLWgSqmAJMGdHQSZdOV",
    "X-IG-WWW-Claim": "hmac.AR2LMXsxt1XmLg8qo84A2V0GYSiQ3HyhOO1jSgqwx4ak6sPp",
    "Connection": "keep-alive",
    "X-ASBD-ID": "198387",
    "X-IG-App-ID": "936619743392459",
    "X-Instagram-AJAX": "1006362082"
})

for k, v in response.json().items():
    print(k, v)
