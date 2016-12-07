# pitchfx_finalproject

In order to run this app:

    First, run the server:

    python manage.py runserver

    Copy and paste this ("http://127.0.0.1:8000/myapp/") into your web browser to run it.
    You can choose one of two forms in the navbar. You can either filter by demographic variables under "Pitches" or by pitcher under "Pitches by Player".
    Use the form to create the graph you are interested in (pick the race, ethnicity, and game status (home/away)). The press "Go!"

Once you do this, a graph will display itself underneath the form. Please feel free to change the graph you are looking at by playing around with the dropdown menus.

If you would like to learn more about the data we've used and how we created this data, click on the "Readme" header at the top of the page or just click this, or type into your browser "http://127.0.0.1:8000/myapp/ourdata/." If you would like to see the website from where we found the data, click on "PITCHf/x".

Methodology and Our Data Used:

PITCHf/x records the location of every pitch and every major league game, along with identifying information on pitchers, batters, umpires, game situations, and game locations. PITCHf/x data are rich, but also arduous to parse through. Fortunately, other baseball researchers have written python-based parsers to scrape and compile data. The dataset that we scraped only includes regular season games, and pitchers who pitched more than 160 innings during the 2016 season. The variables from this dataset include:
Pitcher ID
Whether the game was home or away
The field at which the game was played
The call of the pitch
And the location of the pitch based on the hight and distance away from the center of the plate.

Our second dataset is a CSV file we made using PITCHf/x pitcher IDs. Using these IDs, we recorded the pitcher's name, race, and ethnicity (Hispanic or not Hispanic). We coded race and ethnicity by looking at photos of each pitcher (as this is how it was done in other baseball research). We then merged the two datasets based on pitcher ID.

We used PITCHf/x data to plot pitch locations on an x-y coordinate plane, and code each pitch as a called ball or strike. The web app that we built allows the user to set parameters for which pitches are displayed based on PITCHf/x and Baseball Reference data – e.g. all pitches to black batters in home games.
Previous Research

Some previous work has been done on umpire bias, ranging from Internet blog reporting to Hamermesh’s paper on umpires’ racial bias towards pitchers, see here: http://sabr.org/research/there-racial-bias-among-umpires. Due to lack of time and access to umpire data (while we have umpire codes, we cannot find umpire names or races that correspond to them), we were unable to include "umpire race" as a variable. Our project also did not undertake such deep econometric analyses, but simply provides a useful tool for visualizing differences in ball and strike calls based on a variety of parameters. One reservation about this project is that it seems like a “non-finding” is fairly likely without more intricate statistical analyses.
