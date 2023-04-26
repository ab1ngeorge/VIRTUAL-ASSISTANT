#YOU NEED AN API KEY TO GET THIS APP WORKING
#CREATE AN ACCOUNT IN IMDB SITE TO GET AN APIKEY .THE KEY IS ABOUT 100 CALLS/DAY.

#modules
import flet
from flet import *
import requests                     #make the API calls

APIKEY = "k_5d9w7oqq"

#START WITH THE APP TITLE
class AppTitle(UserControl):
    def __init__(self):
        super().__init__()
    
    def InputContainer(self, width:int):
        return Container(
            width=width,
            height=40,
            bgcolor='white10',
            border_radius=8,
            padding=8,
            content=Row(
                
                spacing=10,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Icon(name=icons.SEARCH_ROUNDED, size=17, opacity=0.8,),
                    TextField(
                        border_color='transparent',
                        height=20,
                        text_size=14,
                        cursor_color="white",
                        content_padding=0,
                        cursor_width=1,
                        color='white',
                        hint_text='Search',
                        
                    )
                ],
            ),
            
        )
    
    def build(self):
        return Container(
            padding=padding.only(top=20, left=15, right=15),
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Text(
                        "IMDb Movies & Shows",
                        size=15,
                        weight='bold',
                        
                    ),
                    Divider(height=5, color="transparent"),
                    self.InputContainer(280),
                    Divider(height=20, color="white10"),
                ]
            )
        )

#COMING SOON MOVIES
class ComingSoon(UserControl):
    def __init__(self):
        super().__init__()
    
    def CommingSoonTitle(self):
        #API CALL WILL GO HERE....
        #THE API REQUESTS:
        res = requests.get('https://imdb-api.com/en/API/ComingSoon/' + APIKEY)
        #SO HERE WE CAN GET THE API CALL FROM THE DOCS ON IMDB => 
        #THE DOCUMENTATION HAS SEVERAL TYPES OF DATA: COMING SOON,TOP 250,TOP TV SHOWS,TOP MOVIES,etc...        
        
        
        self.movie_list = GridView(
            expand=True,
            child_aspect_ratio=1.65,
            horizontal=True,                    #MAKES THE GRIDS HORIZONTAL
            
        )

        #HERE I'M LOOPING THROUGH THE JSON FILE THAT WE GET FROM THE ABOVE REQUEST
        #THE JSON FILE HAS A MAIN KEY CALLED ITEMS AND EACH MOVIE HAS A NUMERICAL KEY 0-etc.
        #I SIMPLY WANT THE LENGTH OF THE JSON ITEMS TO PASS INTO THE RANGE()FUNCTION TO START MY LOOP
        #I CAN ACCESS THE INFO WITHIN THE LOOP ITSELF.
        #SUBSTRACT 112 FROM THE RANGE BECAUSE I DON'T NEED 133 MOVIE TITLES: 
        
        for movie in range(len(res.json()['items']) -112):
            self.movie_list.controls.append(
                Column(
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        Container(
                            expand=9,
                            border_radius=12,
                            image_fit=ImageFit.FILL,
                            image_src=res.json()['items'][movie]['image']

                            #THE ABOVE RESPONSE GET US THE LINK TO THE MOVIE POSTER.
                        ),
                        Column(
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            expand=2,
                            spacing=2,
                            controls=[
                                Text(
                                    res.json()['items'][movie]['title'],
                                    size=11,
                                    no_wrap=True,                #OVERFLOW ENABLED
                                ),
                                Text(
                                    res.json()['items'][movie]['releaseState'],
                                    size=9,
                                    color="white54",
                                    no_wrap=True,                #OVERFLOW ENABLED
                                ),
                            ],
                        ),
                    ],
                )
            )
        
        
        return self.movie_list
    
    def build(self):
        return Container( 
            width=1000,
            height=240,
            content=Column(
                controls=[
                    Row(
                        
                        controls=[
                            Text(
                                "Coming Soon",
                                size=14,
                            )
                        ]
                    ),
                    self.CommingSoonTitle(),
                    ],
            ),
        )

#FINALLY, WE CAN GRAB THE TRENDING TV SHOWS
class TopTvShows(UserControl):
    def __init__(self):
        super().__init__()
    
    def TrendingTvShows(self):
        #SAME CALL AS THE ABOVE BUT DIFFERENT API LINK
        res = requests.get('https://imdb-api.com/API/MostPopularTVs/' + APIKEY)
        
        self.tv_list = GridView(
            child_aspect_ratio=1.2,
            expand=True,
            horizontal=True,
            spacing=25,
        )
        
        for show in range(len(res.json()['items']) - 80):
            self.tv_list.controls.append(
                Column(
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        Container(
                            expand=9,
                            border_radius=12,
                            image_fit=ImageFit.FILL,
                            image_src=res.json()['items'][show]['image']

                            #THE ABOVE RESPONSE GET US THE LINK TO THE MOVIE POSTER.
                        ),
                        Column(
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            expand=2,
                            spacing=2,
                            controls=[
                                Text(
                                    res.json()['items'][show]['title'],
                                    size=11,
                                    no_wrap=True,                   #OVERFLOW ENABLED
                                ),
                                Text(
                                    res.json()['items'][show]['year'],
                                    size=9,
                                    color="white54",
                                    no_wrap=True,                   #OVERFLOW ENABLED
                                ),
                            ],
                        ),
                    ],
                )
            )
        
        return self.tv_list
    
    
    def build(self):
        return Container(
            width=1000,
            height=240,
            clip_behavior=ClipBehavior.HARD_EDGE,
            content=Column(
                controls=[
                    Row(
                        controls=[
                            Text(
                            "Trending TV Shows",
                            size=14,
                            ),
                        ],
                    ),
                    self.TrendingTvShows(),
                ],
                ),
        )

#MAIN PAGE

def main(page: Page):
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment = MainAxisAlignment.CENTER
    print(page.width)
    print(page.height)
    page.bgcolor = '#33354a','#2f3143','#2f3143','#292b3c','#222331',"#222331",'#1a1a25','#1a1b26','#1a1b26','#21222f','#1d1e2a','black'
    
    #MAIN CONTAINER
    _main_ = Container(
        width=1000,
        height=685,
        
        #GRADIENT
        gradient=RadialGradient(
            center=Alignment(-0.5, -0.8),
            radius=3,
            colors=[
                '#33354a',
                '#2f3143',
                '#2f3143',
                '#292b3c',
                '#222331',
                "#222331",
                '#1a1a25',
                '#1a1b26',
                '#1a1b26',
                '#21222f',
                '#1d1e2a',
                'black',
            ],
        ),
        border_radius=30,
        border=border.all(2, "black"),
        padding=10,
        clip_behavior=ClipBehavior.HARD_EDGE, 
        #CLIP THE INNER CONTENT TO PREVENT OVERFLOW

       

        content=Column(
            scroll='none',
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                #WE ADD THE CLASSES ACCORDINGLY HERE....
                AppTitle(),
                Container(
                    expand=True,
                    padding=10,
                    content=Column(
                        scroll='hidden',
                        controls=[
                            ComingSoon(),
                            Divider(height=10, color='white10'),
                            TopTvShows(),
                            
                            
                        ]
                    )
                )
            ]
        )
        
    )
    page.add(_main_)
    page.update()
    

if __name__ == "__main__":
    flet.app(target=main)