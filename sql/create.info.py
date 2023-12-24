import sqlite3


conn = sqlite3.connect('travel_agency.db')


cursor = conn.cursor()

# Вставка данных в таблицу Customers (Клиенты)
cursor.executemany("INSERT INTO Customers (FirstName, LastName, Email) VALUES (?, ?, ?)", [
    ('John', 'Doe', 'john.doe@example.com'),
    ('Alice', 'Smith', 'alice.smith@example.com'),
    ('Michael', 'Johnson', 'michael.johnson@example.com'),
    ('Emma', 'Wilson', 'emma.wilson@example.com'),
    ('James', 'Brown', 'james.brown@example.com')
])

# Вставка данных в таблицу Tours (Туры)
cursor.executemany("INSERT INTO Tours (TourName, StartDate, EndDate, Price) VALUES (?, ?, ?, ?)", [
    ('Tour 1', '2023-09-01', '2023-09-10', 1500),
    ('Tour 2', '2023-08-15', '2023-08-25', 1200),
    ('Tour 3', '2023-07-05', '2023-07-15', 1800),
    ('Tour 4', '2023-06-20', '2023-06-30', 1600),
    ('Tour 5', '2023-05-10', '2023-05-20', 1400)
])

# Вставка данных в таблицу Hotels (Отели)
cursor.executemany("INSERT INTO Hotels (HotelName, City, Country, Rating) VALUES (?, ?, ?, ?)", [
    ('Hotel A', 'New York', 'USA', 4.5),
    ('Hotel B', 'Paris', 'France', 4.0),
    ('Hotel C', 'Rome', 'Italy', 4.2),
    ('Hotel D', 'London', 'UK', 4.4),
    ('Hotel E', 'Tokyo', 'Japan', 4.7)
])

# Вставка данных в таблицу Bookings (Бронирования)
cursor.executemany("INSERT INTO Bookings (CustomerID, TourID, BookingDate, PaymentStatus, HotelID) VALUES (?, ?, ?, ?, ?)", [
    (1, 1, '2023-08-20', 'Paid', 1),
    (2, 2, '2023-07-10', 'Paid', 2),
    (3, 3, '2023-06-25', 'Pending', 3),
    (4, 4, '2023-05-15', 'Paid', 4),
    (5, 5, '2023-04-30', 'Paid', 5)
])

# Вставка данных в таблицу Payments (Платежи)
cursor.executemany("INSERT INTO Payments (BookingID, PaymentAmount) VALUES (?, ?)", [
    (1, 1500),
    (2, 1200),
    (4, 1600),
    (5, 1400)
])

# Вставка данных в таблицу TourGuides (Гиды)
cursor.executemany("INSERT INTO TourGuides (FirstName, LastName, Email) VALUES (?, ?, ?)", [
    ('Guide 1', 'Smith', 'guide1@example.com'),
    ('Guide 2', 'Johnson', 'guide2@example.com'),
    ('Guide 3', 'Brown', 'guide3@example.com'),
    ('Guide 4', 'Wilson', 'guide4@example.com'),
    ('Guide 5', 'Davis', 'guide5@example.com')
])

# Вставка данных в таблицу TouristGroups (Группы туристов)
cursor.executemany("INSERT INTO TouristGroups (TourID, GuideID, DepartureDate) VALUES (?, ?, ?)", [
    (1, 1, '2023-09-01'),
    (2, 2, '2023-08-15'),
    (3, 3, '2023-07-05'),
    (4, 4, '2023-06-20'),
    (5, 5, '2023-05-10')
])

# Вставка данных в таблицу TouristGroupMembers (Участники группы туристов)
cursor.executemany("INSERT INTO TouristGroupMembers (GroupID, CustomerID) VALUES (?, ?)", [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
])

# Вставка данных в таблицу Excursions (Экскурсии)
cursor.executemany("INSERT INTO Excursions (ExcursionName, Price) VALUES (?, ?)", [
    ('Excursion 1', 100),
    ('Excursion 2', 80),
    ('Excursion 3', 120),
    ('Excursion 4', 90),
    ('Excursion 5', 110)
])

# Вставка данных в таблицу ExcursionBookings (Бронирования экскурсий)
cursor.executemany("INSERT INTO ExcursionBookings (CustomerID, ExcursionID, BookingDate, PaymentStatus) VALUES (?, ?, ?, ?)", [
    (1, 1, '2023-08-21', 'Paid'),
    (2, 2, '2023-07-12', 'Paid'),
    (3, 3, '2023-06-27', 'Pending'),
    (4, 4, '2023-05-17', 'Paid'),
    (5, 5, '2023-05-01', 'Paid')
])


conn.commit()
conn.close()