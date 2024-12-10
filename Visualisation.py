import matplotlib.pyplot as plt

year = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
scammed_people = [195675, 235001, 240090, 301113, 311156, 322456, 300145, 435098]

plt.plot(year, scammed_people, marker="o", color="black", mec="green")
plt.title("Number of people scammed (2017 - 2024)")
plt.xlabel("Year")
plt.ylabel("Poeple")
plt.grid(True)
plt.show()