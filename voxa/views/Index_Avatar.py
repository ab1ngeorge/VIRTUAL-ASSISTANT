import flet
import flet as ft
from flet import *
import time

def stopTalk():
    avatarImage.src = "assets\image\AvatarStatic.png"
    avatarContainer.update()

def startTalk():
    print("staring to talk")
    avatarImage.src = "assets\image\Avatar.gif"
    avatarContainer.update()

def buttonClicked():
    print("clicked")
    micIcon.opacity = 0.0 if micIcon.opacity == 1.0 else 1.0
    waveImg.visible = True if waveImg.visible == False else False
    micContainer.update()

micIcon = IconButton(
    icon=ft.icons.MIC,
    icon_color="#18B2DE",
    tooltip="tap to speak",
    selected_icon=ft.icons.MIC_NONE_ROUNDED,
    icon_size=50,
    selected_icon_color="blue400",
    # on_click= buttonClicked,
    selected=False,
)

waveImg = Image(
    src="assets\image\wave.gif",
    visible=False,
)

micContents = Stack(
    controls=[
        waveImg,
        micIcon,
    ]
)


micContainer = Container(
        padding=0,
        animate=animation.Animation(1000, "bounceOut"),
        width=65,
        height=65,
        bgcolor="black",
        border_radius=30,
        content=
        micContents
    )

def promptReset():
    userPrompt.value = ''
    aiPrompt.value = ''
    userPromptContainer.offset = ft.transform.Offset(0, 0)
    userPromptContainer.opacity = 0
    userPromptContainer.update()
    aiPromptContainer.opacity = 0     
    aiPromptContainer.offset = ft.transform.Offset(0, 0)
    aiPromptContainer.update()

def promptController(userData,aidata):
        promptReset()
        userPromptContainer.offset = ft.transform.Offset(0, 0)
        userPromptContainer.opacity = 1 #if userPromptContainer.opacity == 1 else 1
        userPromptContainer.update()
        aiPromptContainer.opacity = 1 #if aiPromptContainer.opacity == 1 else 1
        aiPromptContainer.offset = ft.transform.Offset(0, 0)
        aiPromptContainer.update()
        splitDataUser = userData.split()
        lengthofDataUser = len(splitDataUser)
        splitDataAi = aidata.split()
        lengthofDataAi = len(splitDataAi)
        aiPrompt.value = ''
        if userPrompt.value == '':
            for i in range(lengthofDataUser):
                wrd = userData.split()[i]
                wrd = wrd + " "
                userPrompt.value += wrd
                userPromptContainer.update()
                time.sleep(0.07)            
        else:
            print("some bug")
        for i in range(lengthofDataAi):
                word = aidata.split()[i]
                word = word + " "
                aiPrompt.value += word
                aiPromptContainer.update()
                time.sleep(0.25)


# b = ft.TextButton("Test", on_click=promptController, data="hello")

aiPrompt = Text(" ",size=25)

# the AI prompt container where AI result text is stored 
 
aiPromptContainer = Container(
        alignment= alignment.bottom_left,
        animate_opacity=300,
        opacity=0.0,
        offset=ft.transform.Offset(-1, 0),
        animate_offset=ft.animation.Animation(2000),
        content=Container(
            border_radius=30,
            bgcolor="#18B2DE",
            padding=10,
            
            content=aiPrompt
        )

)



userPrompt = Text("",size=25,)

userPromptContainer = Container(
        alignment= alignment.bottom_right,
        animate_opacity=300,
        opacity=0.0,
        offset=ft.transform.Offset(0, 1),
        animate_offset=ft.animation.Animation(1000),
        content=Container(
            border_radius=30,
            bgcolor="#FB37FF",
            padding=10,
            content=userPrompt
        )
    )

promptContainer = Container(
    margin= margin.only(top=50),
    border= border.all(1, color="white"),
    border_radius=20,
    width=10000,
    padding=10,
    content=Column(
        controls=[
                userPromptContainer,
                aiPromptContainer,
            ]
        )
    )





def test(content):
    resultImage.src = content
    # resultContainer = resultImage
    # resultImageColumn.controls.append(resetImage)
    resultContainerAnimater.content = resultContainer #if resultContainerAnimater.content == blank else blank
    resultContainerAnimater.update()
def resetImage():
    resultContainerAnimater.content = blank
    resultContainerAnimater.update()

resultImage = Image(
    src='',
)
resultImageColumn = Column(
    alignment="center",
    controls=[
        resultImage
    ]

)

# the actual result container
resultContainer = Container(
    margin=margin.only(top = 0),
    width=850,
    height=350,
    alignment=alignment.center,
    content=resultImageColumn
)  


blank = ft.Container(
    bgcolor="white"
        )

# switches from the blank to actual result container in a animated way
resultContainerAnimater = AnimatedSwitcher(
        content= blank,
        transition= AnimatedSwitcherTransition.SCALE,
        duration=800,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
)



avatarImage = Image(
        src="assets\image\AvatarStatic.png", fit=ImageFit.CONTAIN,width=350,height=350
    )



avatarContainer = Container(
    margin=margin.only(bottom=10),      # the container which holds the avatar image
    content=avatarImage
)


topConatinerRow =Container(
        # bgcolor="white",
        content= Row(
        alignment= "center",
        controls=[                          # the container which holds both avatar and result container
            avatarContainer,
            resultContainerAnimater,
            
        ]
    ),
   
    )


mainContainer = Container(      #main container which will hold everything
     
             #GRADIENT
        # gradient=RadialGradient(
        #     center=Alignment(-0.5, -0.8),
        #     radius=3,
        #     colors=[
        #         '#33354a',
        #         '#2f3143',
        #         '#2f3143',
        #         '#292b3c',
        #         '#222331',
        #         "#222331",
        #         '#1a1a25',
        #         '#1a1b26',
        #         '#1a1b26',
        #         '#21222f',
        #         '#1d1e2a',
        #         'black',
        #     ],
        # ),
    content=Column(
    controls=[
    topConatinerRow,
    Divider(height=30, color='white5'),
    promptContainer,

    Row(
                  alignment="center",
                  controls=[
                      micContainer,
                  ]  
                ),
    
    ]
)
    
)





def Avatar(page):
    page.window_frameless = True
    page.window_full_screen = True
    content = mainContainer
    return content


