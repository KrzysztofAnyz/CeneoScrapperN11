import  requests

respons = requests.get("https://www.ceneo.pl/71299205#tab=reviews")

print(respons.text)