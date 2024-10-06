# Example 1

def Studentinfo(Name,Id,age,Class,subject,marks):
    print(f's_Name={Name}')
    print(f's_Id={Id}')
    print(f's_age={age}')
    print(f's_class={Class}')
    print(f's_subject={subject}')
    print(f's_marks={marks}')
    return'---studentinfo'

print('----')
print(f'student_1{('Hitesh',1,20,10,'English',50)}')
print('---')
print(f'student_2{('Swapnil',2,20,10,'maths',50)}')
print('----')

## Example 2

def productinfo(Name,brand,price,Expirydate,type):
    print(f'product_Name={Name}')
    print(f'product_Brand={brand}')
    print(f'product_price={price}')
    print(f'product_Expirydate={Expirydate}')
    print(f'product_type={type}')

    return{
        'product-name':Name,
        'product-Brand':brand,
        'product-price':price,
        'product-Expirydate':Expirydate,
        'product-type':type,
    }


print('---')
product1=productinfo('Salt','Tata',30,'02-03-2024','Regularuse')
print('---')
product2=productinfo('Bakingsod','Tata',40,'04-05-2024','Regularuse')
print('---')