import wikipedia


def collect_links_from_wikipedia_page(s):
    for link in wikipedia.page(s).links:
        if link.upper() != link and all(chr.isalpha() or chr == " " for chr in link):
            yield link


# def y1():
#     """Associated with computers"""
#     return collect_links_from_wikipedia_page("computer")

# def y2():
#     """Associated with transportation"""
#     return collect_links_from_wikipedia_page("transportation")

# def y3():
#     """Associated with space"""
#     return collect_links_from_wikipedia_page("Outer space")

# def y4():
#     """Associated with politics"""
#     return collect_links_from_wikipedia_page("politics")

# def y5():
#     """Associated with beach"""
#     return collect_links_from_wikipedia_page("beach")

# def y6():
#     """Associated with time"""
#     return collect_links_from_wikipedia_page("time")

# def y7():
#     """Associated with literature"""
#     return collect_links_from_wikipedia_page("literature")

# def y8():
#     """Associated with music"""
#     return collect_links_from_wikipedia_page("music")

# def y9():
#     """Associated with crime"""
#     return collect_links_from_wikipedia_page("crime")

# def y10():
#     """Associated with vacation"""
#     return collect_links_from_wikipedia_page("vacation")

# def y11():
#     """Associated with art"""
#     return collect_links_from_wikipedia_page("art")

# def y12():
#     """Associated with school"""
#     return collect_links_from_wikipedia_page("school")

# def y13():
#     """Associated with sports"""
#     return collect_links_from_wikipedia_page("sports")

# def y14():
#     """Associated with love"""
#     return collect_links_from_wikipedia_page("love")

# def y15():
#     """Associated with money"""
#     return collect_links_from_wikipedia_page("money")

# def y16():
#     """Associated with family"""
#     return collect_links_from_wikipedia_page("family")

# def y17():
#     """Associated with math"""
#     return collect_links_from_wikipedia_page("math")

# def y18():
#     """Associated with parties"""
#     return collect_links_from_wikipedia_page("parties")

# def y19():
#     """Associated with the human body"""
#     return collect_links_from_wikipedia_page("human body")

# def y20():
#     """Associated with weather"""
#     return collect_links_from_wikipedia_page("weather")

# def y21():
#     """Associated with science"""
#     return collect_links_from_wikipedia_page("science")

def y22():
    """A type of plant"""
    return collect_links_from_wikipedia_page("List of plants by common name")

def y23():
    """A type of animal"""
    return collect_links_from_wikipedia_page("List of animal names")

def y24():
    """The name of a country"""
    # from https://en.wikipedia.org/wiki/List_of_sovereign_states
    return ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola',
    'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria',
    'Azerbaijan', 'The Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
    'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina',
    'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi',
    'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic',
    'Chad', 'Chile', 'China', 'Colombia', 'Comoros',
    'Democratic Republic of the Congo', 'Republic of the Congo', 'Costa Rica',
    'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti',
    'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt',
    'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini',
    'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'The Gambia', 'Georgia',
    'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea',
    'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland',
    'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy',
    'Ivory Coast', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya',
    'Kiribati', 'North Korea', 'South Korea', 'Kuwait', 'Kyrgyzstan', 'Laos',
    'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein',
    'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives',
    'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico',
    'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco',
    'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands',
    'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Norway',
    'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua New Guinea',
    'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania',
    'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia',
    'Saint Vincent and the Grenadines', 'Samoa', 'San Marino',
    'São Tomé and Príncipe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles',
    'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands',
    'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan',
    'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Tajikistan', 'Tanzania',
    'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey',
    'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates',
    'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu',
    'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']

def y25():
    """The name of a game"""
    return collect_links_from_wikipedia_page('List of abstract strategy games') \
         + collect_links_from_wikipedia_page('List of board games')

def y26():
    """The title of a movie"""
    # TODO: this will return many false positives. Either scan manually or get
    # a better data source?
    return collect_links_from_wikipedia_page('List of films considered the best')

def y27():
    """The title of a TV show"""
    links = []
    for startswith in 'numbers A B C D E F G H I-J K-L M N O P Q-R S T U-V-W X-Y-Z'.split():
        links += collect_links_from_wikipedia_page(f"List of television programs: {startswith}")
    return links

def y28():
    """The name of a brand"""
    links = []
    for list in collect_links_from_wikipedia_page('Lists of brands'):
        links += collect_links_from_wikipedia_page(list)
    return links

def y29():
    """A type of profession"""
    categories = ['healthcare',
 'mental health',
 'artistic',
 'dance',
 'entertainer',
 'film and television',
 'writing',
 'industrial',
 'metalworking',
 'railway industry',
 'scientific']
    links = []
    for category in categories:
        links += collect_links_from_wikipedia_page(f"List of {category} occupations")
    return links

def y30():
    """A type of food"""
    links = []
    for list in [link for link in collect_links_from_wikipedia_page('Lists of foods') if link.startswith('List of ')]:
        links += collect_links_from_wikipedia_page(list)
    return links

def y31():
    """An article of clothing"""
    links = []
    for link in collect_links_from_wikipedia_page("Index of fashion articles"):
        link = link.split(' (')[0] # Belt (clothing) => Belt
        if any(chr.isnumeric() for chr in link):
            pass
        links.append(link)
    return links

def y32():
    """An item found in a kitchen"""
    return collect_links_from_wikipedia_page('List of food preparation utensils')

def y33():
    """An item found at the office"""
    return collect_links_from_wikipedia_page('Office Supplies')

def y34():
    """An object visible from here"""
    # This one won't be generally solvable. But here are some things we can
    # generally assume!
    return ['card', 'cards', 'deck', 'box', 'player', 'friend', 'floor',
    'person', 'hand', 'foot', 'arm', 'leg', 'face']
