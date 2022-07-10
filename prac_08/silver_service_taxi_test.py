from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Hummer", 100, 1)
    taxi.drive(100)
    print(taxi)
    print(taxi.get_fare())
    taxi.drive(60)
    print(taxi)
    print(taxi.get_fare())

main()