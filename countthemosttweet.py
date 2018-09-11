twitter_dict = {}
count= {}
def check(times):
    n = int(input("enter the total number of twitter"))
    for i in range(n):
        key = input("enter the key: ")
        value = input("enter the value:")
        twitter_dict[key] = value
        if key in count:
            count[key] = count[key] + 1
        else:
            count[key] =  1
    times = times - 1
    if times > 0:
        return times
    else:
        for key, value in sorted(count.items()):
            if value > 2:
                print(key,value)
            elif value == 2:
                print(key,value)

def main():
    try:
        times = int(input("how many times want to create"))
        #print(times)
        while times is not None:
            times = check(times)
            #print(times)
            #break
    except ValueError:
        print("invalid")
if __name__ == '__main__':
    main()
