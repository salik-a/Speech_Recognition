import pyaudio
import wave
from python_speech_features import mfcc
import sys
import numpy as np

np.set_printoptions(threshold=sys.maxsize)
import scipy.io.wavfile as wav
import math


def dtw(mfcc1, mfcc2):
    if (len(mfcc1) <= len(mfcc2)):
        live_sound = np.array(mfcc1)
        recorded_sound = np.array(mfcc2)
    elif (len(mfcc1) > len(mfcc2)):
        live_sound = np.array(mfcc2)
        recorded_sound = np.array(mfcc1)
    table = np.array(np.zeros((len(live_sound), len(recorded_sound))))

    table_distance = 0;
    sum = 0;
    x = 1

    for i in range(len(recorded_sound)):
        table_distance = 0;
        for j in range(len(recorded_sound[0])):
            table_distance = (live_sound[0][j] - recorded_sound[i][j]) * (live_sound[0][j] - recorded_sound[i][j])
            table[0][i] = table[0][i] + table_distance
    table_distance = 0

    for i in range(1, len(live_sound)):
        table_distance = 0;
        for j in range(len(recorded_sound[0])):
            table_distance = (live_sound[i][j] - recorded_sound[0][j]) * (live_sound[i][j] - recorded_sound[0][j])
            table[i][0] = table[i][0] + table_distance

    for i in range(1, len(recorded_sound)):
        table[0][i] = table[0][i] + table[0][i - 1]
    for i in range(1, len(live_sound)):
        table[i][0] = table[i][0] + table[i - 1][0]

    while (x <= len(table) - 1):
        for i in range(x, len(recorded_sound)):
            table_distance = 0;
            for j in range(0, len(recorded_sound[0])):
                table_distance = (live_sound[x][j] - recorded_sound[i][j]) * (live_sound[x][j] - recorded_sound[i][j])
                table[x][i] = table[x][i] + table_distance

        table_distance = 0
        for i in range(x + 1, len(live_sound)):
            table_distance = 0;
            for j in range(0, len(recorded_sound[0])):
                table_distance = (live_sound[i][j] - recorded_sound[x][j]) * (live_sound[i][j] - recorded_sound[x][j])
                table[i][x] = table[i][x] + table_distance

        for i in range(x, len(recorded_sound)):
            if table[x][i - 1] <= table[x - 1][i] and table[x][i - 1] <= table[x - 1][i - 1]:
                table[x][i] = table[x][i] + table[x][i - 1]
            elif table[x - 1][i - 1] <= table[x - 1][i] and table[x - 1][i - 1] <= table[x][i - 1]:
                table[x][i] = table[x][i] + table[x - 1][i - 1]
            elif table[x - 1][i] <= table[x - 1][i - 1] and table[x - 1][i] <= table[x][i - 1]:
                table[x][i] = table[x][i] + table[x - 1][i]
        for i in range(x + 1, len(live_sound)):
            if table[i - 1][x] <= table[i][x - 1] and table[i - 1][x] <= table[i - 1][x - 1]:
                table[i][x] = table[i][x] + table[i - 1][x]
            elif table[i - 1][x - 1] <= table[i][x - 1] and table[i - 1][x - 1] <= table[i - 1][x]:
                table[i][x] = table[i][x] + table[i - 1][x - 1]
            elif table[i][x - 1] <= table[i - 1][x - 1] and table[i][x - 1] <= table[i - 1][x]:
                table[i][x] = table[i][x] + table[i][x - 1]

        x = x + 1;



    for i in range(0, len(table)):
        for j in range(0, len(table[0])):
            table[i][j] = math.sqrt(table[i][j])



    return table[len(table)-1][len(table[0])-1]


CHUNK = 16000
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 4
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

(RATE, sig) = wav.read("C:/Users/LENOVO/PycharmProjects/untitled4/output.wav")
mfcc_output = mfcc(sig, RATE)

(RATE, sig) = wav.read("C:/Users/LENOVO/Desktop/yeni1/Jarvis_template.wav")
mfcc_Jarvis = mfcc(sig, RATE)

