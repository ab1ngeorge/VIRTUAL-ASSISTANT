from flet import *
import flet as ft
from threading import Thread
import psutil
import time

def NavBar(page):
    percentage_battery = Text("", size=13, weight="bold")
    status_battery = Text("")




    def toggle_icon_button(e):
        #e.control.selected = not e.control.selected

        if(e.control.selected == False):
            page.go('/backside')
            e.control.selected = not e.control.selected
            e.control.selected = True
            e.control.update()

        else:
             page.go('/')
            
             e.control.selected = False
             e.control.update()

    def get_battery_status():
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = battery.percent
        return (plugged, percent)

    def check_every_seconds():
        prev_status = None
        while True:
            battery_status = get_battery_status()
            if prev_status != battery_status[0]:
                if battery_status[0]:
                    print(f"Your battery is plugged, percentage: {battery_status[1]} %")
                    mystatus.bgcolor = "green"
                    mystatus.tooltip = "Charging"
                    percentage_battery.value = "{} %".format(int(battery_status[1]))
                    page.overlay.append(constatus)
                    page.update()
                elif battery_status[1] < 20:
                    mystatus.bgcolor = "red"
                    mystatus.tooltip = "Please Charge"
                    percentage_battery.value = "{} %".format(int(battery_status[1]))
                    page.overlay.append(constatus)
                    page.update()
                elif battery_status[1] > 99:
                    mystatus.bgcolor = "orange"
                    mystatus.tooltip = "Full Charged"
                    percentage_battery.value = "{} %".format(int(battery_status[1]))
                    page.overlay.append(constatus)
                    page.update()
                else:
                    print(f"Your battery is NOT CHARGING, percentage: {battery_status[1]} %")
                    mystatus.bgcolor = "blue"
                    mystatus.tooltip = "Not Charging"
                    percentage_battery.value = "{} %".format(int(battery_status[1]))
                    page.overlay.append(constatus)
                    page.update()
                prev_status = battery_status[0]
            time.sleep(1)

    def quit(e):
        page.window_destroy()
        pid = os.getpid()  # get the process ID of the current Python script
        os.kill(pid, signal.SIGTERM)

    mystatus = Container(
        bgcolor="red",
        width=60,
        height=30,
        tooltip=status_battery.value,
        border_radius=30,
        margin=margin.only(top=12, left=0, right=0, bottom=0),
        alignment=alignment.center,
        padding=5,
        content=Column([percentage_battery])
    )

    constatus = Container(
        tooltip="",
        content=Column([mystatus])
    )

    NavBar2 = ft.AppBar(
        leading=ft.IconButton(ft.icons.MENU, selected_icon=ft.icons.HOME,
            on_click=toggle_icon_button,
            selected=False,
           ),
        
        
        leading_width=40,
        title=ft.Text("SHADOW"),
        
        center_title=False,
        actions=[
           
            #ft.IconButton(ft.icons.HOME, on_click=lambda _: page.go('/')),
            constatus,
            
            ft.IconButton(ft.icons.INFO_OUTLINED, on_click=lambda _: page.go('/about')),
            
            ft.IconButton(ft.icons.SETTINGS_ROUNDED, on_click=lambda _: page.go('/settings')),
            
            ft.IconButton(ft.icons.CLOSE, on_click=quit)
        ]
    )

    # start the battery status checking loop in a separate thread
    Thread(target=check_every_seconds).start()

    content = NavBar2
    return content
