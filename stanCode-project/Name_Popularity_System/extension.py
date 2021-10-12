"""
File: extension.py
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        ##################
        response = requests.get(url)
        html = response.text

        soup = BeautifulSoup(html)
        table = soup.find('table', {'class': 't-stripe'})
        tbody = table.find('tbody')
        trs = tbody.find_all('tr')

        total_male = 0
        total_female = 0
        for i in range(len(trs)-1):
            tr = trs[i]
            tds = tr.find_all('td')
            male_text = tds[2].text
            female_text = tds[4].text
            male_num = ''                           # 為了去掉逗點，重串
            for j in range(len(male_text)):
                if male_text[j].isdigit():
                    male_num += male_text[j]
            female_num = ''                         # 為了去掉逗點，重串
            for k in range(len(female_text)):
                if female_text[k].isdigit():
                    female_num += female_text[k]
            total_male += int(male_num)
            total_female += int(female_num)
        print(f"Male Number: {total_male}")
        print(f"Female Number: {total_female}")
        ##################


if __name__ == '__main__':
    main()
