import customtkinter as ctk
import requests
from datetime import datetime


API_KEY = "de3f5e353add5a930daff787bf6958ee"

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


app = ctk.CTk()

app.title("Weather App")
app.geometry("900x650")


title_label = ctk.CTkLabel(
    app,
    text="🌤 Weather App",
    font=("Arial", 30, "bold")
)
title_label.pack(pady=20)


def update_time():

    current = datetime.now()

    date = current.strftime("%A, %d %B %Y")
    time = current.strftime("%I:%M:%S %p")

    date_label.configure(text=f"📅 {date}")
    time_label.configure(text=f"🕒 {time}")

    app.after(1000, update_time)
def search_weather():

    city = city_entry.get().strip()

    if city == "":
        city_label.configure(text="Please enter a location.")
        return

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:

        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            city_label.configure(text="Location not found!")
            return

        city_name = data["name"]
        country = data["sys"]["country"]

        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        sunrise = data["sys"]["sunrise"]
        sunset = data["sys"]["sunset"]

        wind_speed = data["wind"]["speed"] * 3.6

        weather = data["weather"][0]["description"].title()

        sunrise_time = datetime.fromtimestamp(sunrise).strftime("%I:%M %p")
        sunset_time = datetime.fromtimestamp(sunset).strftime("%I:%M %p")

        city_label.configure(
            text=f"📍 {city_name}, {country}"
        )

        temp_label.configure(
            text=f"🌡 Temperature : {temperature:.1f}°C"
        )

        feels_label.configure(
            text=f"🥵 Feels Like : {feels_like:.1f}°C"
        )

        weather_label.configure(
            text=f"🌤 Weather : {weather}"
        )

        humidity_label.configure(
            text=f"💧 Humidity : {humidity}%"
        )

        wind_label.configure(
            text=f"🌬 Wind Speed : {wind_speed:.1f} km/h"
        )

        pressure_label.configure(
            text=f"🌡 Pressure : {pressure} hPa"
        )

        sunrise_label = ctk.CTkLabel(
            app,
            text="🌅 Sunrise : --",
            font=("Arial",18)
        )
        sunrise_label.pack()

        sunset_label = ctk.CTkLabel(
            app,
            text="🌇 Sunset : --",
            font=("Arial",18)
        )
        sunset_label.pack()
        sunrise_label.configure(
            text=f"🌅 Sunrise : {sunrise_time}"
        )

        sunset_label.configure(
            text=f"🌇 Sunset : {sunset_time}"
        )
        date_label = ctk.CTkLabel(
            app,
            text="📅 Date",
            font=("Arial",18,"bold")
        )
        date_label.pack(pady=(25,5))

        time_label = ctk.CTkLabel(
            app,
            text="🕒 Time",
            font=("Arial",22,"bold")
        )
        time_label.pack()

    except Exception:
        city_label.configure(
            text="Internet Connection Error!"
        )


search_frame = ctk.CTkFrame(app)

search_frame.pack(pady=20)

city_entry = ctk.CTkEntry(
    search_frame,
    width=400,
    height=40,
    placeholder_text="Enter village, town, city or district..."
)

city_entry.pack(side="left", padx=10)

search_button = ctk.CTkButton(
    search_frame,
    text="Search",
    width=120,
    command=search_weather
)

search_button.pack(side="left")


result_label = ctk.CTkLabel(
    app,
    text="Search a location",
    font=("Arial",18),
    justify="left"
)

result_label.pack(pady=40)

city_label = ctk.CTkLabel(
    app,
    text="Search a location",
    font=("Arial",22,"bold")
)
city_label.pack(pady=20)

temp_label = ctk.CTkLabel(
    app,
    text="🌡 Temperature : --",
    font=("Arial",18)
)
temp_label.pack()

feels_label = ctk.CTkLabel(
    app,
    text="🥵 Feels Like : --",
    font=("Arial",18)
)
feels_label.pack()

weather_label = ctk.CTkLabel(
    app,
    text="🌤 Weather : --",
    font=("Arial",18)
)
weather_label.pack()

humidity_label = ctk.CTkLabel(
    app,
    text="💧 Humidity : --",
    font=("Arial",18)
)
humidity_label.pack()

wind_label = ctk.CTkLabel(
    app,
    text="🌬 Wind Speed : --",
    font=("Arial",18)
)
wind_label.pack()

pressure_label = ctk.CTkLabel(
    app,
    text="🌡 Pressure : --",
    font=("Arial",18)
)
pressure_label.pack()

date_label = ctk.CTkLabel(
    app,
    text="📅 Date",
    font=("Arial",18,"bold")
)
date_label.pack(pady=(25,5))

time_label = ctk.CTkLabel(
    app,
    text="🕒 Time",
    font=("Arial",22,"bold")
)
time_label.pack()


update_time()

app.mainloop()
