from django.db import models

# Create your models here.
PITCHER_RACE = (
                ('Black', 'Black'),
                ('White', 'White'),
                ('Asian', 'Asian'),
                ('Other', 'Other')
    )

PITCHER_ETHNICITY = (
                    ('0', 'Non-Hispanic' ),
                    ('1', 'Hispanic')
)

HOME_OR_AWAY = (
                ('0', 'Away' ),
                ('1', 'Home')
)

PITCHER_NAME = (
                ('Aaron Sanchez', 'Aaron Sanchez'),
                ('Adam Wainwright','Adam Wainwright'),
                ('Anibal Sanchez', 'Anibal Sanchez'),
                ('Archie Bradley', 'Archie Bradley'),
                ('Bartolo Colon', 'Bartolo Colon'),
                ('Brandon Finnegan', 'Brandon Finnegan'),
                ('Carlos Carrasco', 'Carlos Carrasco'),
                ('Carlos Martinez', 'Carlos Martinez'),
                ('Carlos Rodon', 'Carlos Rodon'),
                ('CC Sabathia', 'CC Sabathia'),
                ('Chad Bettis', 'Chad Bettis'),
                ('Chase Anderson', 'Chase Anderson'),
                ('Chris Archer', 'Chris Archer'),
                ('Chris Sale', 'Chris Sale'),
                ('Chris Tillman', 'Chris Tillman'),
                ('Clayton Kershaw', 'Clayton Kershaw'),
                ('Cole Hamels', 'Cole Hamels'),
                ('Collin McHugh', 'Collin McHugh'),
                ('Corey Kluber', 'Corey Kluber'),
                ('Dallas Keuchel', 'Dallas Keuchel'),
                ('Dan Straily', 'Dan Straily'),
                ('Danny Duffy', 'Danny Duffy'),
                ('David Price', 'David Price'),
                ('Doug Fister', 'Doug Fister'),
                ('Drew Pomeranz', 'Drew Pomeranz'),
                ('Drew Smyly', 'Drew Smyly'),
                ('Edinson Volquez', 'Edinson Volquez'),
                ('Ervin Santana', 'Ervin Santana'),
                ('Felix Hernandez', 'Felix Hernandez'),
                ('Francisco Liriano', 'Francisco Liriano'),
                ('Gio Gonzalez', 'Gio Gonzalez'),
                ('Hector Santiago', 'Hector Santiago'),
                ('Hisashi Iwakuma', 'Hisashi Iwakuma'),
                ('Ian Kennedy', 'Ian Kennedy'),
                ('Ivan Nova', 'Ivan Nova'),
                ('J.A. Happ', 'J.A. Happ'),
                ('Jacob deGrom', 'Jacob deGrom'),
                ('Jaime Garcia', 'Jaime Garcia'),
                ('Jake Arrieta', 'Jake Arrieta'),
                ('Jake Odorizzi', 'Jake Odorizzi'),
                ('James Shields', 'James Shields'),
                ('Jason Hammel', 'Jason Hammel'),
                ('Jeff Samardzija', 'Jeff Samardzija'),
                ('Jerad Eickhoff', 'Jerad Eickhoff'),
                ('Jered Weaver', 'Jered Weaver'),
                ('Jeremy Hellickson', 'Jeremy Hellickson'),
                ('Jhoulys Chacin', 'Jhoulys Chacin'),
                ('Jimmy Nelson', 'Jimmy Nelson'),
                ('John Lackey', 'John Lackey'),
                ('Johnny Cueto', 'Johnny Cueto'),
                ('Jon Gray', 'Jon Gray'),
                ('Jon Lester', 'Jon Lester'),
                ('Jose Fernandez', 'Jose Fernandez'),
                ('Jose Quintana', 'Jose Quintana'),
                ('Josh Tomlin', 'Josh Tomlin'),
                ('Julio Teheran', 'Julio Teheran'),
                ('Justin Verlander', 'Justin Verlander'),
                ('Kendall Graveman', 'Kendall Graveman'),
                ('Kenta Maeda', 'Kenta Maeda'),
                ('Kevin Gausman', 'Kevin Gausman'),
                ('Kyle Gibson', 'Kyle Gibson'),
                ('Kyle Hendricks', 'Kyle Hendricks'),
                ('Luis Perdomo', 'Luis Perdomo'),
                ('Madison Bumgarner', 'Madison Bumgarner'),
                ('Marco Estrada', 'Marco Estrada'),
                ('Marcus Stroman', 'Marcus Stroman'),
                ('Martin Perez', 'Martin Perez'),
                ('Masahiro Tanaka', 'Masahiro Tanaka'),
                ('Matt Moore', 'Matt Moore'),
                ('Matt Shoemaker', 'Matt Shoemaker'),
                ('Matt Wisler', 'Matt Wisler'),
                ('Max Scherzer', 'Max Scherzer'),
                ('Michael Fulmer', 'Michael Fulmer'),
                ('Michael Pineda', 'Michael Pineda'),
                ('Mike Fiers', 'Mike Fiers'),
                ('Mike Leake', 'Mike Leake'),
                ('Noah Syndergaard', 'Noah Syndergaard'),
                ('Patrick Corbin', 'Patrick Corbin'),
                ('R.A. Dickey', 'R.A. Dickey'),
                ('Rick Porcello', 'Rick Porcello'),
                ('Ricky Nolasco', 'Ricky Nolasco'),
                ('Robbie Ray', 'Robbie Ray'),
                ('Sean Manaea', 'Sean Manaea'),
                ('Stephen Strasburg', 'Stephen Strasburg'),
                ('Steven Wright', 'Steven Wright'),
                ('Tanner Roark', 'Tanner Roark'),
                ('Tom Koehler', 'Tom Koehler'),
                ('Trevor Bauer', 'Trevor Bauer'),
                ('Tyler Chatwood', 'Tyler Chatwood'),
                ('Ubaldo Jimenez', 'Ubaldo Jimenez'),
                ('Wade Miley', 'Wade Miley'),
                ('Yordano Ventura', 'Yordano Ventura'),
                ('Zach Davies', 'Zach Davies'),
                ('Zack Greinke', 'Zack Greinke')
)

