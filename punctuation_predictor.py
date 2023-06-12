import subprocess


def write_to_file(transcript):
    text_file = open("./input.txt", "w")
    text_file.write(transcript)
    text_file.close()


def predict_ru(transcript):
    write_to_file(transcript)
    com = ['python3', 'example.py', './input.txt']
    process = subprocess.Popen(args=com, stdout=subprocess.PIPE)
    process.wait()
    output = process.stdout.read().decode('utf-8')
    rm = subprocess.Popen(args=['rm', './input.txt'])
    rm.wait()
    return output



