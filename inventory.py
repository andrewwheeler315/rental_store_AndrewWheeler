def load_inventory():

    print('Which type of item are you looking for exactly? ')
    item_type = input('Movies, Games, or Anime. ')

    Movies = {
        'Transformers':
        {'Director: Micheal Bay'
         'Genre: Action, Sci-Fi'
         'Price: $1.00'},
        'Deadpool':
        {'Director: Tim Miller'
         'Genre: Comedy, Action'
         'Price: $1.25'},
        'X-Men Origins Wolverine':
        {'Director: Gavin Hood'
         'Genre: Action'
         'Price: $1.50'},
        'Die Hard': {
            'Director: John McTiernan'
            'Genre: Action'
            'Price: $1.75'
        },
        '2012': {
            'Director: Roland Emmerich'
            'Genre: Apocalyptic'
            'Price: $2.00'
        },
        'The Day After Tomorrow': {
            'Director: Roland Emmerich'
            'Genre: Apocalyptic'
            'Price: $2.25'
        },
        'Armageddon': {
            'Director: Micheal Bay'
            'Genre: Apocalyptic'
            'Price: $2.50'
        },
        'Thor': {'Director: Kenneth Branagh'
                 'Genre: Action'
                 'Price: $2.75'},
        'The Lord of the Rings': {
            'Director: Peter Jackson'
            'Genre: Fantasy War'
            'Price: $3.00'
        },
        'The Hobbit': {
            'Director: Peter Jackson'
            'Genre: Fantasy War'
            'Price: $3.25'
        },
        'Harry Potter': {
            'Director: Chris Columbus'
            'Genre: Fantasy'
            'Price: $3.50'
        },
        'Chucky': {'Director: Don Mancini'
                   'Genre: Horror'
                   'Price: $3.75'},
        'A Quiet Place': {
            'Director: John Kransinski'
            'Genre: Horror'
            'Price: $4.00'
        },
        'Escape Plan': {
            'Director: Mikael Hafstrom'
            'Genre: Action'
            'Price: $2.25'
        },
        'Rampage': {'Director: Brad Peyton'
                    'Genre: Action'
                    'Price: $1.50'}
    }

    Games = {
        'Final Fantasy XV':
        {'Director: Hajime Tabata'
         'Genre: RPG'
         'Price: $1.25'},
        'Final Fantasy XIII':
        {'Director: Motomu Toriyama'
         'Genre: ATB RPG'
         'Price: $1.00'},
        'Final Fantasy X':
        {'Director: Yoshinori Kitase'
         'Genre: Turn Based RPG'
         'Price: $0.75'},
        'Final Fantasy X-2': {
            'Director: Motomu Toriyama'
            'Genre: Turn Based RPG'
            'Price: $0.75'
        },
        'Final Fantasy VII': {
            'Director: Yoshinori Kitase'
            'Genre: ATB Turn Based RPG'
            'Price: $0.50'
        },
        "Uncharted 3: Drake's Deception": {
            'Director: Amy Henning'
            'Genre: TPS, Adventure'
            'Price: $2.00'
        },
        "Uncharted 4: A Thief's End": {
            'Director: Amy Henning'
            'Genre: TPS, Adventure'
            'Price: $2.75'
        },
        'Gears of War 3': {
            'Director: Karen Traviss'
            'Genre: TPS, Military Science'
            'Price: $2.25'
        },
        'Gears of War Judgement': {
            'Director: Karen Traviss'
            'Genre: TPS, Military Science'
            'Price: $2.00'
        },
        'God of War 3': {
            'Director: Stig Asmussen'
            'Genre: Mythology, Action'
            'Price: $2.50'
        },
        'God of War 4': {
            'Director: Cory Barlog'
            'Genre: Mythology, Action'
            'Price: $3.00'
        },
        'Doom 4': {
            'Director: Marty Stratton'
            'Genre: Fast Paced, FPS, Sci-Fi'
            'Price: $1.25'
        },
        'GTA V': {'Director: Rockstar'
                  'Genre: Action'
                  'Price: $3.25'},
        'Saints Row IV': {
            'Director: Steve Jaros'
            'Genre: Action'
            'Price: $3.50'
        },
        'Saints Row III': {
            'Director: Scott Phillips'
            'Genre: Action'
            'Price: $1.00'
        }
    }

    Anime = {
        'Fairy Tail':
        {'Director: Hiro Mashima'
         'Genre: Fantasy, Action'
         'Price: $0.25'},
        'Seven Deadly Sins':
        {'Director: Nakaba Suzuki'
         'Genre:  Fantasy, Action'
         'Price: $0.50'},
        'Bleach':
        {'Director: Tite Kubo'
         'Genre: Modern, Action'
         'Price: $0.75'},
        'One Piece': {
            'Director: Eiichiro Oda'
            'Genre: Pirate Action'
            'Price: $1.00'
        },
        'Full Metal Alchemist': {
            'Director: Hiromu Arakawa'
            'Genre:  Action'
            'Price: $1.25'
        },
        'Naruto': {
            'Director: Masashi Kishimoto'
            'Genre: Ninja, Action'
            'Price: $1.50'
        },
        'Inuyasha': {
            'Director:  Rumiko Takahashi'
            'Genre: Action'
            'Price: $1.75'
        },
        'Black Clover': {
            'Director: Yuki Tabata'
            'Genre: Magical Action'
            'Price: $1.50'
        },
        'Black Cat': {
            'Director: Kentaro Yabuki'
            'Genre: Bounty Hunter Action'
            'Price: $1.25'
        },
        'Cowboy Bebop': {
            'Director: Yoko Kanno'
            'Genre: Martial Arts, Action'
            'Price: $1.00'
        },
        'Hellsing': {
            'Director: Kouta Hirano'
            'Genre: Fantasy, Action'
            'Price: $0.75'
        },
        'Dragon Ball Z': {
            'Director: Akria Toriyama'
            'Genre: Martial Arts, Action'
            'Price: $0.50'
        },
        'Beyblade': {'Director: Takao Aoki'
                     'Genre: Action'
                     'Price: $0.25'},
        'Yu-Gi-Oh!': {
            'Director: Kazuki Takahashi'
            'Genre: Card Action'
            'Price: $1.00'
        },
        'My Hero Academia': {
            'Director: Kohei Horikoshi'
            'Genre: Super Hero, Action, Comedy, Motivational'
            'Price: $1.50'
        }
    }


def items_checked_in_or_out(categories):
    ''' (dictionary) -> str

    Takes a dictionary of items and returns a string that shows what is in it 
    and what's not.
    '''
    rented_out = []
    taken_back = []
    for category in categories:
        if categories.get(category) == True:
            rented_out.append(category)
        if categories.get(category) == False:
            taken_back.append(category)
    print('Rented Out: ', ', '.join(rented_out))
    print('Taken Back: ', ', '.join(taken_back))
