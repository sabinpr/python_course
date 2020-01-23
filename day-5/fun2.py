def tittle_case(fname,mname , lname , age):
    fname = fname.title().strip()
    if mname != '':
        mname = mname.title().strip()
    lname = lname.title().strip()
    print('your name is : ',fname ,mname , lname)
    print('age is : ' ,age)

fname = input('enter first name :  ')
mname = input('enter middle name : ')
lname = input('enter last name :  ')
age = input('age : ')

tittle_case(fname,mname , lname ,age)