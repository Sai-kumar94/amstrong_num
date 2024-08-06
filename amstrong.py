n=int(input('enter a number'))
dummy=n
l=len(str(n))
sum=0
while dummy!=0:
    rem=dummy%10
    sum+=rem**l
    dummy//=10
if n==sum:
    print(f'{n} is a amstrong number')
else:
    print(f'{n} is not a amstrong number')

#  here we are taking dummy value because we are performing floor division
# floor division will reduce the value to zero
#  The while loop iterates like first, it checks if the number is not equal to zero or not
# if it is not equal to zero then enter into the loop and find the reminder of number ex: 153%10 gives reminder 3.
# In the next step add the cube of a number to the sum1(3*3*3).
# Then the step gives the quotient of the number (153//10=15).
# this loop will continue till the given number is equal to zero.