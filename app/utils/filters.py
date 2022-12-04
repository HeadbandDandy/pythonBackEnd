


# below will be functions set for filtering through data
def format_date(date):
    return date.strftime('%m/%d/%y')

from datetime import datetime 
# print(format_date(datetime.now()))

# below contains function to format and filter URL
# below removes extra information from url leaving only domain name
def format_url(url):
    return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]


# Test for above function
# print(format_url('http://google.com/test/'))


# below contains function to format plural words
def format_plural_words(amount, word):
    if amount != 1:
        return word + 's'

    return word

# below tests for above function
# print(format_plural_words(2, 'cat'))
# print(format_plural_words(1, 'dog'))
# print(format_plural_words(5, 'elephant'))