import requests
from bs4 import BeautifulSoup
# from fake_useragent import UserAgent
from colorama import Fore, Back, Style
import time

def collect(city_code="2398"):
    chars = '1 2 3 4 5 6 7 8 9 0 A B C D E F G H I G K L M N O P Q R S T U V W X Y Z'
    print(chars)
    letter = input(Fore.LIGHTCYAN_EX + 'Enter the first letter of singer:  ')
    response = requests.get(url=f"https://www.amalgama-lab.com/songs/{letter.lower()}/")
    soup = BeautifulSoup(response.text, "lxml")
    singers = soup.find('ul', class_='g').find_all('li')
    for i, v in enumerate(singers):
        link = v.find('a').text.strip()
        print(Fore.RED + f'{i+1}: {link}')
        time.sleep(0.01)

    letter1 = input(Fore.LIGHTCYAN_EX + 'Choose the number of Singer:  ')

    suffix = singers[int(letter1)-1].find('a')['href']
    print(Fore.RED + singers[int(letter1)-1].text.strip())
    res = requests.get(url=f"https://www.amalgama-lab.com{suffix}")

    soup1 = BeautifulSoup(res.text, "lxml")
    songs = soup1.find('li', class_='active').find_next_sibling().find_all('a')
    print(Fore.RED + f'{len(songs)} songs!')
    for i, v in enumerate(songs):
        print(f'{i+1}: {v.text.strip()}')
        time.sleep(0.01)

    letter2 = input(Fore.LIGHTCYAN_EX + 'Choose the number of song: ')
    print(Fore.RED + f'{songs[int(letter2)-1].text.strip()}')
    suffix1 = songs[int(letter2)-1]['href']
    res1 = requests.get(url=f"https://www.amalgama-lab.com{suffix}{suffix1}")
    
    soup2 = BeautifulSoup(res1.text, 'lxml')
    blocks = soup2.find_all('div',class_='string_container')
    for i in blocks:
        orig = i.find('div', class_='original').text.strip()
        tran = i.find('div', class_='translate').text.strip()
        print(Fore.GREEN + f'{orig}')
        print(Fore.CYAN + f'{tran}')
        time.sleep(0.1)
    print(Fore.MAGENTA + 'Good Bye!\nDeveloped by anvarinho!')
    
def main():
    collect(city_code="1873")

if __name__ == "__main__":
    main()