import subprocess


def convert():
    input_file = 'voice.ogg'

    wavefile = input_file[:-4] + '.wav'
    command_wav = ['ffmpeg', '-i', input_file, '-vn', wavefile]
    process = subprocess.Popen(args=command_wav, stdout=subprocess.PIPE)
    process.wait()
    return wavefile

def remove():
    pr = subprocess.Popen(args=['rm', 'voice.ogg'], stdout=subprocess.PIPE)
    pr.wait()
    pr = subprocess.Popen(args=['rm', 'voice.wav'], stdout=subprocess.PIPE)
    pr.wait()