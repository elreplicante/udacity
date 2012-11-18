'''
Created on 22/06/2012

@author: repli
'''
import cgi
months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

month_abbvs = dict((m[:3].lower(), m) for m in months)

def valid_month(month):
    if month:
        short_month = month[:3].lower()
        return month_abbvs.get(short_month)
        
def valid_day(day):
    if day:
        if day >= '0' and day <= '31':
            return int(day)
        
def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if year >= 1900 and year <= 2020:
            return year
given_string = "I think %s and %s are perfectly normal things to do in public."
    
def sub1(s):
    return given_string % s

given_string2 = "I think %s and %s are perfectly normal things to do in public."
def sub2(s1, s2):
    return given_string2 % (s1, s2)

given_string2 = "I'm %(nickname)s. My real name is %(name)s, but my friends call me %(nickname)s."
def sub_m(name, nickname):
    return given_string2 % {'name': name, 'nickname' : nickname}


def escape_html(s):
    return cgi.escape(s, quote = True)



s = """
<form method="post">
    What is your birthday?
    <br>
    <label> Month
        <input type="text" name="month" value="%(month)s">

    </label>
    <label>Day
        <input type="text" name="day" value="%(day)s">
    </label>
    <label>Year
        <input type="text" name="year" value="%(year)s">
    </label>
    <div style="color: red">%(error)s</div>
    
    
    <br>
    <br>
    <input type="submit">
    </form>
    """
s = escape_html(s)
print s