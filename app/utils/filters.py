


# below will be functions set for filtering through data
def format_date(date):
    return date.strftime('%m/%d/%y')

from datetime import datetime 
print(format_date(datetime.now()))

# below contains function to format and filter URL
# below removes extra information from url leaving only domain name
def format_url(url):
    return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]
