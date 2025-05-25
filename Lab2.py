import statistics as stats

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")

def get_user_input():
    numberlist=input("Enter numbers: ")
    numberlist=numberlist.split(",")
    numlist=list(map(float,numberlist))
    return numlist

def calc_average_temperature(numlist):
    average=sum(numlist)/len(numlist)
    return average

def calc_min_max_temperature(numlist):
    min_max=[]
    minimum=min(numlist)
    maximum=max(numlist)
    min_max=[minimum,maximum]
    return min_max

def calc_median_temperature(numlist):
    median=stats.median(numlist)
    return median



def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    average=calc_average_temperature(num_list)
    print("average temp = " +str(average))
    min_max=calc_min_max_temperature(num_list)
    print("min,max = " + str(min_max))
    median=calc_median_temperature(num_list)
    print("median = " + str(median))

if __name__ == "__main__":
    main()
