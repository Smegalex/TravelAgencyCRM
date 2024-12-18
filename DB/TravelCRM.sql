create table Managers(
ID number(4) GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
Name varchar2(255) NOT NULL,
Surname varchar2(255),
Email varchar2(50) NOT NULL,
AdminRights char(1)
);

create table Clients(
ID number(4) GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
Name varchar2(255) NOT NULL,
Surname varchar2(255),
Email varchar2(50) NOT NULL 
);


create table Trips(
ID number(4) GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
Name varchar2(255) NOT NULL,
IDPlace number(4) NOT NULL
);

create table Places(
ID number(4) GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
Name varchar2(255) NOT NULL,
Country varchar2(255) NOT NULL,
Coordinates varchar2(30),
Description varchar2(511)
);

create table Bookings(
ID number(4) GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
IDClient number(4) NOT NULL,
IDManager number(4) NOT NULL,
IDTrip number(4) NOT NULL,
people_amount number(3) NOT NULL
);

ALTER TABLE Trips ADD CONSTRAINT FK_Trips_Places FOREIGN KEY (IDPlace) REFERENCES Places(ID);

ALTER TABLE Bookings ADD CONSTRAINT FK_Bookings_Clients FOREIGN KEY (IDClient) REFERENCES Clients(ID);
ALTER TABLE Bookings ADD CONSTRAINT FK_Bookings_Trips FOREIGN KEY (IDTrip) REFERENCES Trips(ID);
ALTER TABLE Bookings ADD CONSTRAINT FK_Bookings_Managers FOREIGN KEY (IDManager) REFERENCES Managers(ID);

