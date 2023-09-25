import sqlite3


conn = sqlite3.connect('travel_agency.db')

# Создание курсора для выполнения SQL-запросов
cursor = conn.cursor()

# Создание таблицы Customers (Клиенты)
cursor.execute('''CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INTEGER PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT,
    Email TEXT
)''')

# Создание таблицы Tours (Туры)
cursor.execute('''CREATE TABLE IF NOT EXISTS Tours (
    TourID INTEGER PRIMARY KEY,
    TourName TEXT,
    StartDate DATE,
    EndDate DATE,
    Price INTEGER
)''')

# Создание таблицы Hotels (Отели)
cursor.execute('''CREATE TABLE IF NOT EXISTS Hotels (
    HotelID INTEGER PRIMARY KEY,
    HotelName TEXT,
    City TEXT,
    Country TEXT,
    Rating REAL
)''')

# Создание таблицы Bookings (Бронирования)
cursor.execute('''CREATE TABLE IF NOT EXISTS Bookings (
    BookingID INTEGER PRIMARY KEY,
    CustomerID INTEGER,
    TourID INTEGER,
    BookingDate DATE,
    PaymentStatus TEXT,
    HotelID INTEGER,
    FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID),
    FOREIGN KEY (TourID) REFERENCES Tours (TourID),
    FOREIGN KEY (HotelID) REFERENCES Hotels (HotelID)
)''')

# Создание таблицы Payments (Платежи)
cursor.execute('''CREATE TABLE IF NOT EXISTS Payments (
    PaymentID INTEGER PRIMARY KEY,
    BookingID INTEGER,
    PaymentAmount INTEGER,
    FOREIGN KEY (BookingID) REFERENCES Bookings (BookingID)
)''')

# Создание таблицы TourGuides (Гиды)
cursor.execute('''CREATE TABLE IF NOT EXISTS TourGuides (
    GuideID INTEGER PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT,
    Email TEXT
)''')

# Создание таблицы TouristGroups (Группы туристов)
cursor.execute('''CREATE TABLE IF NOT EXISTS TouristGroups (
    GroupID INTEGER PRIMARY KEY,
    TourID INTEGER,
    GuideID INTEGER,
    DepartureDate DATE,
    FOREIGN KEY (TourID) REFERENCES Tours (TourID),
    FOREIGN KEY (GuideID) REFERENCES TourGuides (GuideID)
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
    ExcursionName TEXT,
    Price INTEGER
)''')

# Создание таблицы ExcursionBookings (Бронирования экскурсий)
cursor.execute('''CREATE TABLE IF NOT EXISTS ExcursionBookings (
    BookingID INTEGER PRIMARY KEY,
    CustomerID INTEGER,
    ExcursionID INTEGER,
    BookingDate DATE,
    PaymentStatus TEXT,
    FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID),
    FOREIGN KEY (ExcursionID) REFERENCES Excursions (ExcursionID)
)''')

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
