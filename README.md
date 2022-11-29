## Project Title
Audio Restoration in Python

## Project Description

In this assignment I implemented different interpolation methods, namely median filtering and cubic splines to restore the audio. For the restoration of audio signals, an adaptive median filtering technique based on predictions is suggested. The stages of this approach include prediction, detection, and adaptive median filtering. In comparison to weighted median filters, recursive weighted median filters, adaptive median filters and model-based approaches. The suggested algorithm is effective at detecting and suppressing degradations in audio signals.

There are two main categories of degradations that are frequently used in audio signal processing: localized degradations and global degradations. Localized degradations, such as clicks, crackles, scratches, and clips, are waveform discontinuities that only impact specific samples. Global degradations include background impulse noise and specific kinds of non-linear distortions, and they have an impact on all waveform samples. Clicks are categorized as finite duration flaws that appear at random locations in the waveform. They might appear as a result of minute dust and dirt particles getting stuck in the grooves of a phonograph disc, granularity in the material used to press such a disc, or tiny surface scratches [1].

Median filtering is a traditional method for interpolating corrupted or missing samples in speech and audio signals, but it is too basic to handle gaps more than a few samples [2]. Since the filtering is done evenly throughout the entire signal, uncorrupted samples are often modified by median filters and other order statistic filters [3] that work on a localized area. A median filter will, however, stop changes in the input signal that are shorter in time than the filter window. A large median window is required when the signal is highly corrupted by impulsive noise, which results in more uncorrupted samples being replaced by the window's median value and more high frequency components being eliminated by the filter.

The cubic spline method involves fitting a succession of distinctive cubic polynomials between each data point, with the requirement that the resulting curve be continuous and look smooth. The rates of change and total change over an interval can then be calculated using these cubic splines. Finding a curve that connects data points with a degree of three or less is possible through the use of cubic spline interpolation. Splines are polynomials that have continuous first and second derivatives and are smooth and continuous across a specified plot.

---

## Installation and Execution

Provide details on the Python version and libraries (e.g. numpy version) you are using. One easy way to do it is to do that automatically:
```sh                                 
pip3 install pipreqs

pipreqs $project/path/requirements.txt
```
For more details check [here](https://github.com/bndr/pipreqs)


Afer installing all required packages you can run the demo file simply by typing:
```sh
python demo_audio_restoration.py
```
---

## Methodology and Results
Describe here how you have designed your code, e.g. a main script/routine that calls different functions, is the unittesting included in the main routine? 

In order to significantly reduce noise in an audio, the median filter is a non-linear ordered statistic digital filtering approach and is one of the better windowing operators. When working with lengthy audio recordings, it is typically not a good idea to operate on the complete signal without any pre-processing. This frequently results in the production of fresh audio artifacts. More significantly, segmenting the signal makes it much easier to find corrupted audio when it comes to burst detection. Padding is one of the common audio processing processes used by the burst rectification technique.

The qubic spline is a function of Si(x) as denoted below:
Si(x) = ai + bi · (x − xi) + ci · (x − xi)2 + di · (x − xi)3


**Results**

1. For the median filter, different lengths were explored to test the effectiveness of the restoration. The original and degraded data for an audio titled source_hot_fives_ is shown in the figures below.

In particular, XXXX were tested and XXX was observed to deliver the lowest MSE, as shown in the figure below.

<img src="Original Audio.png" width="350">
<img src="Degraded Audio.png" width="350">


The restored waveform <output_medianFilter.wav> with the optimal filter length is given below:



2. Observations drawn from the cubic splines is that the MSE is lower and the execution time is 15 seconds.
Using the cubic splines, we observe ....

The restored waveform <output_cubicSplines.wav> with the optimal filter length is given below:


3. Comparing the median filter and cubic splines interpolation methods, I notice that the cubic splines method achieves a lower MSE. The runtime of XX method is .....

After listening to the two restored files, we notice ...


---
## Credits

This code was developed for purely academic purposes by Reldean Williams (github profile name - Reldean-Williams). 

## Resources:

[1] S. J. Godsill, P. J. W. Rayner, and O. Capp'e. "Digital Audio Restoration". In K. Brandenburg and M. Kahrs, editors, Applications of Digital Signal Processing to Audio and Acoustics. Kluwer Academic Publishers, 1996.
[2] L. Lu, S. Li, L. Wenyin, H. J. Zhang and Y. Mao. "Audio textures". Proc. of ICASSP2002, Vol. II, pp. 1761-1764, 2002.
[3] Charu Chandra, Michael S. Moore and Sanjit K. Mitra "An efficient method for the removal of impulse noise from speech an audio signals" Dept. of Electrical and computer Engineering University of California, Santa Barbara Santa Barbara, CA 93106-9560




