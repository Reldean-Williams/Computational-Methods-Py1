# Importing python libraries
import numpy as np
import random
import matplotlib.pyplot as plt
import Median_Filter as median
from scipy import signal as sc
from scipy.io import wavfile
from scipy.io.wavfile import write
from scipy.interpolate import CubicSpline
import time
from tqdm import tqdm
from playsound import playsound

# The data is being read from the Audio files
samplerate, original = wavfile.read("source_hot_fives_.wav")
samplerate, degraded = wavfile.read("deg_.wav")

# A single channel is used
original1 = original[:, 1]
degraded1 = degraded[:, 1]

# An Array is being created of detect for position of clicks
detect = np.zeros(len(degraded1))

Threshold = 32000
for i in range(len(degraded1)):
    if (degraded1[i] >= Threshold):
        detect[i] = 1

for i in range(len(degraded1)):
    if (degraded1[i] <= (Threshold * -1)):
        detect[i] = 1

# Plotting the original, degraded and detected clicks
figure, axs = plt.subplots(3, 1)
axs[0].plot(original1)
axs[0].set_title('Original Audio')
axs[1].plot(degraded1)
axs[1].set_title('Degraded Audio')
axs[2].plot(detect)
axs[2].set_title('Clicks')

start = time.time()

click_index = np.where(detect == 1)

data_new = degraded1
sorted_data = np.arange(len(data_new))


x_data = np.delete(sorted_data, click_index)
y_data = np.delete(data_new, click_index)


for i in tqdm(range(0, 100)):
    restored = CubicSpline(x_data, y_data)
    time.sleep(0.1)

for i in range(len(click_index)):
    data_new[click_index[i]] = restored(click_index)[i]

stop = time.time()

print(" Execution time for Cubic Spline : ", format(stop - start))

MSE = np.square(np.subtract(original1, data_new)).mean()
print(" MSE ", abs(MSE))

samplerate, degraded_new = wavfile.read("deg_.wav")
deg_data = degraded_new[:, 1]

# Plotting the original, degraded and restored audio data
figure, axs = plt.subplots(3, 1)
axs[0].plot(original1)
axs[0].set_title('Original Audio')
axs[1].plot(deg_data)
axs[1].set_title('Degraded Audio')
axs[2].plot(data_new)
axs[2].set_title('Restored Audio Cubic Spline')

for ax in axs.flat:
    ax.label_outer()

plt.show()

# Writing the restored data to create an output audio file
res_data1 = np.array(data_new)
write("output_cubic_spline.wav", samplerate, res_data1.astype(np.int16))
playsound("output_cubic_spline.wav")