# n = int(input("Enter any number: "))
# sum1 = 0
# for i in range(1, n):
#     if(n % i == 0):
#         sum1 = sum1 + i
# if (sum1 == n):
#     print("The number is a Perfect number!")
# else:
#     print("The number is not a Perfect number!")
# ====================================================
# def isPerfect( num ): 
#     sum = 1
#     i = 2
#     while i*i<= num: 
#         if num % i == 0: 
#             sum = sum + i + num/i 
#         i += 1
#     return (True if sum == num and num!=1 else False) 
# for number in range (1000): 
#     if isPerfect (number): 
#         print(number ) 
#     else:
#     	print(n,"it is not a perfect number")
# print(isPerfect(1))
# ================================================== 
# def isperfect(number):
# 	sum=1
# 	i=2
# 	while i*i<=number:
# 		if number%i==0:
# 			sum=sum+i+number/i
# 		i=i+1
# 	return (True if sum==num else False)
# for num in range(1000):
# 	if isperfect (num):
# 		print(num)
# print(isperfect(0))
# =============================================