from collections import deque

portions = [int(el) for el in input().split(", ")]
stamina = deque([int(el) for el in input().split(", ")])

peaks = {
    "Vihren": 80,
    "Kutelo": 90,
    "Banski Suhodol": 100,
    "Polezhan": 60,
    "Kamenitza": 70
}

conquered_peaks = []

for _ in range(7):

    last_portion = portions.pop()
    first_stamina = stamina.popleft()

    total_sum = last_portion + first_stamina

    for peak, height in peaks.items():
        if total_sum >= height:
            conquered_peaks.append(peak)
            del peaks[peak]
            break
        else:
            break


if len(conquered_peaks) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    print("\n".join(conquered_peaks))