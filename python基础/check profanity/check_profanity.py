### http://www.wdylike.appspot.com/?q=
import urllib.request
import re
# urllib.request.urlopen('http://www.wdylike.appspot.com/?q=' + 'shit').read()

def read_text():
    quotes = open('/Users/zenghailong/Desktop/Deep learning/movie_quotes.txt')
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    output = []
    string = re.findall('[a-zA-Z]+', text_to_check)
    # print(string)
    for i in range(len(string)):
        connection = urllib.request.urlopen('http://www.wdylike.appspot.com/?q=' + string[i])
        output.append(str(connection.read()))
    print(output)
    if "b'true'" in output:
        print('Profanity Alert!')
    elif "b'false'" in output:
        print('This document has no curse words!')
    else:
        print('Could not scan the document properly.')
    connection.close()

read_text()