(RATE, sig) = wav.read("C:/Users/LENOVO/Desktop/yeni1/Tofftl_template.wav")
mfcc_Tofftl = mfcc(sig, RATE)

(RATE, sig) = wav.read("C:/Users/LENOVO/Desktop/yeni1/Tontl_template.wav")
mfcc_Tontl = mfcc(sig, RATE)

(RATE, sig) = wav.read("C:/Users/LENOVO/Desktop/yeni1/Tontt_template.wav")
mfcc_Tontt = mfcc(sig, RATE)

(RATE, sig) = wav.read("C:/Users/LENOVO/Desktop/yeni1/Ttat_template.wav")
mfcc_Ttat = mfcc(sig, RATE)

(RATE, sig) = wav.read("C:/Users/LENOVO/Desktop/yeni1/Jarvish_template.wav")
mfcc_Jarvish = mfcc(sig, RATE)

(RATE, sig) = wav.read("C:/Users/LENOVO/Desktop/yeni1/Tofftlh_template.wav")
mfcc_Tofftlh = mfcc(sig, RATE)

(RATE, sig) = wav.read("C:/Users/LENOVO/Desktop/yeni1/Tontlh_template.wav")
mfcc_Tontlh = mfcc(sig, RATE)

(RATE, sig) = wav.read("C:/Users/LENOVO/Desktop/yeni1/Tontth_template.wav")
mfcc_Tontth = mfcc(sig, RATE)

(RATE, sig) = wav.read("C:/Users/LENOVO/Desktop/yeni1/Ttath_template.wav")
mfcc_Ttath = mfcc(sig, RATE)

(RATE, sig) = wav.read("C:/Users/LENOVO/Desktop/yeni1/Jarvisu_template.wav")
mfcc_Jarvisu = mfcc(sig, RATE)

(RATE, sig) = wav.read("C:/Users/LENOVO/Desktop/yeni1/Tofftlu_template.wav")
mfcc_Tofftlu = mfcc(sig, RATE)

(RATE, sig) = wav.read("C:/Users/LENOVO/Desktop/yeni1/Tontlu_template.wav")
mfcc_Tontlu = mfcc(sig, RATE)

(RATE, sig) = wav.read("C:/Users/LENOVO/Desktop/yeni1/Tonttu_template.wav")
mfcc_Tonttu = mfcc(sig, RATE)

(RATE, sig) = wav.read("C:/Users/LENOVO/Desktop/yeni1/Ttatu_template.wav")
mfcc_Ttatu = mfcc(sig, RATE)

(RATE, sig) = wav.read("C:/Users/LENOVO/Desktop/yeni1/Jarvisd_template.wav")
mfcc_Jarvisd = mfcc(sig, RATE)

(RATE, sig) = wav.read("C:/Users/LENOVO/Desktop/yeni1/Tofftld_template.wav")
mfcc_Tofftld = mfcc(sig, RATE)

(RATE, sig) = wav.read("C:/Users/LENOVO/Desktop/yeni1/Tontld_template.wav")
mfcc_Tontld = mfcc(sig, RATE)

(RATE, sig) = wav.read("C:/Users/LENOVO/Desktop/yeni1/Tonttd_template.wav")
mfcc_Tonttd = mfcc(sig, RATE)

(RATE, sig) = wav.read("C:/Users/LENOVO/Desktop/yeni1/Ttatd_template.wav")
mfcc_Ttatd = mfcc(sig, RATE)

(RATE, sig) = wav.read("C:/Users/LENOVO/Desktop/yeni1/Jarvise_template.wav")
mfcc_Jarvise = mfcc(sig, RATE)

(RATE, sig) = wav.read("C:/Users/LENOVO/Desktop/yeni1/Tofftle_template.wav")
mfcc_Tofftle = mfcc(sig, RATE)

(RATE, sig) = wav.read("C:/Users/LENOVO/Desktop/yeni1/Tontle_template.wav")
mfcc_Tontle = mfcc(sig, RATE)

