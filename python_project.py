# List/Arrays/Possible values for input

import pandas as pd
possible_city=("new york city","chicago","washington")
possible_filter=("month","day","both","none")
possible_month=("january","february","march","april","may","june","july","august","september","october","november","december")
possible_day=("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
possible_files={"new york city":"new_york_city.csv","chicago":"chicago.csv","washington":"washington.csv"}
line_count=1

def city_selection():
	city_input = input("Which city would you like to explore? New York City, Chicago or Washington?\n")
	print ("You have selected: "+city_input+"\n")
	if city_input.lower() not in possible_city:
		print("Double check your input")
		city_selection()
	else: return city_input.lower()

def filter_selection():
	filter_input=input("Would you like to filter the data by month, day, both or none?\n")
	print ("You have selected: "+filter_input+"\n")
	if filter_input.lower() not in possible_filter:
		print("Double check your input")
		filter_selection()
	else: return filter_input.lower()

def month_selection():
	month_input=input("Which month would you like to explore? Please input name of the month e.g. January.\n")
	print("You have selected: "+month_input+"\n")
	if  month_input.lower() not in possible_month:
		print("Double check your input")
		month_selection()
	else: return month_input.lower()

def day_selection():
	day_input=input("Which day would you like to explore? Please input name of the day e.g. Monday.\n")
	print("You have selected: "+day_input+"\n")
	if  day_input.lower() not in possible_day:
		print("Double check your input")
		day_selection()
	else: return day_input.lower()

#Function returns the common day of the week by month
def get_most_common_day_of_the_week_by_month(month):
	city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
	city_data['day_of_the_week'] = city_data['Start Time'].dt.weekday_name
	city_data['month'] = city_data['Start Time'].dt.month
	month_int= possible_month.index(month)+1
	possible_months_in_csv=city_data['month'].unique().tolist()
	if month_int in possible_months_in_csv:
		city_data_filtered_by_month = city_data[city_data.month == month_int]
		most_common_day_of_the_week_by_month=city_data['day_of_the_week'].mode()[0]
	else: most_common_day_of_the_week_by_month="No data for this month available."
	return str(most_common_day_of_the_week_by_month)

#Function returns the most common hour by month
def get_most_common_hour_by_month(month):
	city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
	city_data['hour'] = city_data['Start Time'].dt.hour
	city_data['month'] = city_data['Start Time'].dt.month
	#Parameter month is in format string e.g. January and has to be converted into an integer. 
	#The +1 is due to zero indexing. 
	month_int= possible_month.index(month)+1
	possible_months_in_csv=city_data['month'].unique().tolist()
	#Not all months are present in data set. Thus, check if month is csv file. 
	if month_int in possible_months_in_csv:
		city_data_filtered_by_month = city_data[city_data.month == month_int]
		most_common_hour_by_month=city_data_filtered_by_month['hour'].mode()[0]
	else: most_common_hour_by_month="No data for this month available."
	return str(most_common_hour_by_month)

#Function returns most popular stations by month
def get_most_common_station(month,start_end):
	city_data[start_end+' Time'] = pd.to_datetime(city_data[start_end+' Time'])
	city_data['month'] = city_data[start_end+' Time'].dt.month
	possible_months_in_csv=city_data['month'].unique().tolist()
	if (possible_month.index(month)+1) in possible_months_in_csv:
		city_data_filtered_by_month=city_data[city_data.month == (possible_month.index(month)+1)]
		most_common_station= city_data_filtered_by_month[start_end+" Station"].mode()[0]	
	else: most_common_station="No data for this month available."
	return most_common_station

#Function returns total trip duration by month
def get_total_travel_time_by_month(month):
	city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
	city_data['month'] = city_data['Start Time'].dt.month
	#Parameter month is in format string e.g. January and has to be converted into an integer. 
	#The +1 is due to zero indexing. 
	month_int= possible_month.index(month)+1
	possible_months_in_csv=city_data['month'].unique().tolist()
	#Not all months are present in data set. Thus, check if month is csv file. 
	if month_int in possible_months_in_csv:
		city_data_filtered_by_month = city_data[city_data.month == month_int]
		total_travel_in_seconds_by_month=city_data_filtered_by_month['Trip Duration'].sum()
		total_travel_in_days_by_month=total_travel_in_seconds_by_month//(24*3600)
	else: total_travel_in_days_by_month="No data for this month available."
	return str(total_travel_in_days_by_month)

#Function returns average trip duration by month
def get_average_travel_time_by_month(month):
	city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
	city_data['month'] = city_data['Start Time'].dt.month
	#Parameter month is in format string e.g. January and has to be converted into an integer. 
	#The +1 is due to zero indexing. 
	month_int= possible_month.index(month)+1
	possible_months_in_csv=city_data['month'].unique().tolist()
	#Not all months are present in data set. Thus, check if month is csv file. 
	if month_int in possible_months_in_csv:
		city_data_filtered_by_month = city_data[city_data.month == month_int]
		average_travel_in_seconds=city_data['Trip Duration'].mean()
		average_travel_in_minutes_by_month=average_travel_in_seconds//60
	else: average_travel_in_minutes_by_month="No data for this month available."
	return str(average_travel_in_minutes_by_month)

#Fucntion returns user gender type count by month 
def get_user_gender_by_month(month):
	if u_city == "washington":
		user_gender_by_month="There is no data available." 
	else: 
		city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
		city_data['month'] = city_data['Start Time'].dt.month
		#Parameter month is in format string e.g. January and has to be converted into an integer. 
		#The +1 is due to zero indexing. 
		month_int= possible_month.index(month)+1
		possible_months_in_csv=city_data['month'].unique().tolist()
		#Not all months are present in data set. Thus, check if month is csv file. 
		if month_int in possible_months_in_csv:
			city_data_filtered_by_month = city_data[city_data.month == month_int]
			user_gender_by_month= city_data_filtered_by_month['Gender'].value_counts()	
		else:
			user_gender_by_month="There is no data available." 
	return str(user_gender_by_month) 

#Function returns oldest user, youngest user and most common birth year
def years_of_birth_by_month(month):
	if u_city == "washington":
		result="There is no data available." 
	else: 
		city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
		city_data['month'] = city_data['Start Time'].dt.month
		#Parameter month is in format string e.g. January and has to be converted into an integer. 
		#The +1 is due to zero indexing. 
		month_int= possible_month.index(month)+1
		possible_months_in_csv=city_data['month'].unique().tolist()
		#Not all months are present in data set. Thus, check if month is csv file. 
		if month_int in possible_months_in_csv:
			city_data_filtered_by_month = city_data[city_data.month == month_int]
			oldest_user_birth_year_by_month=city_data_filtered_by_month['Birth Year'].min()
			youngest_user_birth_year_by_month=city_data_filtered_by_month['Birth Year'].max()
			most_comon_year_of_birth_by_month=city_data_filtered_by_month['Birth Year'].mode()[0]
			result = "Oldest user: "+str(int(oldest_user_birth_year_by_month))+"\n"+"Youngest user: "+str(int(youngest_user_birth_year_by_month))+"\n"+"Most common year of birth: "+str(int(most_comon_year_of_birth_by_month))
		else:
			result = "There is no data available."
	return result 

#Fucntion returns user type count by month
def get_user_type_count_by_month(month):
	city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
	city_data['month'] = city_data['Start Time'].dt.month
	#Parameter month is in format string e.g. January and has to be converted into an integer. 
	#The +1 is due to zero indexing. 
	month_int= possible_month.index(month)+1
	possible_months_in_csv=city_data['month'].unique().tolist()
	#Not all months are present in data set. Thus, check if month is csv file. 
	if month_int in possible_months_in_csv:
		city_data_filtered_by_month = city_data[city_data.month == month_int]
		user_type_count_by_month = city_data_filtered_by_month['User Type'].value_counts()
	else: user_type_count_by_month="No data for this month available."
	return str(user_type_count_by_month)

#Function returns most popular start or end station by day.
def get_most_common_station_by_day(day,start_end):
	city_data[start_end+' Time'] = pd.to_datetime(city_data[start_end+' Time'])
	city_data['day'] = city_data[start_end+' Time'].dt.weekday_name
	city_data_filtered_by_day=city_data[city_data.day.str.lower() == day]
	return city_data_filtered_by_day[start_end+" Station"].mode()[0]	

def get_total_travel_time_by_day(day):
	city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
	city_data['day'] = city_data['Start Time'].dt.weekday_name
	city_data_filtered_by_day = city_data[city_data.day.str.lower() == day]
	total_travel_in_seconds_by_day=city_data_filtered_by_day['Trip Duration'].sum()
	total_travel_in_days_by_day=total_travel_in_seconds_by_day//(24*3600)
	return str(total_travel_in_days_by_day)

def get_average_travel_time_by_day(day):
	city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
	city_data['day'] = city_data['Start Time'].dt.weekday_name
	city_data_filtered_by_day = city_data[city_data.day.str.lower() == day]
	average_travel_in_seconds=city_data['Trip Duration'].mean()
	average_travel_in_minutes_by_day=average_travel_in_seconds//60
	return str(int(average_travel_in_minutes_by_day))

#Fucntion returns most common hour by day
def get_most_common_hour_by_day(day):
	city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
	city_data['hour'] = city_data['Start Time'].dt.hour
	city_data['day'] = city_data['Start Time'].dt.weekday_name
	city_data_filtered_by_day = city_data[city_data.day.str.lower() == day]
	most_common_hour=city_data_filtered_by_day['hour'].mode()[0]
	return str(most_common_hour)

#Fucntion returns user type count by day
def get_user_type_count_by_day(day):
	city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
	city_data['day'] = city_data['Start Time'].dt.weekday_name
	city_data_filtered_by_day = city_data[city_data.day.str.lower() == day]
	user_type_count_by_day = city_data_filtered_by_day['User Type'].value_counts()
	return str(user_type_count_by_day)

def years_of_birth_by_day(day):
	if u_city == "washington":
		result = "There is no data available." 
	else:
		city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
		city_data['hour'] = city_data['Start Time'].dt.hour
		city_data['day'] = city_data['Start Time'].dt.weekday_name
		city_data_filtered_by_day = city_data[city_data.day.str.lower() == day]
		oldest_user_birth_year_by_day=city_data_filtered_by_day['Birth Year'].min()
		youngest_user_birth_year_by_day=city_data_filtered_by_day['Birth Year'].max()
		most_comon_year_of_birth_by_day=city_data_filtered_by_day['Birth Year'].mode()[0]
		result = "Oldest user: "+str(int(oldest_user_birth_year_by_day))+"\n"+"Youngest user: "+str(int(youngest_user_birth_year_by_day))+"\n"+"Most common year of birth: "+str(int(most_comon_year_of_birth_by_day))
	return result 

#Fucntion returns user gender type count by day 
def get_user_gender_by_day(day):
	if u_city == "washington":
		user_gender_by_day="There is no data available." 
	else:
		city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
		city_data['hour'] = city_data['Start Time'].dt.hour
		city_data['day'] = city_data['Start Time'].dt.weekday_name
		city_data_filtered_by_day = city_data[city_data.day.str.lower() == day]
		user_gender_by_day = city_data_filtered_by_day['Gender'].value_counts()	
	return str(user_gender_by_day) 

#Function returns the most common hour by day
def get_most_common_hour_by_day(day):
	city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
	city_data['hour'] = city_data['Start Time'].dt.hour
	city_data['day'] = city_data['Start Time'].dt.weekday_name
	city_data_filtered_by_day = city_data[city_data.day.str.lower()== day]
	most_common_hour=city_data_filtered_by_day['hour'].mode()[0]
	return str(most_common_hour)

#Function returns most common hour by day and month.
def get_most_common_hour_by_day_and_month(day,month):
	city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
	#New columns hour, day and month are added.
	city_data['hour'] = city_data['Start Time'].dt.hour
	city_data['day'] = city_data['Start Time'].dt.weekday_name
	city_data['month'] = city_data['Start Time'].dt.month
	#Parameter month is in format string e.g. January and has to be converted into an integer. 
	#The +1 is due to zero indexing. 
	month_int= possible_month.index(month)+1
	possible_months_in_csv=city_data['month'].unique().tolist()
	#Not all months are present in data set. Thus, check if month is csv file. 
	if month_int in possible_months_in_csv:
		city_data_filtered_by_day = city_data[city_data.day.str.lower() == day]
		city_data_filtered_by_day_and_month = city_data_filtered_by_day[city_data_filtered_by_day.month == month_int]
		most_common_hour=city_data_filtered_by_day_and_month['hour'].mode()[0]
	else: most_common_hour="No data for this month available."
	return str(most_common_hour)

#Function return most popular start or end station by day and month.
def get_most_common_station_by_day_and_month(day,month,start_end):
	city_data[start_end+' Time'] = pd.to_datetime(city_data[start_end+' Time'])
	city_data['month'] = city_data[start_end+' Time'].dt.month
	city_data['day'] = city_data['Start Time'].dt.weekday_name
	#Parameter month is in format string e.g. January and has to be converted into an integer. 
	#The +1 is due to zero indexing. 
	month_int= possible_month.index(month)+1
	possible_months_in_csv=city_data['month'].unique().tolist()
	if (possible_month.index(month)+1) in possible_months_in_csv:
		city_data_filtered_by_day = city_data[city_data.day.str.lower() == day]
		city_data_filtered_by_day_and_month = city_data_filtered_by_day[city_data_filtered_by_day.month == month_int]
		most_common_station_by_day_and_month=city_data_filtered_by_day_and_month[start_end+" Station"].mode()[0]
	else: most_common_station_by_day_and_month="No data for this month available."
	return most_common_station_by_day_and_month

#Function returns user type count by day and month
def get_user_type_count_by_day_and_month(day,month):
	city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
	city_data['month'] = city_data['Start Time'].dt.month
	city_data['day'] = city_data['Start Time'].dt.weekday_name
	#Parameter month is in format string e.g. January and has to be converted into an integer. 
	#The +1 is due to zero indexing. 
	month_int= possible_month.index(month)+1
	possible_months_in_csv=city_data['month'].unique().tolist()
	#Not all months are present in data set. Thus, check if month is csv file. 
	if month_int in possible_months_in_csv:
		city_data_filtered_by_day = city_data[city_data.day.str.lower() == day]
		city_data_filtered_by_day_and_month = city_data_filtered_by_day[city_data_filtered_by_day.month == month_int]
		user_type_count_by_day_and_month = city_data_filtered_by_day_and_month['User Type'].value_counts()
	else: user_type_count_by_day_and_month="No data for this month available."
	return str(user_type_count_by_day_and_month)

#Function returns user gender type count by day and month 
def get_user_gender_by_day_and_month(day,month):
	if u_city == "washington":
		user_gender_by_day_and_month="There is no data available." 
	else:
		city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
		city_data['month'] = city_data['Start Time'].dt.month
		city_data['day'] = city_data['Start Time'].dt.weekday_name
		#Parameter month is in format string e.g. January and has to be converted into an integer. 
		#The +1 is due to zero indexing. 
		month_int= possible_month.index(month)+1
		possible_months_in_csv=city_data['month'].unique().tolist()
		#Not all months are present in data set. Thus, check if month is csv file. 
		if month_int in possible_months_in_csv:
			city_data_filtered_by_day = city_data[city_data.day.str.lower() == day]
			city_data_filtered_by_day_and_month = city_data_filtered_by_day[city_data_filtered_by_day.month == month_int]
			user_gender_by_day_and_month = city_data_filtered_by_day_and_month['Gender'].value_counts()
		else:
			user_gender_by_day_and_month="There is no data available." 		
	return str(user_gender_by_day_and_month) 

#Function returns oldest user, youngest user and most common birth year
def years_of_birth_by_day_and_month(day,month):
	if u_city == "washington":
		result = "There is no data available." 
	else:
		city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
		city_data['month'] = city_data['Start Time'].dt.month
		city_data['day'] = city_data['Start Time'].dt.weekday_name
		#Parameter month is in format string e.g. January and has to be converted into an integer. 
		#The +1 is due to zero indexing. 
		month_int= possible_month.index(month)+1
		possible_months_in_csv=city_data['month'].unique().tolist()
		#Not all months are present in data set. Thus, check if month is csv file. 
		if month_int in possible_months_in_csv:
			city_data_filtered_by_day = city_data[city_data.day.str.lower() == day]		
			city_data_filtered_by_day_and_month = city_data_filtered_by_day[city_data_filtered_by_day.month == month_int]
			oldest_user_birth_year_by_day_and_month=city_data_filtered_by_day_and_month['Birth Year'].min()
			youngest_user_birth_year_by_day_and_month=city_data_filtered_by_day_and_month['Birth Year'].max()
			most_comon_year_of_birth_by_day_and_month=city_data_filtered_by_day_and_month['Birth Year'].mode()[0]
			result = "Oldest user: "+str(int(oldest_user_birth_year_by_day_and_month))+"\n"+"Youngest user: "+str(int(youngest_user_birth_year_by_day_and_month))+"\n"+"Most common year of birth: "+str(int(most_comon_year_of_birth_by_day_and_month))
		else: result = "There is no data available."
	return result 

#Function returns total trip duration by day and month
def get_total_travel_time_by_day_and_month(day,month):
	city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
	city_data['month'] = city_data['Start Time'].dt.month
	city_data['day'] = city_data['Start Time'].dt.weekday_name
	#Parameter month is in format string e.g. January and has to be converted into an integer. 
	#The +1 is due to zero indexing. 
	month_int= possible_month.index(month)+1
	possible_months_in_csv=city_data['month'].unique().tolist()
	if (possible_month.index(month)+1) in possible_months_in_csv:
		city_data_filtered_by_day = city_data[city_data.day.str.lower() == day]
		city_data_filtered_by_day_and_month = city_data_filtered_by_day[city_data_filtered_by_day.month == month_int]
		total_travel_in_seconds_by_day_and_month=city_data_filtered_by_day_and_month['Trip Duration'].sum()
		total_travel_in_days_by_day_and_month=total_travel_in_seconds_by_day_and_month//(24*3600)
	else: total_travel_in_days_by_day_and_month = "There is no data available."
	return str((total_travel_in_days_by_day_and_month))

#Function returns average trip duration by day and month
def get_average_travel_time_by_day_and_month(day,month):
	city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
	city_data['month'] = city_data['Start Time'].dt.month
	city_data['day'] = city_data['Start Time'].dt.weekday_name
	#Parameter month is in format string e.g. January and has to be converted into an integer. 
	#The +1 is due to zero indexing. 
	month_int= possible_month.index(month)+1
	possible_months_in_csv=city_data['month'].unique().tolist()
	if (possible_month.index(month)+1) in possible_months_in_csv:
		city_data_filtered_by_day = city_data[city_data.day.str.lower() == day]
		city_data_filtered_by_day_and_month = city_data_filtered_by_day[city_data_filtered_by_day.month == month_int]
		average_travel_in_seconds=city_data['Trip Duration'].mean()
		average_travel_in_minutes_by_day_and_month=average_travel_in_seconds//60
	else: average_travel_in_minutes_by_day_and_month= "There is no data available."
	return str((average_travel_in_minutes_by_day_and_month))

#Function return most popular start or end station by day and month.
def get_most_common_station_by_day_and_month(day,month,start_end):
	city_data[start_end+' Time'] = pd.to_datetime(city_data[start_end+' Time'])
	city_data['month'] = city_data[start_end+' Time'].dt.month
	city_data['day'] = city_data['Start Time'].dt.weekday_name
	#Parameter month is in format string e.g. January and has to be converted into an integer. 
	#The +1 is due to zero indexing. 
	month_int= possible_month.index(month)+1
	possible_months_in_csv=city_data['month'].unique().tolist()
	if (possible_month.index(month)+1) in possible_months_in_csv:
		city_data_filtered_by_day = city_data[city_data.day.str.lower() == day]
		city_data_filtered_by_day_and_month = city_data_filtered_by_day[city_data_filtered_by_day.month == month_int]
		most_common_station_by_day_and_month=city_data_filtered_by_day_and_month[start_end+" Station"].mode()[0]
	else: most_common_station_by_day_and_month="No data for this month available."
	return most_common_station_by_day_and_month

#Function returns the most common start month
def get_most_common_start_month():
	city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
	city_data['month'] = city_data['Start Time'].dt.month
	most_common_start_month=city_data['month'].mode()[0]
	return possible_month[most_common_start_month -1]

#Function returns the most day of the week
def get_most_common_day_of_the_week():
	city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
	city_data['day_of_the_week'] = city_data['Start Time'].dt.weekday_name
	most_common_day_of_the_week=city_data['day_of_the_week'].mode()[0]
	return most_common_day_of_the_week

#Function returns the most common hour
def get_most_common_hour():
	city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
	city_data['hour'] = city_data['Start Time'].dt.hour
	most_common_hour=city_data['hour'].mode()[0]
	return str(most_common_hour)

#Function returns total trip duration 
def get_total_travel_time():
	total_travel_in_seconds=city_data['Trip Duration'].sum()
	total_travel_in_days=total_travel_in_seconds//(24*3600)
	return str(total_travel_in_days)

#Function returns average trip duration 
def get_average_travel_time():
	average_travel_in_seconds=city_data['Trip Duration'].mean()
	average_travel_in_minutes=average_travel_in_seconds//60
	return str(average_travel_in_minutes)

#Function returns most popular start or end station.
def get_most_common_station_none(start_end):
	return city_data[start_end+" Station"].mode()[0]	

#Function returns frequent start and end combination
def get_most_frequent_start_end_combination():
	city_data["Start End Combination"] = city_data['Start Station']+" & "+city_data['End Station']
	return city_data["Start End Combination"].mode()[0]

#Fucntion returns user type count
def get_user_type_count():
	user_type = city_data['User Type'].value_counts()
	return str(user_type)

#Fucntion returns user gender type count
def get_user_gender():
	if u_city == "washington":
		user_gender="There is no data available." 
	else:
		user_gender = city_data['Gender'].value_counts()
	return str(user_gender) 

#Fucntion returns oldest user, youngest user and most common birth year
def years_of_birth():
	if u_city == "washington":
		result = "There is no data available." 
	else:
		oldest_user_birth_year=city_data['Birth Year'].min()
		youngest_user_birth_year=city_data['Birth Year'].max()
		most_comon_year_of_birth=city_data['Birth Year'].mode()[0]
		result = "Oldest user: "+str(int(oldest_user_birth_year))+"\n"+"Youngest user: "+str(int(youngest_user_birth_year))+"\n"+"Most common year of birth: "+str(int(most_comon_year_of_birth))
	return result 

# Program Start

print("Hello, welcome to BikeSharing data!")	
u_city=city_selection()
city_data=pd.read_csv(possible_files[u_city])
u_filter=filter_selection()

if u_filter=="month":
	u_month=month_selection()
	print("The most common day of the week in month "+u_month+" is: "+get_most_common_day_of_the_week_by_month(u_month))
	print("The most common hour in month "+u_month+" is: "+get_most_common_hour_by_month(u_month))
	print("Most common start station: "+get_most_common_station(u_month,"Start"))
	print("Most common end station: "+get_most_common_station(u_month,"End"))
	print("The total travel time in month "+u_month+" is: "+get_total_travel_time_by_month(u_month)+" days.")
	print("The average travel time in month "+u_month+" is: "+get_average_travel_time_by_month(u_month)+" minutes.")
	print(u_city+" users have the following user types in month "+u_month+"\n"+get_user_type_count_by_month(u_month))
	#print(u_city+" has the following gender distribution:\n"+get_user_gender_by_month(u_month))
	print(years_of_birth_by_month(u_month))

elif u_filter=="day":
	print("filter day")
	u_day=day_selection()
	print("The most common hour is: "+get_most_common_hour_by_day(u_day))
	print("Most common start station: "+get_most_common_station_by_day(u_day,"Start"))
	print("Most common end station: "+get_most_common_station_by_day(u_day,"End"))
	print("The total travel time for day "+u_day+" is: "+get_total_travel_time_by_day(u_day)+" days.")
	print("The average travel time for day "+u_day+" is: "+get_average_travel_time_by_day(u_day)+" minutes.")
	print(u_city+" users have the following user types on day "+u_day+"\n"+get_user_type_count_by_day(u_day))
	print(u_city+" has the following gender distribution:\n"+get_user_gender_by_day(u_day))
	print(years_of_birth_by_day(u_day))

elif u_filter=="both":
	print("filter both")
	u_month=month_selection()
	u_day=day_selection()
	print("The most common hour for "+u_day+" in month "+u_month+" is: "+get_most_common_hour_by_day_and_month(u_day,u_month))	
	print("The most common start station for "+u_day+" in month "+u_month+" is: "+get_most_common_station_by_day_and_month(u_day,u_month,"Start"))
	print("The most common end station for "+u_day+" in month "+u_month+" is: "+get_most_common_station_by_day_and_month(u_day,u_month,"End"))
	print("The total travel time for day "+u_day+" in month "+u_month+" is: "+get_total_travel_time_by_day_and_month(u_day,u_month)+" days.")
	print("The average travel time for day "+u_day+" in month "+u_month+" is: "+get_average_travel_time_by_day_and_month(u_day,u_month)+" minutes.")
	print(u_city+" users have the following user types on day "+u_day+" in month "+u_month+"\n"+get_user_type_count_by_day_and_month(u_day,u_month))
	print(u_city+" has the following gender distribution:\n"+get_user_gender_by_day_and_month(u_day,u_month))
	print(years_of_birth_by_day_and_month(u_day,u_month))

elif u_filter=="none":
	print("filter none")
	print("Most common month: "+get_most_common_start_month())
	print("The most common day of the week is: "+get_most_common_day_of_the_week())
	print("The most common hour is: "+get_most_common_hour())
	print("The total travel time is: "+get_total_travel_time()+" days.")
	print("The average travel time is: "+get_average_travel_time()+" minutes")
	print("Most common start station: "+get_most_common_station_none("Start"))
	print("Most common end station: "+get_most_common_station_none("End"))
	print("Most frequent start and end combination: "+get_most_frequent_start_end_combination())
	print(u_city+" users have the following user types:\n"+get_user_type_count())
	print(u_city+" has the following gender distribution:\n"+get_user_gender())
	print(years_of_birth())

with open(possible_files[u_city]) as f:
	while input("Would you like to review the raw data? If so input yes.\n") =="yes":
		for line in range(5):
			print(f.readline())




