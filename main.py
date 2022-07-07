def is_even(arr):
    if((arr[0]%2+arr[1]%2==0) or ((arr[0]%2+arr[1]%2==1) and arr[2]%2==0)):
        return True
    else:
        return False
def find_number(arr):
    even = is_even(arr)
    for num in arr:
        if ((even and num%2==1) or (not even and num%2==0)):
            print(num)
            break
if __name__ == "__main__":
    find_number([])