(RATE, sig) = wav.read("C:/Users/LENOVO/Desktop/yeni1/Tontte_template.wav")
mfcc_Tontte = mfcc(sig, RATE)

(RATE, sig) = wav.read("C:/Users/LENOVO/Desktop/yeni1/Ttate_template.wav")
mfcc_Ttate = mfcc(sig, RATE)



dtwlist=[]
Jarvis=dtw(mfcc_output, mfcc_Jarvis)
Tofftl=dtw(mfcc_output, mfcc_Tofftl)
Tontl=dtw(mfcc_output, mfcc_Tontl)
Tontt=dtw(mfcc_output, mfcc_Tontt)
Ttat=dtw(mfcc_output, mfcc_Ttat)
Jarvish=dtw(mfcc_output, mfcc_Jarvish)
Tofftlh=dtw(mfcc_output, mfcc_Tofftlh)
Tontlh=dtw(mfcc_output, mfcc_Tontlh)
Tontth=dtw(mfcc_output, mfcc_Tontth)
Ttath=dtw(mfcc_output, mfcc_Ttath)
Jarvisu=dtw(mfcc_output, mfcc_Jarvisu)
Tofftlu=dtw(mfcc_output, mfcc_Tofftlu)
Tontlu=dtw(mfcc_output, mfcc_Tontlu)
Tonttu=dtw(mfcc_output, mfcc_Tonttu)
Ttatu=dtw(mfcc_output, mfcc_Ttatu)
Jarvisd=dtw(mfcc_output, mfcc_Jarvisd)
Tofftld=dtw(mfcc_output, mfcc_Tofftld)
Tontld=dtw(mfcc_output, mfcc_Tontld)
Tonttd=dtw(mfcc_output, mfcc_Tonttd)
Ttatd=dtw(mfcc_output, mfcc_Ttatd)
Jarvise=dtw(mfcc_output, mfcc_Jarvise)
Tofftle=dtw(mfcc_output, mfcc_Tofftle)
Tontle=dtw(mfcc_output, mfcc_Tontle)
Tontte=dtw(mfcc_output, mfcc_Tontte)
Ttate=dtw(mfcc_output, mfcc_Ttate)



dtwlist.append(Jarvis)
dtwlist.append(Tofftl)
dtwlist.append(Tontl)
dtwlist.append(Tontt)
dtwlist.append(Ttat)
dtwlist.append(Jarvish)
dtwlist.append(Tofftlh)
dtwlist.append(Tontlh)
dtwlist.append(Tontth)
dtwlist.append(Ttath)
dtwlist.append(Jarvisu)
dtwlist.append(Tofftlu)
dtwlist.append(Tontlu)
dtwlist.append(Tonttu)
dtwlist.append(Ttatu)
dtwlist.append(Jarvisd)
dtwlist.append(Tofftld)
dtwlist.append(Tontld)
dtwlist.append(Tonttd)
dtwlist.append(Ttatd)
dtwlist.append(Jarvise)
dtwlist.append(Tofftle)
dtwlist.append(Tontle)
dtwlist.append(Tontte)
dtwlist.append(Ttate)


print dtwlist
print min(dtwlist)
print


closest=min(dtwlist)
if (closest==Jarvis or closest==Jarvish or closest==Jarvisu or closest==Jarvisd or closest==Jarvise):
    print("Yes sir")
elif (closest==Tofftl or closest==Tofftlh or closest==Tofftlu or closest==Tofftld or closest==Tofftle):
    print("Lights off")
elif (closest==Tontl or closest==Tontlh or closest==Tontlu or closest==Tontld or closest==Tontle):
    print("Lights on")
elif (closest==Tontt or closest==Tontth or closest==Tonttu or closest==Tonttd or closest==Tontte):
    print("Tv is on")
elif (closest==Ttat or closest==Ttath or closest==Ttatu or closest==Ttatd or closest==Ttate):
    print("Air Temperature is 30 Degree")