# PARK_NAME = (
#             # ('Angel Stadium of Anaheim' 'AT&T Park' 'Busch Stadium' 'Chase Field' 'Citi Field' 'Citizens Bank Park' 'Comerica Park'
#             # 'Coors Field' 'Dodger Stadium' 'Fenway Park' 'Fort Bragg Field' 'Globe Life Park in Arlington'
#             # 'Great American Ball Park' 'Kauffman Stadium' 'Marlins Park' 'Miller Park' 'Minute Maid Park'
#             # 'Nationals Park' 'Oakland Coliseum' 'Oriole Park at Camden Yards' 'Peoria Stadium' 'Petco Park'
#             # 'PNC Park' 'Progressive Field' 'Rogers Centre' 'Safeco Field' 'Target Field' 'Tropicana Field'
#             # 'Turner Field' 'U.S. Cellular Field' 'Wrigley Field' 'Yankee Stadium', 'All'), #trying to get an ALL field....
#             ('Angel Stadium of Anaheim', 'Angel Stadium of Anaheim'),
#             ('AT&T Park', 'AT&T Park'),
#             ('Busch Stadium', 'Busch Stadium'),
#             ('Chase Field', 'Chase Field'),
#             ('Citi Field', 'Citi Field'),
#             ('Citizens Bank Park', 'Citizens Bank Park'),
#             ('Comerica Park', 'Comerica Park'),
#             ('Coors Field', 'Coors Field'),
#             ('Dodger Stadium', 'Dodger Stadium'),
#             ('Fenway Park', 'Fenway Park'),
#             ('Fort Bragg Field', 'Fort Bragg Field'),
#             ('Globe Life Park in Arlington', 'Globe Life Park in Arlington'),
#             ('Great American Ball Park', 'Great American Ball Park'),
#             ('Kauffman Stadium', 'Kauffman Stadium'),
#             ('Marlins Park', 'Marlins Park'),
#             ('Miller Park', 'Miller Park'),
#             ('Minute Maid Park', 'Minute Maid Park'),
#             ('Nationals Park', 'Nationals Park'),
#             ('Oakland Coliseum', 'Oakland Coliseum'),
#             ('Oriole Park at Camden Yards', 'Oriole Park at Camden Yards'),
#             ('Peoria Stadium', 'Peoria Stadium'),
#             ('Petco Park', 'Petco Park'),
#             ('PNC Park', 'PNC Park'),
#             ('Progressive Field', 'Progressive Field'),
#             ('Rogers Centre', 'Rogers Centre'),
#             ('Safeco Field', 'Safeco Field'),
#             ('Target Field', 'Target Field'),
#             ('Tropicana Field', 'Tropicana Field'),
#             ('Turner Field', 'Turner Field'),
#             ('U.S. Cellular Field', 'U.S. Cellular Field'),
#             ('Wrigley Field', 'Wrigley Field'),
#             ('Yankee Stadium', 'Yankee Stadium')
# )


RACE_DICT = dict(PITCHER_RACE)
ETHNICITY_DICT = dict(PITCHER_ETHNICITY)
# PARK_NAME_DICT = dict(PARK_NAME)
HOME_DICT = dict(HOME_OR_AWAY)
NAME_DICT = dict(PITCHER_NAME)

class Input(models.Model):
    pitcher_race = models.CharField(max_length=50, choices=PITCHER_RACE)
    pitcher_ethnicity = models.CharField(max_length=50, choices=PITCHER_ETHNICITY)
    # park_name = models.CharField(max_length=50, choices=PARK_NAME)
    home_or_away = models.CharField(max_length=50, choices=HOME_OR_AWAY)
    pitcher_name = models.CharField(max_length=50, choices=PITCHER_NAME)
