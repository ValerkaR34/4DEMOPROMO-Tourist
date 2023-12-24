CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INTEGER PRIMARY KEY,
    FirstName VARCHAR,
    LastName VARCHAR,
    Email VARCHAR
);

CREATE TABLE IF NOT EXISTS Tours (
    TourID INTEGER PRIMARY KEY,
    TourName VARCHAR,
    StartDate DATE,
    EndDate DATE,
    Price INTEGER
);

CREATE TABLE IF NOT EXISTS Hotels (
    HotelID INTEGER PRIMARY KEY,
    HotelName VARCHAR,
    City VARCHAR,
    Country VARCHAR,
    Rating REAL
);

CREATE TABLE IF NOT EXISTS Bookings (
    BookingID INTEGER PRIMARY KEY,
    CustomerID INTEGER,
    TourID INTEGER,
    BookingDate DATE,
    PaymentStatus VARCHAR,
    HotelID INTEGER,
    FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (TourID) REFERENCES Tours (TourID) ON DELETE CASCADE,
    FOREIGN KEY (HotelID) REFERENCES Hotels (HotelID) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Payments (
    PaymentID INTEGER PRIMARY KEY,
    BookingID INTEGER,
    PaymentAmount INTEGER,
    FOREIGN KEY (BookingID) REFERENCES Bookings (BookingID) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS TourGuides (
    GuideID INTEGER PRIMARY KEY,
    FirstName VARCHAR,
    LastName VARCHAR,
    Email VARCHAR
);

CREATE TABLE IF NOT EXISTS TouristGroups (
    GroupID INTEGER PRIMARY KEY,
    TourID INTEGER,
    GuideID INTEGER,
    DepartureDate DATE,
    FOREIGN KEY (TourID) REFERENCES Tours (TourID) ON DELETE CASCADE,
    FOREIGN KEY (GuideID) REFERENCES TourGuides (GuideID) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS TouristGroupMembers (
    MemberID INTEGER PRIMARY KEY,
    GroupID INTEGER,
    CustomerID INTEGER,
    FOREIGN KEY (GroupID) REFERENCES TouristGroups (GroupID),
    FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID)
);

CREATE TABLE IF NOT EXISTS Excursions (
    ExcursionID INTEGER PRIMARY KEY,
    ExcursionName VARCHAR,
    Price INTEGER
);

CREATE TABLE IF NOT EXISTS ExcursionBookings (
    BookingID INTEGER PRIMARY KEY,
    CustomerID INTEGER,
    ExcursionID INTEGER,
    BookingDate DATE,
    PaymentStatus VARCHAR,
    FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (ExcursionID) REFERENCES Excursions (ExcursionID) ON DELETE CASCADE
);
