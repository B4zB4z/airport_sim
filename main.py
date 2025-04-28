from airport import Airport

def main():
    # Create an instance of Airport
    airport = Airport()
    
    # Call the simulate method on that instance
    airport.simulate(steps=30, delay=0.5)  # you can adjust steps and delay

if __name__ == "__main__":
    main()
