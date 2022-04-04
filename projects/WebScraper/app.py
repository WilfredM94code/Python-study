# This web scraper bot will get the last 10 questions from StackOverflow
# For this there will be used the 'requests' and 'bs4' modules

import requests
from bs4 import BeautifulSoup

url = 'https://stackoverflow.com/questions'

response = requests.get(url)
print('type(response) = ', type(response))
# This object is a <class 'requests.models.Response'>. It has several attributes

text_response = response.text
# This attribute returns a string containing the whole HTML data

soup = BeautifulSoup(text_response, 'html.parser')
print('type(soup) = ', type(soup))
# The 'BeautifulSoup()' object recieves a string and a instruction to deal with that string
# Such string, in this case a HTML string, is passed through an html parser and it returns
# an object type <class 'bs4.BeautifulSoup'>

questions = soup.select('.s-post-summary')
# The 'select()' method recieves a string containing a CCS class

print('type(questions) = ', type(questions))
# This object contains a lot of data contained under the '.s-post-summary' CSS class
# This is an iterable. Any value stored in this iterable is related to the CSS class
# and within this label

print('questions[0] = ', questions[0])
print('type (questions[0]) = ', type(questions[0]))
# Every itterable is a <class 'bs4.element.Tag'> object
# This object returns every content withn the '.s-post-summary' tag

print('questions[0].attrs = ', questions[0].attrs)
print('type (questions[0].attrs) = ', type(questions[0].attrs))
# This attribute 'attrs' gets every attribute or data related with the particular tag

print("questions[0].select_one('.s-link') = ",
      questions[0].select_one('.s-link'))
print("type(questions[0].select_one('.s-link')) = ",
      type(questions[0].select_one('.s-link')))
# The 'select_one ()' method recieves a string with the CSS class name and returns a <class 'bs4.element.Tag'>

print(questions[0].select_one('.s-link').get_text())
# The 'get_text()' converts the tag and converts it into a string

questions[0].select_one('.s-link').get('href')
# The 'get()' method recieves a string with the name of the attribute returns the value associated it

for count, question in enumerate(questions):
    print('Question ', count)
    print(question.select_one('.s-link').get_text())
    print(question.select_one('.s-post-summary--content-excerpt').get_text().replace(
        '                ', '').replace('...', '').replace('\n', '').replace('            ', ''))
    print('Link ', url + question.select_one('.s-link').get('href'), '\n')
