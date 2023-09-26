import sqlite3


conn = sqlite3.connect('travel_agency.db')


cursor = conn.cursor()

# Создание таблицы Customers (Клиенты)
cursor.execute('''CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INTEGER PRIMARY KEY,
    FirstName VARCHAR,
    LastName VARCHAR,
    Email VARCHAR
)''')

# Создание таблицы Tours (Туры)
cursor.execute('''CREATE TABLE IF NOT EXISTS Tours (
    TourID INTEGER PRIMARY KEY,
    TourName VARCHAR,
    StartDate DATE,
    EndDate DATE,
    Price INTEGER
)''')

# Создание таблицы Hotels (Отели)
cursor.execute('''CREATE TABLE IF NOT EXISTS Hotels (
    HotelID INTEGER PRIMARY KEY,
    HotelName VARCHAR,
    City VARCHAR,
    Country VARCHAR,
    Rating REAL
)''')

# Создание таблицы Bookings (Бронирования)
cursor.execute('''CREATE TABLE IF NOT EXISTS Bookings (
    BookingID INTEGER PRIMARY KEY,
    CustomerID INTEGER,
    TourID INTEGER,
    BookingDate DATE,
    PaymentStatus VARCHAR,
    HotelID INTEGER,
    FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (TourID) REFERENCES Tours (TourID) ON DELETE CASCADE,
    FOREIGN KEY (HotelID) REFERENCES Hotels (HotelID) ON DELETE CASCADE
)''')

# Создание таблицы Payments (Платежи)
cursor.execute('''CREATE TABLE IF NOT EXISTS Payments (
    PaymentID INTEGER PRIMARY KEY,
    BookingID INTEGER,
    PaymentAmount INTEGER,
    FOREIGN KEY (BookingID) REFERENCES Bookings (BookingID) ON DELETE CASCADE
)''')

# Создание таблицы TourGuides (Гиды)
cursor.execute('''CREATE TABLE IF NOT EXISTS TourGuides (
    GuideID INTEGER PRIMARY KEY,
    FirstName VARCHAR,
    LastName VARCHAR,
    Email VARCHAR
)''')

# Создание таблицы TouristGroups (Группы туристов)
cursor.execute('''CREATE TABLE IF NOT EXISTS TouristGroups (
    GroupID INTEGER PRIMARY KEY,
    TourID INTEGER,
    GuideID INTEGER,
    DepartureDate DATE,
    FOREIGN KEY (TourID) REFERENCES Tours (TourID) ON DELETE CASCADE,
    FOREIGN KEY (GuideID) REFERENCES TourGuides (GuideID) ON DELETE CASCADE
)''')

# Создание таблицы TouristGroupMembers (Участники группы туристов)
cursor.execute('''CREATE TABLE IF NOT EXISTS TouristGroupMembers (
    MemberID INTEGER PRIMARY KEY,
    GroupID INTEGER,
    CustomerID INTEGER,
    FOREIGN KEY (GroupID) REFERENCES TouristGroups (GroupID),
    FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID)
)''')

# Создание таблицы Excursions (Экскурсии)
cursor.execute('''CREATE TABLE IF NOT EXISTS Excursions (
    ExcursionID INTEGER PRIMARY KEY,
    ExcursionName VARCHAR,
    Price INTEGER
)''')

# Создание таблицы ExcursionBookings (Бронирования экскурсий)
cursor.execute('''CREATE TABLE IF NOT EXISTS ExcursionBookings (
    BookingID INTEGER PRIMARY KEY,
    CustomerID INTEGER,
    ExcursionID INTEGER,
    BookingDate DATE,
    PaymentStatus VARCHAR,
    FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (ExcursionID) REFERENCES Excursions (ExcursionID) ON DELETE CASCADE
)''')

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
