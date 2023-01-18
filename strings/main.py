# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#Every player that scored
player_one = 'Ruud Gullit'
player_two = 'Marco van Basten'

#Each minute a goal was scored
goal_0 = 32
goal_1 = 54

#Who scored when
scorers = player_one + " " + str(goal_0) + "," + " "+ player_two + " " + str(goal_1)
print(scorers)
report = (player_one + " scored in the " + str (goal_0) + "nd minute\n") + (player_two + " scored in the " + str (goal_1) + "th minute") 
print(report)

# Choose a player that played in the soccer match       
player = 'Ronald Koeman'
first_name_length = player.find(' ')
print(first_name_length)
first_name = player[0:first_name_length]
last_name = player[first_name_length +1:]
print(first_name)
print(last_name)
last_name_len = len(last_name)
print(last_name_len)
name_short = player[0] + "." + " " + last_name

chant_name = first_name + "!" + " "
print(chant_name)
chant = chant_name * first_name_length 
chant = chant[0:-1]

print(chant)

good_chant = (chant != chant_name) 
print(good_chant)