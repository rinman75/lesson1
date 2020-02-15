 
def get_summ(one, two, delimiter = "&"):
    b = one + delimiter + two
    return b.upper()  
learn = "hello"
python = "yury"
get_summ(learn, python)
print(get_summ(learn, python))