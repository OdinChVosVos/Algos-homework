from HotelGuests_6.Hotel import Hotel

guests = [
    ("2024-09-15", "2024-10-20"),
    ("2024-10-14", "2024-10-21"),
    ("2024-09-15", "2024-09-16"),
    ("2024-10-14", "2024-10-22"),
    ("2024-10-14", "2024-10-14"),
    ("2024-09-14", "2024-10-21"),
    ("2024-09-15", "2024-09-15"),
    ("2024-11-14", "2024-11-21")
]

hotel = Hotel()
[hotel.book_dates(guest[0], guest[1]) for guest in guests]

result = hotel.get_max_visitors_day()
print(f"Day with the maximum number of visitors: {result[0]} ({result[1]} visitors)")