from django.db import models

# Create your models here.

Pitcher_Race = (
                ('Black', 'Black'),
                ('White', 'White'),
                ('Asian', 'Asian'),
                ('Other', 'Other'),
                ('Black' 'White' 'Asian' 'Other', 'All') #trying to make a dropdown that allows us to plot not based on race
    )
Race_dict = dict(Pitcher_Race)
class Input(models.Model):
    Pitcher_Race = models.CharField(max_length=50, choices=Pitcher_Race)

Pitcher_Ethnicity = (
                    ('0', 'Non-Hispanic' ),
                    ('1', 'Hispanic'),
                    ('0' '1', "All") #trying to make a dropdown that allows us to plot not based on race
)
class Input(models.Model):
    Pitcher_Ethnicity = models.CharField(max_length=50, choices=Pitcher_Ethnicity)

Park_Name = (
            ('Angel Stadium of Anaheim' 'AT&T Park' 'Busch Stadium' 'Chase Field' 'Citi Field' 'Citizens Bank Park' 'Comerica Park'
            'Coors Field' 'Dodger Stadium' 'Fenway Park' 'Fort Bragg Field' 'Globe Life Park in Arlington'
            'Great American Ball Park' 'Kauffman Stadium' 'Marlins Park' 'Miller Park' 'Minute Maid Park'
            'Nationals Park' 'Oakland Coliseum' 'Oriole Park at Camden Yards' 'Peoria Stadium' 'Petco Park'
            'PNC Park' 'Progressive Field' 'Rogers Centre' 'Safeco Field' 'Target Field' 'Tropicana Field'
            'Turner Field' 'U.S. Cellular Field' 'Wrigley Field' 'Yankee Stadium', 'All'), #trying to get an ALL field....
            ('Angel Stadium of Anaheim', 'Angel Stadium of Anaheim'),
            ('AT&T Park', 'AT&T Park'),
            ('Busch Stadium', 'Busch Stadium'),
            ('Chase Field', 'Chase Field'),
            ('Citi Field', 'Citi Field'),
            ('Citizens Bank Park', 'Citizens Bank Park'),
            ('Comerica Park', 'Comerica Park'),
            ('Coors Field', 'Coors Field'),
            ('Dodger Stadium', 'Dodger Stadium'),
            ('Fenway Park', 'Fenway Park'),
            ('Fort Bragg Field', 'Fort Bragg Field'),
            ('Globe Life Park in Arlington', 'Globe Life Park in Arlington'),
            ('Great American Ball Park', 'Great American Ball Park'),
            ('Kauffman Stadium', 'Kauffman Stadium'),
            ('Marlins Park', 'Marlins Park'),
            ('Miller Park', 'Miller Park'),
            ('Minute Maid Park', 'Minute Maid Park'),
            ('Nationals Park', 'Nationals Park'),
            ('Oakland Coliseum', 'Oakland Coliseum'),
            ('Oriole Park at Camden Yards', 'Oriole Park at Camden Yards'),
            ('Peoria Stadium', 'Peoria Stadium'),
            ('Petco Park', 'Petco Park'),
            ('PNC Park', 'PNC Park'),
            ('Progressive Field', 'Progressive Field'),
            ('Rogers Centre', 'Rogers Centre'),
            ('Safeco Field', 'Safeco Field'),
            ('Target Field', 'Target Field'),
            ('Tropicana Field', 'Tropicana Field'),
            ('Turner Field', 'Turner Field'),
            ('U.S. Cellular Field', 'U.S. Cellular Field'),
            ('Wrigley Field', 'Wrigley Field'),
            ('Yankee Stadium', 'Yankee Stadium')
)
class Input(models.Model):
    Park_Name = models.CharField(max_length=50, choices=Park_Name)


Home_or_Away = (
                ('0', 'Away' ),
                ('1', 'Home')
)
class Input(models.Model):
    Home_or_Away = models.CharField(max_length=50, choices=Home_or_Away)
