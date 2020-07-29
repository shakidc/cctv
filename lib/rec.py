import click
from .camThread import camThread
from .logo import showLogo


@click.command('rec', help="Record Video")
@click.argument('name', required=True)
@click.option('-c', 'cam', help="Total Camera", default=1)
@click.option('--timelapse', 'mode', is_flag=True, flag_value=120, help="Timelaspe Mode")
@click.option('--slowmotion', 'mode', is_flag=True, flag_value=10, help="Slowmotion Mode")
def rec(cam, mode, name):
    showLogo()
    print("Press Esc to stop recordings...")
    mode = mode if mode else 30
    for i in range(0, cam):
        title = "Camera " + str(i + 1)
        thread = camThread(title, i, name, mode)
    thread.start()
