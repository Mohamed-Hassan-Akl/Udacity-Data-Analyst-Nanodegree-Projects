import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("please Enter one of these cities to show the data\" chicago, new york, washington\": ").lower()
        if city not in CITY_DATA:
            print("please check you  city spelling name, it should be one of these \" chicago, new york, washington\"")
        else:
            break
    while True:
        # TO DO: get user input for month (all, january, february, ... , june)
        month = input("please Enter month name or all to show data for all months: ").lower()
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        if month not in months and month != "all":
            print(
                "Please check your month name, it should be one of these \" january, february, march, april, may, june\"")
        else:
            break
    while True:
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = input("please Enter day name or all to show data for all days: ").lower()
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        if day not in days and day != "all":
            print(
                "Please check your day name, it should be one of these \" sunday,monday,tuesday,wednesday,thursday,friday,saturday\"")
        else:
            break
    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    # convert the column start time into data time to have ability to extract useful output like month,day
    df['Start Time'] = pd.to_datetime(df["Start Time"])
    # extract the month column  from the main data frame
    df["month"] = df["Start Time"].dt.month
    # extract the day column from the main data frame
    df["day"] = df["Start Time"].dt.day_name()
    # first step to filter the data frame by  user input month
    if month != "all":
        # to convert the month form being world string object to be in numerical  integer
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # make the filtration method
        df = df[df["month"] == month]

    if day != "all":
        # make another filtration by  input user day
        df = df[df["day"] == day.title()]

    # print(df)
    return df


def show_five_element(df):
    # this function will ask the the user if he want to represent the five element in the data frame
    x = 0
    five_element = input("Do you want to show the first five element of data frame \'yes\', or \'no\'").lower()
    while True:
        if five_element == "yes":
            print(df[x:x + 5])
            five_element = input("Do you want to show anther five element  \'yes\', or \'no\' ?").lower()
            # increment x to show the new five row in the next iteration
            x+=5
            if five_element == "no":
                break
        else:
            break
    #return "pass"

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    com_month =df["month"].mode()[0]
    print("common month : {}".format(com_month))

    # TO DO: display the most common day of week
    com_day= df["day"].mode()[0]
    print("common day : {}".format(com_day))


    # there is not any data fram for hour so I have to creat it \
    df["hour"] = df["Start Time"].dt.hour
    # TO DO: display the most common start hour
    com_hour = df["hour"].mode()[0]
    print("common day : {}".format(com_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    com_st_station =df["Start Station"].mode()[0]
    print("common Start Station : {}".format(com_st_station))

    # TO DO: display most commonly used end station
    com_en_station = df["End Station"].mode()[0]
    print("common End Station : {}".format(com_en_station))

    # TO DO: display most frequent combination of start station and end station trip
    # I will first find the start station and end station dataframe after that I will looking for mode in
    df["Start_To_End_Station"] =df["Start Station"] + df["End Station"]
    com_st_to_en_stationdf=df["Start_To_End_Station"].mode()[0]
    print("common Start_To_End_Station : {}".format(com_st_to_en_stationdf))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df["Trip Duration"].sum()
    print("the total travel time is {}".format(total_travel_time))
    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("the  mean travel time is {}".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df["User Type"].value_counts()
    print ("The user Type are : {}".format(user_type))

    # TO DO: Display counts of gender
    #make a check as not all cities have a gender column in it's data farme'
    if "Gender" in df:
         gender=df["Gender"].value_counts()
         print("\nthe gender distribution is : {}".format(gender))

    # TO DO: Display earliest, most recent, and most common year of birth
    # make a check as not all cities have a birth year column in it's data farme'
    if "Birth Year" in df:

        earliest = df["Birth Year"].min()
        print("\nthe earliest year of birth is : {}".format(int(earliest)))

        most_recent = df["Birth Year"].max()
        print("\nthe recent  year of birth is : {}".format(int(most_recent)))

        most_common = df["Birth Year"].mode()[0]
        print("\nthe most common year of birth is : {}".format(int(most_common)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        print(city, month, day)
        df = load_data(city, month, day)
        print(df)
        show_five_element(df)
        print("DONE")

        time_stats(df)

        station_stats(df)

        trip_duration_stats(df)

        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
