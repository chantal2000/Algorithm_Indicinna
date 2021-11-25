ones = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine')
twos = ('Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen')
tens = ('Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred')
tens_power = ('', 'Thousand', 'Million', 'Billion')

def process(number, index):
    if number=='0':
        return 'Zero' 
    l = len(number)
    if(l> 3):
        return False
    
    number = number.zfill(3)
    words = ''
    tdigit = int(number[1])
    hdigit = int(number[0])
    odigit = int(number[2])
    words += '' if number[0] == '0' else ones[hdigit]
    words += ' Hundred ' if not words == '' else ''
    if(tdigit > 1):
        words += tens[tdigit - 2]
        words += ' '
        words += ones[odigit]
    
    elif(tdigit == 1):
        words += twos[(int(tdigit + odigit) % 10) - 1]
        
    elif(tdigit == 0):
        words += ones[odigit]

    if(words.endswith('Zero')):
        words = words[:-len('Zero')]
    else:
        words += ' '
     
    if(not len(words) == 0):    
        words +=  tens_power[index]
    return words   
def num_to_string(number):
    length = len(str(number))  
    count = length // 3 if length % 3 == 0 else length // 3 + 1
    copy = count
    result = []

    for i in range(length - 1, -1, -3):
          result.append(process(str(number)[0 if i - 2 < 0 else i - 2 : i + 1], copy - count))
          count -= 1;
    final_result = ''
    for s in reversed(result):
        temp = s + ' '
        final_result += temp
    
    return final_result
number = int(input('Enter a number: '))
print('%d in words is: %s' %(number,num_to_string(number)))