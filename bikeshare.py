import time
import pandas as pd
import numpy as np
import time
from tabulate import tabulate

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

Months = ['january', 'february', 'march', 'april', 'may', 'june']
Days =  ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city = ""
    filterBy ="none"
    month = "all"
    day = "all"
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = str(input("Would you like to see data for 'Chicago', 'New York City', or 'Washington'? \n"))
        city = city.strip() ; city = city.lower() 
        if (city == "chicago" or city == "new york city" or city == "washington"):
            break;
        print("wrong input!! please check your spelling.")
        continue;
    
    

    
    while True:
        filterBy = str(input("Would you like to filter the data by 'month', 'day', or 'none' at all? \n"))
        filterBy = filterBy.strip() ; filterBy = filterBy.lower()
        if (filterBy == "month" or filterBy == "day" or filterBy == "none"):
            break;
        print("wrong input!! please check your spelling.")
        continue;
        
    # TO DO: get user input for month (all, january, february, ... , june)
    while filterBy == "month":
        month = str(input("Which month - January, February, March, April, May, or June? \n"))
        month = month.strip() ; month = month.lower()
        if (month in Months):
            break;
        print("wrong input!! please check your spelling.")
        continue;
    
     
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while filterBy == "day":
        day = str(input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? \n"))
        day = day.strip() ; day = day.lower()
        if (day in Days):
            break;
        print("wrong input!! please check your spelling.")
        continue;

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        month = Months.index(month) + 1
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df.month.value_counts().idxmax()
    print('Most common month: \n', common_month)

    # TO DO: display the most common day of week
    common_day = df.day_of_week.value_counts().idxmax()
    print('Most common day: \n', common_day)

    # TO DO: display the most common start hour
    common_hour = df.hour.value_counts().idxmax()
    print('Most common hour: \n', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print('Most commonly used start station: \n', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print('Most commonly used start station: \n', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start End Station'] = list(zip(df['Start Station'], df['End Station']))
    common_start_end_station = df['Start End Station'].value_counts().idxmax()
    df.drop('Start End Station', inplace=True, axis=1)
    print('Most commonly  combination of start and end station trip: \n', common_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time = time.strftime('%H:%M:%S', time.gmtime(total_travel_time))
    print('Total travel time: \n', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_time = time.strftime('%H:%M:%S', time.gmtime(mean_travel_time))
    print('Mean travel time: \n', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types:")
    print(user_types)

    if 'Gender' in df:
    # TO DO: Display counts of gender
        df["Gender"].fillna("Not Specified", inplace = True)
        gender_count = df['Gender'].value_counts()
        print("\nCounts of gender: ")
        print(gender_count)
        
    if 'Birth Year' in df:
    # TO DO: Display earliest, most recent, and most common year of birth
        min_year = df['Birth Year'].min()
        print('\nEarliest year of birth: \n', int(min_year))
        
        max_year = df['Birth Year'].max()
        print('Earliest year of birth: \n', int(max_year))
        
        common_year = df['Birth Year'].value_counts().idxmax()
        print('Earliest year of birth: \n', int(common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def view_data(df):
    i=0
    while True:
        display_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
        if display_data.lower() != 'yes':
            break
        print(tabulate(df.iloc[np.arange(0+i,5+i)], headers ="keys"))
        i+=5

            



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        # TO DO: Display data sample 
        view_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
