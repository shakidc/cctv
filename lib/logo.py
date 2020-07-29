from pyfiglet import Figlet


def showLogo():
    fig = Figlet()
    logo = fig.renderText('mCam')
    print(logo)
