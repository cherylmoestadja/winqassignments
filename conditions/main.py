# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

#weather: 'rainy','sunny','windy','neutral'
#time of day: 'day','night'
#cow milking status: 'True', 'False' 
#location cows: 'pasture', 'cowshed'
#season: 'spring', 'summer', 'fall', 'winter'
#slurry tank: 'True', 'False'
#grass status_long: 'True', 'False'
def farm_action(weather, time_of_day, cow_milking_status, location_cows, season, slurry_tank, grass_status_long):
    if time_of_day == 'night' and location_cows == 'pasture':
        return('take cows to cowshed')
    elif weather == 'rainy':
        return('take cows to cowshed')
    elif cow_milking_status == True and location_cows == 'cowshed': 
        return('milk cows')
    elif slurry_tank == True and location_cows == 'cowshed' and weather != 'sunny'and weather != 'windy':
        return('fertilize pasture')
    elif grass_status_long == True and season == 'spring' and weather == 'sunny' and location_cows != 'pasture':
        return('mow grass')
    if weather == 'sunny' and time_of_day == 'day' and cow_milking_status == True and location_cows == 'pasture' and season == 'spring' and slurry_tank == False and grass_status_long == True:
        return ('take cows to cowshed \nmilk cows \ntake cows back to pasture')
    else:
        return('wait')

print(farm_action('rainy', 'night', True, 'pasture', 'spring', True, True))
print(farm_action('sunny', 'day', True, 'pasture', 'spring', False, True))


