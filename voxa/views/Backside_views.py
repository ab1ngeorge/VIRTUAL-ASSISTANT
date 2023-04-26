from flet import *
import flet as ft
import time
import webbrowser
import time
import psutil
import time




def toggle_dark_mode(e):
        if page.theme_mode == "dark":
            page.theme_mode = "light"
            page.update()
        else: 
            page.theme_mode = "dark"
            page.update()

def quit(e):
        print("button clicked")

        
        pid = os.getpid()  # get the process ID of the current Python script
        os.kill(pid, signal.SIGTERM)


BG = '#1a1c1e' #041955
FWG = '#97b4ff'
FG = '#1a1c1e'##3450a1
PINK = '#eb06ff'
circle = Stack(
    controls=[
        Container(width=100,height=100,border_radius=50,bgcolor='white12'),
        Container(
            gradient=SweepGradient(
                center=alignment.center,
                start_angle=0.0, end_angle=3,stops=[0.5,0.5],colors=['#00000000', PINK],
            ),
            width=100, height=100,border_radius=50,
            content=Row(alignment='center',
                controls=[
                    Container(padding=padding.all(5),
                        bgcolor=BG,
                        width=90,height=90,
                        border_radius=50,
                        content=Container(bgcolor=FG,
                            height=80,width=80,
                            border_radius=40,
                            content=CircleAvatar(opacity=0.8,
                                foreground_image_url="https://i.ibb.co/Z6rhY9c/Avatar-Static.png")))],),),])

backgroundimg=Image(src="assets\image\on.png", fit=ImageFit.CONTAIN,
                    )





# Animation For Page5

def shrink5():
      page_5.controls[0].width = 0
      page_5.controls[0].scale = transform.Scale(
      0.8,alignment=alignment.center_right)
      page_5.controls[0].border_radius=border_radius.only(
      topLeft=35,
      topRight=0,
      bottomLeft=35,
      bottomRight=0
    )
      page_5.update()

  
def restore5():
    page_5.controls[0].width = 1315
    page_5.controls[0].border_radius = 35
    page_5.controls[0].scale = transform.Scale(

      1,alignment=alignment.bottom_center)
    page_5.update()




#For Page 5

def toggle_button_extra(e):
        # e.control.selected = not e.control.selected
        e.control.update()
        if(e.control.selected == False):
        
            shrink5()
            e.control.selected = True
            
        
        else:
            restore5()
            e.control.selected = False

# FOR PAGE 6 ABOUT.....

def toggle_button_about(e):
        # e.control.selected = not e.control.selected
        e.control.update()
        if(e.control.selected == False):
        
            shrink6()
            e.control.selected = True
            
        
        else:
            restore6()
            e.control.selected = False

def shrink6():
    page_6.controls[0].width = 0
    page_6.controls[0].scale = transform.Scale(
      0.8,alignment=alignment.center_right)
    page_6.controls[0].border_radius=border_radius.only(
      topLeft=35,
      topRight=0,
      bottomLeft=35,
      bottomRight=0
    )
    page_6.update()

  
def restore6():
    page_6.controls[0].width = 1315
    page_6.controls[0].border_radius = 35
    page_6.controls[0].scale = transform.Scale(

      1,alignment=alignment.bottom_center)
    page_6.update()        
        
        
        
        
        

def startSid(e):
      print("testin...")
      subprocess.call(["python", "sid_movie.py"])






#For Page 3

def toggle_button_settings(e):
        # e.control.selected = not e.control.selected
        e.control.update()
        if(e.control.selected == False):
        
            shrink3()
            e.control.selected = True
            
        
        else:
            restore3()
            e.control.selected = False

def shrink3():
    page_3.controls[0].width = 0
    page_3.controls[0].scale = transform.Scale(
      0.8,alignment=alignment.center_right)
    page_3.controls[0].border_radius=border_radius.only(
      topLeft=35,
      topRight=0,
      bottomLeft=35,
      bottomRight=0
    )
    page_3.update()

  
def restore3():
    page_3.controls[0].width = 1315
    page_3.controls[0].border_radius = 35
    page_3.controls[0].scale = transform.Scale(

      1,alignment=alignment.bottom_center)
    page_3.update()

