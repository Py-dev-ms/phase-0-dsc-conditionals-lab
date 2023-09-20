def less_than_50():
    number_50 = 50
    my_number = None
    if number_50 > 100:
        # if number_50 is greater than 100, assign the `my_number` variable to the number 100
        my_number = 100
    elif number_50 > 50:
        # if number_50 is greater than 50, assign the `my_number` variable to the number 50
        my_number = 50
    else:
        # else assign the `my_number` variable to 0
        my_number = 0

temperature = 85
is_it_hot = None
# conditionals go here
if temperature > 80:
    is_it_hot = "It is so hot out!"
else:
    is_it_hot = "This is nothing! Bring on the heat."

today_is = 4
day_of_the_week = None
if today_is == 1:
    day_of_the_week = 'Sunday'
elif today_is == 2:
    day_of_the_week = 'Monday'
elif today_is == 3:
    day_of_the_week = 'Tuesday'
elif today_is == 4:
    day_of_the_week = 'Wednesday'
elif today_is == 5:
    day_of_the_week = 'Thursday'
elif today_is == 6:
    day_of_the_week = 'Friday'
else:
    day_of_the_week = 'Saturday'

string = "School"
sub_string = "cool"
ends_with = None
if string.endswith(sub_string):
    ends_with = True
else:
    ends_with = False

print(ends_with)