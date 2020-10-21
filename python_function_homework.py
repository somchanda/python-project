# 1)
def toKhmerNumeric(number):
    number = "{:,.2f}".format(number)
    number = str(number)
    number = number.replace('1', '១')
    number = number.replace('2', '២')
    number = number.replace('3', '៣')
    number = number.replace('4', '៤')
    number = number.replace('5', '៥')
    number = number.replace('6', '៦')
    number = number.replace('7', '៧')
    number = number.replace('8', '៨')
    number = number.replace('9', '៩')
    number = number.replace('0', '០')
    number = number.replace(',', ' ')
    number = number.replace('.', ',')
    return number


# 2)
def toKhmerDateTime(date):
    import datetime
    tmp = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M')
    date_str = datetime.datetime.strftime(tmp, 'day %d month_str%B year %Y hour %I and%Mmin%p')
    date_str = date_str.replace('day ', 'ថ្ងៃទី')
    date_str = date_str.replace('year ', 'ឆ្នាំ')
    date_str = date_str.replace('month_str', 'ខែ')
    date_str = date_str.replace('hour', 'ម៉ោង')
    date_str = date_str.replace('and', 'និង')
    date_str = date_str.replace('min', 'នាទី')
    date_str = date_str.replace('min', 'នាទី')
    date_str = date_str.replace('PM', 'យប់')
    date_str = date_str.replace('AM', 'ព្រឹក')

    day = ['០', '១', '២', '៣', '៤', '៥', '៦', '៧', '៨', '៩']
    for i in range(10):
        date_str = date_str.replace(str(i), day[i])

    date_str = date_str.replace('January', 'មករា')
    date_str = date_str.replace('February', 'កុម្ភៈ')
    date_str = date_str.replace('March', 'មីនា')
    date_str = date_str.replace('April', 'មេសា')
    date_str = date_str.replace('May', 'ឧសភា')
    date_str = date_str.replace('June', 'មិថុនា')
    date_str = date_str.replace('July', 'កក្កដា')
    date_str = date_str.replace('August', 'សីហា')
    date_str = date_str.replace('September', 'កញ្ញា')
    date_str = date_str.replace('October', 'តុលា')
    date_str = date_str.replace('November', 'វិច្ឆិកា')
    date_str = date_str.replace('December', 'ធ្នូ')

    return date_str


print(toKhmerDateTime('2020-01-23 21:59'))


# 3)
def isNumeric(string):
    string = str(string)
    string = string.replace('.', '')
    return string.isnumeric()


print(isNumeric('78833.283'))

# 4)
one = ["", "one ", "two ", "three ", "four ",
       "five ", "six ", "seven ", "eight ",
       "nine ", "ten ", "eleven ", "twelve ",
       "thirteen ", "fourteen ", "fifteen ",
       "sixteen ", "seventeen ", "eighteen ",
       "nineteen "]

ten = ["", "", "twenty ", "thirty ", "forty ",
       "fifty ", "sixty ", "seventy ", "eighty ",
       "ninety "]


def numToWords(n, s):
    str = ""

    if n > 19:
        str += ten[n // 10] + one[n % 10]
    else:
        str += one[n]

    if n:
        str += s

    return str


def convertToWords(n):
    out = ""

    out += numToWords((n // 10000000),
                      "crore ")

    out += numToWords(((n // 100000) % 100),
                      "lakh ")

    out += numToWords(((n // 1000) % 100),
                      "thousand ")

    out += numToWords(((n // 100) % 10),
                      "hundred ")

    if n > 100 and n % 100:
        out += "and "

    out += numToWords((n % 100), "")

    return out


def readAsEnglishText(num):
    num = str(num)
    isFloat = num.find('.')
    if isFloat == -1:
        return convertToWords(int(num))
    else:
        first, second = num.split('.')
        return convertToWords(int(first)) + ' point ' + convertToWords(int(second))


print(readAsEnglishText(49383.1))


# 4)
def readAsKhmerText(number):
    number = str(number)
    number = number.replace('1', '១')
    number = number.replace('2', '២')
    number = number.replace('3', '៣')
    number = number.replace('4', '៤')
    number = number.replace('5', '៥')
    number = number.replace('6', '៦')
    number = number.replace('7', '៧')
    number = number.replace('8', '៨')
    number = number.replace('9', '៩')
    number = number.replace('0', '០')
    if number.find('.') == -1:
        return number
    else:
        first, second = number.split('.')
        return first + ' ក្បៀស ' + second


print(readAsKhmerText(10.1))