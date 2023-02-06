# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# alphabetical_order = a list of strings that represent film names. It returns a list of the same films in alphabetical order. 

movies = ['Jaws', 'Superman', 'Valley of the Dolls', 'Home Alone', 'Amistad', 'Memoirs of a Geisha', 'War Horse']
alphabetical_order = sorted(movies)
print(alphabetical_order)

golden_globe_movies = ['Jaws', 'ET', 'Memoirs of a Geisha', 'Star Wars']
movies_lower = []
for movie in golden_globe_movies:
    movies_lower.append(movie.lower())
print(movies_lower)


def won_golden_globe(movies):
    if movies in golden_globe_movies: 
        return True
    else:
        return False

won_golden_globe('Jaws')
print(won_golden_globe('Jaws'))
print(won_golden_globe('Home Alone'))
print(won_golden_globe('Memoirs of a Geisha'))
print(won_golden_globe('War Horse'))

#movies['movie_title'] = movies['movie_title'].str.lower()
# print(result1.lower())
#remove Joseph Toto's albums and return clean list
remove_toto_albums = ['Fahrenheit', 'The Seventh One', 'Toto XX', 'Falling in Between', 'Toto XIV', 'Old Is New', 'World on a String', 'Rhythym in Motion', 'The Five Sacred Trees']
toto_albums = ['Fahrenheit', 'The Seventh One', 'Toto XX', 'Falling in Between', 'Toto XIV', 'Old Is New' ]

for album in toto_albums:
    remove_toto_albums.remove(album)
                 
print(remove_toto_albums)


