# Current features:  
Displays pokemon, ability to toggle between shiny and non-shiny form  
Displays pokemon's information, barebones pokedex entry page  
Search bar for pokemon's name does no sanitization and fail into eevee image  
  
# To come:  
Need main screen to allow user to select which feature to use  
Height comparison, ability to add, change, and remove pokemon  
Completed pokedex entry  
Guess that pokemon with black silhouette  
Guess that pokemon with negative space (Allow user to see some features => easier version)  
Guess the shiny with differing color shading  
Display all pokemon of a certain type  
Be able to use session cookies to store longest streak of correct answers for guessing features, independent scores  
  
# In making Github Pages:  
Launching atlas toolkit, the URL is always http://faas1.q37.info/xdh.php?_token={} so we can redirect
index.html pretty simply granted we have the token. Just need to understand the token generation and
if anything about the toolkit breaks  
Alternatively execute all the python code as javascript code and just change the dom fields accordingly  

# To run:  
Needs the image files first, which can be gathered from the image downloader, then passed through the vtracer with `parse_svg.py`.  
Atlas-python doesn't run on 3.11 yet so run with 3.10 or earlier, `python3 main.py`.  
  
## Adapted code from:  
https://github.com/epeios-q37/atlas-python  
https://github.com/HybridShivam/Pokemon  
https://github.com/visioncortex/vtracer  
