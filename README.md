# pitchfx_finalproject

In order to run this app, first run the server:
"python manage.py runserver"

Then copy and paste "http://127.0.0.1:8000/myapp/form/" into your web browser to run it.

Use the form to create the graph you are interested in (pick the race, ethnicity, and game status (home/away)).  The press "Go!"  

Once you do this, a graph will display itself underneath the form.  Please feel free to change the graph you are looking at by playing around with the dropdown menus.

If you would like to learn more about the data we've used and how we created this data, click on the "Read Me" header at the top of the page (or type into your browser "http://127.0.0.1:8000/myapp/ourdata/").  If you would like to see the website from where we found the data, click on "pitchFX".  


AIM/GOAL:

The question: is there a relationship between a batter and pitcher characteristics and the balls and strikes called against them in the MLB? PITCHf/x records the location of every pitch and every major league game, along with identifying information on pitchers, batters, umpires, game situations, and game locations. PITCHf/x data are rich, but also arduous to parse through. Fortunately, other baseball researchers have written python-based parsers to scrape and compile data.  The dataset that we scraped only includes regular season games, and pitchers who pitched more than 160 innings during the 2016 season.  The variables from this dataset include pitcher ID, whether the game was home or away, the field at which the game was played, the call of the pitch, and the location of the pitch based on the hight and distance away from the center of the plate. Our second dataset is a CSV file we made using PITCHf/x pitcher IDs.  Using these IDs, we recorded the pitcher's name, race, and ethnicity (Hispanic or not Hispanic).  We coded race and ethnicity by looking at photos of each pitcher (as this is how it was done in other baseball research).  We then merged the two datasets based on pitcher ID.  

We used PITCHf/x data to plot pitch locations on an x-y coordinate plane, and code each pitch as a called ball or strike. The web app that we built allows the user to set parameters for which pitches are displayed based on PITCHf/x and Baseball Reference data – e.g. all pitches to black batters in home games.

Some previous work has been done on umpire bias, ranging from Internet blog reporting to Hamermesh’s paper on umpires’ racial bias towards pitchers. Our project would not undertake such deep econometric analyses, but would provide a useful tool for visualizing differences in ball and strike calls based on a variety of parameters. One reservation about this project is that it seems like a “non-finding” is fairly likely without more intricate statistical analyses.
