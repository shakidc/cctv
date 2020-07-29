import click
from .camThread import camThread


@click.command('rec', help="Record Video")
@click.option('-n', 'name', help="Filename", type=str, required=True)
@click.option('-c', 'cam', help="Total Camera", default=1)
@click.option('--timelapse', 'mode', is_flag=True, flag_value=120, help="Timelaspe Mode")
@click.option('--slowmotion', 'mode', is_flag=True, flag_value=10, help="Slowmotion Mode")
def rec(cam, mode, name):
    mode = mode if mode else 30
    for i in range(0, cam):
        title = "Camera " + str(i + 1)
        thread = camThread(title, i, name, mode)
    thread.start()
