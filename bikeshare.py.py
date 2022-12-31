import time
import pandas as pd
import numpy as np
   # this code created by MYAR.
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA =['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
      city = input("\nWhich city would you like to filter by? New York City, Chicago or Washington?\n").lower()
      if city not in CITY_DATA:
        print("Oops,Try again.")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
      month=input("choose month you would  like to filter by? January, February, March, April, May, June or 'all' \n\n ").lower()
      if month not in MONTH_DATA:
        print("Oops, TRY AGAIN")
        continue
      else:
        break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day=input("WHICH DAY YOU WANT? : Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' if you want select all days.\n\n ").lower()
      if day not in DAY_DATA:
        print("Oops, TRY AGAIN")
        continue
      else:
        break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):


    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df=pd.read_csv(CITY_DATA[city])
     #convert the Start Time column to datetime
    df['Start Time']=pd.to_datetime(df['Start Time'])

    df['month']=df['Start Time'].dt.month
    df['day in week']=df['Start Time'].dt.weekday_name

    if month !='all':
        months=['january', 'february', 'march', 'april', 'may', 'june']
        month=months.index(month)+1
        df = df[df ['month']==month]

    if day !='all':
        df = df [df ['day in week']==day.title()]


    return df


def time_stats(df):


    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('The Most Common Month is: /n', popular_month)
    # TO DO: display the most common day of week
    popular_day = df['day in week'].mode()[0]
    print('The Most Common Day is: /n', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The Most Common Hour is: /n', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time=time.time()

    # TO DO: display most commonly used start station
    Start_Station = df ['Start Station'] . value_counts()
    print('The Most Common start station is: /n', Start_Station)

    # TO DO: display most commonly used end station
    End_Station = df['End Station'] . value_counts()
    print('The Most Common end station is: /n', End_Station)


    # TO DO: display most frequent combination of start station and end station trip
    CombinationStation = df.groupby(['Start Station', 'End Station']).count()
    print('Most Commonly use combination of start station & end station :', Start_Station, " & ", End_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    print('Total travel time:',(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('average travel time:',(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df['User Type'].value_counts()
    print('User Types:\n\n', user_types)
    # TO DO: Display counts of gender
    try:
      gender_types=df['Gender'].value_counts()
      print('Gender Types:\n\n', gender_types)
    except KeyError:
      print("\nGender Types:\n No data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest=int(df['Birth Year'].min())
        recent=int(df['Birth Year'].max())
        commonyear=int(df['Birth Year'].mode()[0])
        print("\n\n The earliest bearth year : {earliest}\n\n The most recent birth year : {recent}\n\n The most common             birth year : {commonyear}")
    except:
        print("Oops, no birth year here!!.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data(df):
    raw_data = 0
    while True:
        answer = input("Do you wanna see raw data? Yes or No").lower()
        if answer not in ['yes', 'no']:
            answer = input("Oops,You write wrong word. type Yes or No.").lower()
        elif answer.lower() == 'yes':
            raw_data += 5
            print(df.iloc[raw_data : raw_data + 5])
            again = input("Do you wanna see more? Yes or No").lower()
            if again.lower() == 'no':
                break
        elif answer.lower() == 'no':
            return
def EDIT():
    print("this code created by MYAR")
def UDACITY():
    print("myar love udacity")



def main():
    while True:

        city, month, day =get_filters()
        df=load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
