import moviepy.editor as mp
import pygame


def startSplashScreen():
    # Load the video file
    clip = mp.VideoFileClip("assets/splashScreen/NewSplashScreen.mp4")
    
    pygame.display.set_caption('Shadow')
    

    # Set up the pygame mixer and load the music file
    pygame.mixer.init()
    pygame.mixer.music.load("assets\splashScreen\sund.mp3")

    # Start playing the music
    pygame.mixer.music.play()
    
    # Play the video in full screen mode with sound
    clip.preview(fullscreen=True)

    # Stop playing the music
    pygame.mixer.music.stop()
    
    # clip.preview(fullscreen=False)
    
    clip.reader.close()
    print("closed")
    
startSplashScreen()