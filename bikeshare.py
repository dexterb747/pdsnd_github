import time
import pandas as pd
import numpy as np

# define global objects. These global objects can be used by other local functions.
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

months = ['january', 'february', 'march', 'april', 'may', 'june']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs. These are 3 big cities to test with.
    city = ''
    while city not in CITY_DATA:
        city = input('Please enter chicago, new york city, washington\n')
        if city.lower() in CITY_DATA:
            break
        else:
            print ('Invalid city entered\n')

    # get user input for month (all, january, february, ... , june). These are just 6 months.
    month = ''
    while month.lower() not in months or month.lower() != 'all':
        month = input('Please enter a month from january to june OR all for the 6 months\n')
        if month.lower() in months or month.lower() == 'all':
            break
        else:
            print ('Invalid month entered\n')

    # get user input for day of week (all, monday, tuesday, ... sunday). These are just 7 days.
    day = ''
    while day.lower() not in days or day.lower() != 'all':
        day = input('Please enter a day from monday to sunday OR all for the 7 days\n')
        if day.lower() in days or day.lower() == 'all':
            break
        else:
            print ('Invalid day entered\n')

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
    df = pd.read_csv(CITY_DATA[city.lower()])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month from the Start Time column to create a month column
    df['Month'] = df['Start Time'].dt.month
    
    # extract week day from the Start Time column to create a week day column
    df['Day of Week'] = df['Start Time'].dt.weekday
    
    # extract hour from the Start Time column to create an hour column
    df['Hour'] = df['Start Time'].dt.hour

    # filter by month if a specific month is entered
    if month.lower() != 'all':
    # use the index of the months list as the relevant month number        
        month = months.index(month.lower()) + 1
        # filter by month
        df = df[df['Month'] == month]

    # filter by day of week if a specific day is entered
    if day.lower() != 'all':
    # use the index of the days list as the relevant day number        
        day = days.index(day.lower())
        # filter by day
        df = df[df['Day of Week'] == day]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    common_month = df['Month'].mode()[0]
    print ('The most common month is ', months[common_month-1])

    # display the most common day of week
    common_day = df['Day of Week'].mode()[0]
    print ('The most common day of week is ', days[common_day])

    # display the most common start hour
    common_hour = df['Hour'].mode()[0]
    print ('The most common start hour is ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print ('The most common Start Station is ', common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print ('The most common End Station is ', common_end_station)

    # display most frequent combination of start station and end station trip
    df['Start to End Station'] = df['Start Station'] + ' to ' + df['End Station']
    common_start_end_station = df['Start to End Station'].mode()[0]
    print ('The most common Start Station and End Station combination is ', common_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print ('The Total Travel Time is ', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print ('The Mean Travel Time is ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print ('The counts of user type are\n', user_types)

    if 'Gender' not in df.columns:
        # Add the missing column to ensure processing continues
        df['Gender'] = ''

    if 'Birth Year' not in df.columns:
        # Add the missing column to ensure processing continues
        df['Birth Year'] = ''

    # Display counts of gender
    gender = df['Gender'].value_counts()
    print ('The counts of gender are\n', gender)

    # Display earliest, most recent, and most common year of birth

    earliest_birth_year = df['Birth Year'].min()
    print ('The most common Birth Year is ', earliest_birth_year)

    recent_birth_year = df['Birth Year'].max()
    print ('The most common Birth Year is ', earliest_birth_year)
    
    common_birth_year = df['Birth Year'].mode()[0]
    print ('The most common Birth Year is ', common_birth_year)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """Displays raw bikeshare data."""

    print('\nReady to print raw data...\n')
    start_time = time.time()
    
    see_raw_data = ''
    row_counter = 0
    column_counter = 5
    while see_raw_data.lower() not in ('yes','no'):
        see_raw_data = 'yes'
        while see_raw_data.lower() == 'yes':                    
            see_raw_data = input('Do you want to see 5 lines of raw data? Enter yes or no\n')
            if see_raw_data.lower() == 'yes':
                print (df.iloc[row_counter:column_counter])
                row_counter = row_counter + 5
                column_counter = column_counter + 5
            elif see_raw_data.lower() == 'no':
                break
            else:
                print ('Invalid answer entered\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
