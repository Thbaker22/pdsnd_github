import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
days = ['monday','tuesday','wednesday','thursday','friday','saterday','sunday']
#This function defines the filters available
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
        city = input('Which City Would you like to select chicago, new york city, or washington: ').lower()
        if city in CITY_DATA:
            break
        else:
            print('Incorect input please slecet a city as indicated')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Would you like to select a month from jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec, or all: ').lower()
        if month == 'all':
            break
        elif month in months:
            break
        else:
            print('Incorrect input please select a month as indicated')
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Would you like to select a day from monday, tuesday, wednesday, thursday, friday, saterday, sunday or all: ').lower()
        if day == 'all':
            break
        elif day in days:
            break
        else:
            print('Incorrect input please select a day as indicated')

    print('-'*40)
    return city, month, day

#This function loads in the data
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
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
        month = month.index(month) + 1
        
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('\nThe most common month is ', df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('\nThe most common day of the week is ', df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print('\nThe most common start hour is ', df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nThe most commonly used start station is ', df['Start Station'].mode()[0]) 

    # TO DO: display most commonly used end station
    print('\nThe most commonly used end station is ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('\nThe most frequent combination of stations is ', (df['Start Station'] + ' and ' + df['End Station']).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('\nThe total travel time is ', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('\nThe mean travel time is ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

        
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
        
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\n',user_types)
    
              
    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('\n',gender_count)

    except:
        print('\nNo gender data for selected city')
    
    # TO DO: Display earliest, most recent, and most common year of birth
    try:    
        print('\nThe earliest year of birth is ', df['Birth Year'].min())
        print('\nThe most recent year of birth is ', df['Birth Year'].max())
        print('\nThe most common year of birth is ', df['Birth Year'].mode()[0])
    except:
        print('\nNo birth data for selected city')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_data(df):
    view_count = 0
    while True:
        choice = input('Would you like to view 5 lines of raw data: ').lower()
        if choice == 'yes':
            print(df.iloc[view_count:view_count+5])
            view_count += 5
        elif choice == 'no':
            break
        else:
            print('please input yes or no')

    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
