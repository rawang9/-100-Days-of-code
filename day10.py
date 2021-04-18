=============================================================================
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year,month):
    '''take thea year and month to check thdays in it'''
    #a doc string to define the fun when it called
    result=is_leap(year)  
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if is_leap(year) and month==2:
        return 29
    return month_days[month-1]
            
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

=============================================================================
#calculator
from day10_logo import logo
print(logo)
def add(n,m):
    '''add twwo no'''
    return n+m
def sub(n,m):
    return n-m
def div(n,m):
    return n/m
def mul(n,m):
    return n*m
operation={'+':add,'-':sub,'/':div,'*':mul}
flag=True
decision=''
n=0
while flag is True:
    if n==0:
        n=int(input("enter the first operator:   "))
    o=input("+\n-\n/\n*\n select the operation ")
    m=int(input("enter the second operator "))
    function=operation[o]
    n=function(n,m)
    print(n)
    decision=input(f"if you like to contionus with {n} type yes or no to start new cal or exit to end it    ")
    if decision.lower()=='exit':
        flag=False
    elif decision=='no':
        n=0