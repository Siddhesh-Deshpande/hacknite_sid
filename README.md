# hacknite_sid

This is a project based on webscraping with the help of beautiful soup.
The project gives you a sorted list of running shoes that are available on the flipkart and ebay website. you just have to enter the brand which you are looking for.
The project is useful in day to day life as it helps us save a lot of time , we get do not have to waste a lot of time on searching through different websites searching for the cheapest possible options.
To get started with this you need to have following things installed:
1. Python version 3.6 or higher
2. bs4 library(pip install bs4)
3. requests library(pip install requests)
4. urllib.parse library

to use this one just needs to download the ws.py file and the result.txt from this repository and make sure to keep them in same directory
to run this file:
1.open the terminal
2.change the curerent directory to the directory where you have downloaded the files
3.type the command python3 ws.py
4. give the name of brand whose running shoes you want to search for(Eg-> Nike,adidas)
5. after this wait for program to be exceuted completely
6. then open the result.txt file this contain name of shoes , link to buy them(link of website they are on), prices in increasing order.

Making of the project:
the project is made using beautifulsoup library,requests library and urllib.parse library of python. 
a script is written that scrapes the prices,name and url to access product from the website of flipkart and ebay the popular e commerce platforms. then the data is sorted and stored in a file using file I/O concept. 

Contributor - Siddhesh Deshpande
