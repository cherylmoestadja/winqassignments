# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# alphabetical_order = a list of strings that represent film names. It returns a list of the same films in alphabetical order. 


movies = ['Jaws', 'Superman', 'Valley of the Dolls', 'Home Alone', 'Amistad', 'Memoirs of a Geisha', 'War Horse']
def alphabetical_order(movies):
    return sorted(movies)
print(alphabetical_order(movies))

golden_globe_movies = ['Jaws', 'ET', 'Memoirs of a Geisha', 'Star Wars']
movies_lower = [movies.lower() for movies in golden_globe_movies]
print(movies_lower)

def won_golden_globe(movies):
    if 'Jaws'in movies or 'Jaws'.lower() in movies or 'Jaws'.upper() in movies: 
        return True
    if 'Memoirs of a Geisha'in movies or 'Memoirs of a Geisha'.lower() in movies or 'Memoirs of a Geisha'.upper() in movies:  
        return True 
    if 'ET'in movies or 'ET'.lower() in movies or 'ET'.upper() in movies:  
        return True
    if 'Star Wars'in movies or 'Star Wars'.lower() in movies or 'Star Wars'.upper() in movies:  
        return True
    else:
        return False

print(won_golden_globe('Jaws'))
print(won_golden_globe('jaws'))
print(won_golden_globe('superman'))
print(won_golden_globe('star wars'))


#movies['movie_title'] = movies['movie_title'].str.lower()
# print(result1.lower())
#remove Joseph Toto's albums and return clean list
list_albums = ['Fahrenheit', 'The Seventh One', 'Falling in Between','Toto XX','World on a String', 'Toto XIV','Old Is New','Rhythym in Motion', 'The Five Sacred Trees']
toto_albums = ['Fahrenheit', 'The Seventh One', 'Toto XX','Falling in Between','Toto XIV','Old Is New'] 
# albums_john = 'World on a String', 'Rhythym in Motion', 'The Five Sacred Trees'
def remove_toto_albums(list_albums):
        if 'Fahrenheit' in list_albums:
            list_albums.remove('Fahrenheit')
        if 'The Seventh One'in list_albums:
            list_albums.remove('The Seventh One')
        if 'Old Is New' in list_albums:
            list_albums.remove('Old Is New')
        if 'Toto XX' in list_albums:
            list_albums.remove('Toto XX')
        if 'Falling in Between' in list_albums:
            list_albums.remove('Falling in Between')
        if 'Toto XIV' in list_albums:
            list_albums.remove('Toto XIV')
        return list_albums
        
print(remove_toto_albums(list_albums))


    