page_1 = Container(
    width=1515,
    height=780,
    bgcolor=BG,###
    border_radius=35,
    padding=padding.only(left=40,top=60,right=200),
    content=Column(
        controls=[
            Container(height=20),
            circle,
            Text('Shadow',size=32,weight='bold'),
            Container(height=25),
            Row(controls=[
                ft.IconButton(ft.icons.INFO,on_click=lambda e: toggle_button_about(e)
                            ),
                Text('About ',size=15,weight=FontWeight.W_300,color='white',font_family='poppins')
            ]),
            Container(height=3),
            Row(controls=[
                ft.IconButton(ft.icons.SETTINGS,on_click=lambda e: toggle_button_settings(e)
                            ),
                Text('Settings',size=15,weight=FontWeight.W_300,color='white',font_family='poppins')
            ]),
            Container(height=3),
            Row(controls=[
                ft.IconButton(ft.icons.FEATURED_PLAY_LIST_OUTLINED,on_click=lambda e:toggle_button_extra(e)
                            ),
                Text('Extra ',size=15,weight=FontWeight.W_300,color='white',font_family='poppins')
            ]),

            Container(height=3),
            Row(controls=[
                ft.IconButton(ft.icons.POWER_SETTINGS_NEW,tooltip="Exit",icon_color=PINK,on_click=lambda e: quit(e)
                            ),         
            ]),
            Image(src="/images/2.png",width=300,height=200,),
            Text('Good',color=PINK,font_family='poppins',),
            
        ]
    )
)


content = ft.Column(
               
            [
                ft.Row(
                [
                    ft.Text("My Settings", size=30), 
                    ft.IconButton(icon=ft.icons.SETTINGS_ROUNDED, icon_size=30),

                    ], 
                alignment=ft.MainAxisAlignment.CENTER
            ),
                ft.Row(
                    [
                        ft.TextButton("Light/Dark Mode", icon=ft.icons.WB_SUNNY_OUTLINED, on_click=quit)
                    ],
                ),
                ft.Row(
                    [
                        ft.TextButton("Exit Application", icon=ft.icons.CLOSE, on_click=lambda _: page.window_close(), icon_color="red")
                    ]
                ),
            ]
        )
  


content2 = ft.Column(
               
            [
                ft.Row(
      
                [
                    ft.Text("About ", size=30), 
                    ft.IconButton(icon=ft.icons.INFO, icon_size=30),

                    ], 
                alignment=ft.MainAxisAlignment.CENTER
            ),
                # ft.Row(
                #     [
                #         ft.TextButton("Light/Dark Mode", icon=ft.icons.WB_SUNNY_OUTLINED, on_click=toggle_dark_mode)
                #     ],
                # ),
                ft.Row(
                    [
                        ft.Text(" Version: 1.77.3 (beta) \n Date:2023-04-20  \n OS: Windows_NT x64 10.0.22621",size=16,  font_family="RobotoSlab",text_align= TextAlign.JUSTIFY,no_wrap=True)
                    ],
                ),
                ft.Row(
                    [
                        ft.Text("\n\nHello, I am SHADOW, an AI designed to assist you with your needs. My core functionality is \nbased on a deep learning algorithm, specifically a neural network, which allows me to\nunderstand your requests and respond accordingly.\n\nMy neural network has been trained on a vast dataset of user inputs and their corresponding\nintents, enabling me to predict the most likely intent based on the learned patterns and\nrelationships between words and intents in the training data. The architecture and training\ndetails of my neural network may vary depending on the specific implementation, but rest\nssured that I am constantly improving and evolving to better serve you.\n\nWhether you need help with a task, have a question, or just want to chat, I am always here to lend a hand. Let's get started! ", size=25, width=1280, font_family="RobotoSlab",text_align= TextAlign.START)
                    ]
                ),
            ]
        )

 # Gif.src = "assets\image\Avatar.gif"

#BACK PAGE ANIMATION..... Engine Running....

page_4 = Row(alignment='end',
    controls=[
      Container(
        width=1315,
        height=843,
        bgcolor=BG,
        border = ft.border.all(1, ft.colors.WHITE),
        border_radius=35,

        padding=padding.only(
          top=50,left=20,
          right=20,bottom=5
            ),
          content=Row(alignment='center',
            controls=[
      Container(
          # width=640,
          # height=640,
      content=backgroundimg,
      
      
      #front.waveImg
      #Text('Settings',size=15,weight=FontWeight.W_300,color='white',font_family='poppins'),
        

      

      )
              
            ]
          )
      )
    ]
  )







