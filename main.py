# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

#define a function greet
def greet(name, greeting_template = 'Hello, <name>!'):
    greeting_message = greeting_template.replace('<name>', name)
    return greeting_message


name = 'Kim'
greeting_template = 'Hello, <name>!'
greeting_message = greet(name, greeting_template)
print(greeting_message)

#write a function force
def force(mass, body = 'earth'):
    gravity = {
        'sun': 274,
        'mercury': 3.7,
        'venus': 8.9,
        'earth': 9.8,
        'moon': 1.6,
        'mars': 3.7,
        'jupiter': 23.1,
        'saturn': 10.4,
        'uranus': 8.7,
        'neptune': 11.0,
        'pluto': 0.58
    }  
  
    gravity = round(gravity[body.lower()], 1)
    force = mass * gravity
    return force


#define a function pull
def pull(m1, m2, d):
    
    G = 6.674*10**-11
    force = G*(m1*m2)/d**2
    return force  
