from weather import Weather

def main():
    while True:
        print("_"*50)
        print("Weather App")
        print("_"*50)
        print("1. Weather By City")
        print("2. Exit")
        choice = input("Select 1-2: ")

        if choice == "1":
            city = input("Enter the city name: ")
            weather = Weather()
            weather.get_weather(city)
        elif choice == "2":
            print("Exiting...!")
            break
        else:
            print("Wrong Entry Please Try again!..")

if __name__ == "__main__":
    main()