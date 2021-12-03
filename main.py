####### FUNÇÃO 1 #######
def sum_numbers(*args):
    output = 0

    for number in args:
        output += number
    
    return output


####### FUNÇÃO 2 #######
def get_multiplied_amount(multiplier, *args):
    sum = 0

    for number in args:
        sum += number
    
    return sum * multiplier


####### FUNÇÃO 3 #######
def word_concatenator(*args):
    return " ".join(args)


####### FUNÇÃO 4 #######
def inverted_word_factory(*args):
    # output = []
    inverted_words = []

    for word in args:
        inverted_words.append(word[::-1])
    
    inverted_words.reverse()

    return ' '.join(inverted_words)



####### FUNÇÃO 5 #######
def dictionary_separator(**kwargs):
    keys = []
    values = []

    for key in kwargs:
        keys.append(key)
        values.append(kwargs[key])

    output = []
    output.append(keys)
    output.append(values)
    
    return tuple(output)


####### FUNÇÃO 6 #######
def dictionary_creator(*args, **kwargs):
    if len(args) < len(kwargs):
        return None
    
    dict_values = []
    
    output = {}

    for key, value in kwargs.items():
        dict_values.append(value)

    for i in range(len(dict_values)):
        output[args[i]] = dict_values[i]
    
    return output


####### FUNÇÃO 7 #######
def purchase_logger(**kwargs):
    price = str(kwargs['price'])
    quantity = str(kwargs['quantity'])

    output = 'Product ' + kwargs['name'] + ' costs ' + price + ' and was bought ' + quantity

    return output



####### FUNÇÃO 8 #######
def world_cup_logger(country, *args):
    years_in_order = list(args)
    years_in_order.sort()
    output = f'{country} - '

    # for year in years_in_order:
    #     output += str(year) + ', '

    for i in range(len(years_in_order)):
        if i == len(years_in_order) -1:
            output += 'e ' + str(years_in_order[i])
        elif i == len(years_in_order) -2:
            output += str(years_in_order[i]) + ' '
        else:
            output += str(years_in_order[i]) + ', '

    return output