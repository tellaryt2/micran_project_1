import numpy as np
import matplotlib.pyplot as plt

def signals():
    N = 4096
    fs = 100e6
    f_signal = 20e6

    t = np.arange(N) / fs

    # Угловая частота
    w = 2 * np.pi * f_signal

    # Массивы синуса и косинуса
    sin_signal = np.sin(w * t)
    cos_signal = np.cos(w * t)

    # Массив комплексных чисел
    complex_signal = cos_signal + 1j * sin_signal

    # Преобразование Фурье (для спектра)
    fft_result = np.fft.fft(complex_signal)

    # Частотная шкала
    freqs = np.fft.fftfreq(N, 1 / fs)

    # Амплитудный спектр
    amplitude_spectrum = np.abs(fft_result) / N * 2

    # Амплитуда в дБм
    power_spectrum_dBm = 10 * np.log10(amplitude_spectrum ** 2)

    plt.figure(figsize=(10, 6))

    # Положительные частоты
    positive_freqs = freqs[:N // 2]
    positive_power_spectrum_dBm = power_spectrum_dBm[:N // 2]

    plt.plot(positive_freqs / 1e6, positive_power_spectrum_dBm, label='Спектр',
             color='blue')  # Частоты в МГц

    plt.xlabel('Частота, МГц')
    plt.ylabel('Мощность, дБм')

    plt.grid(True)
    plt.legend()

    plt.title('Спектр комплексного сигнала')

    plt.show()