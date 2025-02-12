import math

places = ['fowey', 'mevagissey', 'portscatho', 'falmouth', 'cadgewith', 'porthleven', 'penzance']
distances = [7, 11, 5.5, 13, 9, 9]

print("Welcome to the new and upcoming ferry \nserving costal ports in Cornwall \n")

run_checker = 0

abso_total = 0

places_rev = False


def time_def():
    global hour, time
    time_loop = True
    time_check_loop = True
    while time_loop == True:
        while time_check_loop == True:
            try:
                time = input("Enter time you want to book for? HH:MM\n")
                hour, minu = [int(i) for i in time.split(":")]
                if minu > 59:
                    print('incorrect time')
                    time = input("Enter time in HH:MM\n")
                    hour, minu = [int(i) for i in time.split(":")]
                elif hour > 23:
                    print('incorrect time')
                    time = input("Enter time in HH:MM\n")
                    hour, minu = [int(i) for i in time.split(":")]
                else:
                    time_loop = False
                    time_check_loop = False
            except ValueError:
                print('incorrect value entered')

        if hour in range(14, 19):
            places_rev = places.reverse()
            
        time_loop = False
    print('You are traveling on', date, 'at', time)


def cost_calculation(anum, cnum, conum):
    global abso_total_calc, abso_total
    return_check = False

    cost_adult = 1
    cost_child = 0.5
    cost_concessions = 0.75

    cost_a = cost_adult * anum
    cost_c = cost_child * cnum
    cost_con = cost_concessions * conum
    total = cost_c + cost_con + cost_a

    user_start = places.index(location_start)
    user_end = places.index(location_end)
    counter = user_start
    distance_calc = 0

    user_return = input('would you like to return? ')
    user_return = user_return.lower()
    if user_return == 'yes' or user_return == 'yeah' or user_return == 'y':
        return_check = True

    if return_check == True:
        if user_start > user_end:
            print('no journey at this time')
        else:
            for i in range(user_start, user_end):
                distance_calc = distances[counter] + distance_calc
                counter += 1
            abso_total = distance_calc * total
            abso_total_calc = abso_total * 2

    else:
        for i in range(user_start, user_end):
            distance_calc = distances[counter] + distance_calc
            counter += 1
        abso_total_calc = distance_calc * total


    if abso_total > 0.01:
        abso_total_calc = math.ceil(abso_total * 100) / 100

    calc_abso = str(abso_total_calc)
    print('\nThe total for your journey is £' + calc_abso)

def location(location_start, location_end):
    location_loop = True
    while location_loop == True:
        if location_start not in places or location_end not in places:
            print('incorrect location check spelling')
            print('Where would you like to start: \n')
            location_start = input()
            location_start = location_start.lower()
            print('Where will you be leaving us: \n')
            location_end = input()
            location_end = location_end.lower()
        else:
            location_loop = False

def date_def():
    date_loop = True
    global date
    while date_loop == True:
        try:
            date = input('what date do you want to book for? DD/MM/YYYY  \n')
            day, month, year = [int(i) for i in date.split("/")]
            if (len(date) == 9
                    or len(date) == 10
                    or len(date) == 11
                    and len(str(day)) == 2
                    or len(str(day)) == 1
                    and day <= 31
                    and len(str(month)) == 2
                    or len(str(month)) == 1
                    and month <= 12
                    and len(str(year)) == 4)\
                    and year >= 2024 \
                    or year >= 24:
                date_loop = False
            else:
                print('Incorrect date entered')
        except ValueError:
            print('incorrect value entered')

try:
    #location
    print(places)
    print('Where would you like to start: \n')
    location_start = input()
    location_start = location_start.lower()
    print('Where will you be disembarking: \n')
    location_end = input()
    location_end = location_end.lower()

    location(location_start=location_start, location_end=location_end)

    people_loop = True
    # number of people
    print('How many adults will join us today: \n')
    adults_num = int(input())
    print('How many children will join us today: \n')
    children_num = int(input())
    print('How many concessions will join us today: \n')
    concessions_num = int(input())


    while people_loop and ValueError == False:
        if adults_num <= -1:
            print('incorrect number of adults')
            print('How many adults will join us today: \n')
            adults_num = int(input())
        elif children_num <= -1:
            print('incorrect number of children')
            print('How many children will join us today: \n')
            children_num = int(input())
        elif concessions_num <= -1:
            print('incorrect number of concession')
            print('How many concessions will join us today: \n')
            concessions_num = int(input())
        else:
            people_loop = False

    #date
    date_def()

    #time
    time_def()

    #calculation
    cost_calculation(anum=adults_num, cnum=children_num, conum=concessions_num)

    print('You are traveling on', date, 'at', time)
    print('You will be travelling from', location_start, 'to', location_end)

except:
    print('Error 404')
