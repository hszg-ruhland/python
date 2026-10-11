# Fibonacci Numbers recoursiv

def get_fibo(n):
  if ( n==0 ):
    return 0
  if ( n==1 ):
    return 1
  return get_fibo(n-2)+get_fibo(n-1)


print(f"Fibonacci Number n=10 is {get_fibo(10)}")