# NEW page for Settings....

page_3 = Row(alignment='end',
    controls=[
      Container(
        width=0,
        height=843,
        bgcolor="#1a1c1e",
        border = ft.border.all(1, ft.colors.WHITE),
        
        border_radius=35,
        animate=animation.Animation(600,AnimationCurve.DECELERATE),
        animate_scale=animation.Animation(400, curve='decelerate'),
        padding=padding.only(
          top=50,left=20,
          right=20,bottom=5
          ),
          content=Column(
            controls=[
      content
              
            ]
          )
      )
    ]
  )




# NEW page for ABOUT US....

page_6 = Row(alignment='end',
    controls=[
      Container(
        width=0,
        height=843,
        bgcolor=FG,
        border = ft.border.all(1, ft.colors.WHITE),
        border_radius=35,
        animate=animation.Animation(600,AnimationCurve.DECELERATE),
        animate_scale=animation.Animation(400, curve='decelerate'),
        padding=padding.only(
          top=50,left=20,
          right=20,bottom=5
          ),
          content=Column(
            controls=[
     
      content2
              
            ]
          )
      )
    ]
  )


# page 5 Features.....

sidgame = ft.Stack(
        [
            ft.Image(
                src=f"assets\extragif\game.gif",
                width=300,
                height=300,
                fit=ft.ImageFit.CONTAIN,
            ),
            ft.Column(
                [
                      ft.TextButton(text="Game",on_click=lambda _:webbrowser.open("https://www.msn.com/en-in/play?ocid=winp2fp"))
                ],
                alignment=ft.MainAxisAlignment.END,
                
            ),
        ],
        width=300,
        height=300,
  )

puzzle = ft.Stack(
        [
            ft.Image(
                src=f"assets\extragif\puzzle.gif",
                width=300,
                height=300,
                fit=ft.ImageFit.CONTAIN,
            ),
            ft.Column(
                [
                    ft.TextButton(text="Tap to play",on_click=lambda _:webbrowser.open("https://www.msn.com/en-in/play/puzzle-daily/cg-9ncn1rblf8qb?ocid=winp2fp&cvid=d20c45fed2f946aca092029d54be83cd&ei=6"),
                      
                    )
                ],
                alignment=ft.MainAxisAlignment.END,
                
            ),
        ],
        width=300,
        height=300,

    )
  

card = ft.Stack(
        [
            ft.Image(
                src=f"assets\extragif\card.gif",
                width=300,
                height=300,
                fit=ft.ImageFit.CONTAIN,
            ),
            ft.Column(
                [
                    ft.TextButton(text="Tap to play",on_click=lambda _:webbrowser.open("https://www.msn.com/en-in/play/card?ocid=winp2fp&cvid=d20c45fed2f946aca092029d54be83cd&ei=6"),
                      
                    )
                ],
                alignment=ft.MainAxisAlignment.END,
                
            ),
        ],
        width=300,
        height=300,

    )
  
chess = ft.Stack(
        [
            ft.Image(
                src=f"assets\extragif\chess.gif",
                width=300,
                height=300,
                fit=ft.ImageFit.CONTAIN,
            ),
            ft.Column(
                [
                    ft.TextButton(text="Tap to play",on_click=lambda _:webbrowser.open("https://www.msn.com/en-in/play/card?ocid=winp2fp&cvid=d20c45fed2f946aca092029d54be83cd&ei=6"),
                      
                    )
                ],
                alignment=ft.MainAxisAlignment.END,
                
            ),
        ],
        width=300,
        height=300,
    )
arcade = ft.Stack(
        [
            ft.Image(
                src=f"assets\extragif\cade.gif",
                width=300,
                height=300,
                fit=ft.ImageFit.CONTAIN,
            ),
            ft.Column(
                [
                    ft.TextButton(text="Tap to play",on_click=lambda _:webbrowser.open("https://www.msn.com/en-in/play/arcade?ocid=winp2fp&cvid=d20c45fed2f946aca092029d54be83cd&ei=6"),
                      
                    )
                ],
                alignment=ft.MainAxisAlignment.END,
                
            ),
        ],
        width=300,
        height=300,
    )
  
