sh=input('Enter Hours: ')
sr=input('Enter Rate: ')
xh=float(sh)
xr=float(sr)
if xh>40:
    print('Overtime')
    pay=(xh-40)*(xr*0.5)+(xh*xr)
    print('Pay: ',pay)
else:
    print('Regular')
    pay=xh*xr
    print('Pay: ',pay)
print('อำนาจอธิปไตยเป็นของคนไทย')
q=input('ใช่ไหม\n')
if q=='ใช่':
    print('Good Democracy')
elif q=='ไม่':
    print('And then?')
    w=input('No King ')
    if w=='0':
        print('Vive La Republique!')
else:
    print('You are extreme Royalist, NOT DEMOCRACY!')
print('ยี่สิบสี่มิถุนาความเป็นมาประวัติศาสตร์')

    