map = ft.Stack(
        [
            ft.Image(
                src=f"assets\extragif\map.gif",
                width=300,
                height=300,
                fit=ft.ImageFit.CONTAIN,
            ),
            ft.Column(
                [
                    ft.TextButton(text="map",on_click=lambda _:webbrowser.open("https://www.msn.com/en-in/play?ocid=winp2fp"),
                      
                    )
                ],
                alignment=ft.MainAxisAlignment.END,
                
            ),
        ],
        width=300,
        height=300,
  )
athulrajweather = ft.Stack(
        [
            ft.Image(
                src=f"assets\extragif\weather.gif",
                width=300,
                height=300,
                fit=ft.ImageFit.CONTAIN,
            ),
            ft.Column(
                [
                    ft.TextButton(text="weather",on_click=lambda _:webbrowser.open("https://www.msn.com/en-in/weather/forecast/in-Sulthanbathery,Kerala?ocid=winp2fp&loc=eyJhIjoiTXVsbGFua29saSBTaGVkIFJvYWQiLCJsIjoiU3VsdGhhbmJhdGhlcnkiLCJyIjoiS2VyYWxhIiwicjIiOiJXYXlhbmFkIiwiYyI6IkluZGlhIiwiaSI6IklOIiwidCI6MTAyLCJnIjoiZW4tdXMiLCJ4IjoiNzYuMTc4MDMxOTIxMzg2NzIiLCJ5IjoiMTEuNzg5OTIyNzE0MjMzMzk4In0%3D&weadegreetype=C")
                      
                    )
                ],
                alignment=ft.MainAxisAlignment.END,
                
            ),
        ],
        width=300,
        height=300,
    )

alannews = ft.Stack(
        [
            ft.Image(
                src=f"assets\extragif\gnews.gif",
                width=300,
                height=300,
                fit=ft.ImageFit.CONTAIN,
            ),
            ft.Column(
                [
                    ft.TextButton(text="News",on_click=lambda _:webbrowser.open("https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en")
                      
                    )
                ],
                alignment=ft.MainAxisAlignment.END,
                
            ),
        ],
        width=300,
        height=300,
    )
  

movies = ft.Stack(
        [
            ft.Image(
                src=f"assets\extragif\movie.gif",
                width=300,
                height=300,
                fit=ft.ImageFit.CONTAIN,
            ),
            ft.Column(
                [
                    ft.TextButton(text="IMDB",on_click=startSid,
                    # ft.TextButton(text="IMDB",on_click=lambda _: print("Button with a custom content clicked!"),
                      
                    )
                ],
                alignment=ft.MainAxisAlignment.END,
                
            ),
        ],
        width=300,
        height=300,
    )



  #page for Extra Features.....

page_5 = Row(alignment='end',
    controls=[Container(
      #left=230,
        
        
        width=0,
        height=850,
        bgcolor=FG,
        border = ft.border.all(1, ft.colors.WHITE),
        border_radius=35,
        animate=animation.Animation(600,AnimationCurve.DECELERATE),
        animate_scale=animation.Animation(400, curve='decelerate'),
               padding=padding.only(
          top=30,left=10,
          right=20,bottom=5
          ),
        

        content=Column(
        
        controls=[
        
        Row(alignment='spaceBetween',
            controls=[
                Container(
                #GAME TITLE....
                content=TextButton("Game", icon=icons.GAMES),)],),
        Row(
        scroll="auto",
            
        controls=[  
            Container(
            expand=False,
            margin=10,
            ),sidgame,puzzle,card,chess,arcade,
            
            ] ),


            Container(height=5),
            Row(controls=[
                 Container(
      
                    # Title ara....
                
                content=TextButton("Tools \ Entertainment", icon=icons.LIGHTBULB),)]),
                Row(
        scroll="auto",
            
        controls=[  
            Container(
            expand=False,
            margin=10,
            ),movies,athulrajweather,alannews,map,
            
            ] ),

        
        ]
        )
    )])


   
        
       


BackMainContainer = Container(
    width=1515,height=783,bgcolor="#1a1c1e",
    border_radius=35,
    content=Stack(
        controls=[
            page_1,
            page_4,
        page_5,
        page_6,
        page_3,
       
        ]
    )
)
def Backside(page):
    page.theme_mode = "dark"
    page.window_frameless = True
    page.window_full_screen = True
    content5 = BackMainContainer
    return content5
