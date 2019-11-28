# Class Diagram

```
Employee
    |
    --Pilot

Voyage
    |
    2->Flight
    |
    2->Pilot
    |
    +->Employee

Flight
    |
    1->Destination
    |
    1->Airplane

```

## Attributes
Employee: Name License Ssn Address Landline Mobile Email  
Pilot: License  
Voyage: OutFlight ReturnFlight FlightCaptain FlightAssistant MainAttendant FlightAttendants[]  
Flight: PlaneType Destination DepartureDate  
Destination: Country Airport FlightTime Distance ContactName ContactNumber
Airplane: id, type, maker, nrSeats

Employees: pilots, attendants, all
Voyages: all
Destinations: all
Airplanes: all

File: file attributes

Interface: interface attributes
Window: window attributes
Menu: menu attributes

## Methods
Voyage: emptySeats(), status()

Employees: sortPilots(), filterPilots(), sortAttend(), filterAttend(), sort(), filter()
Voyages: sort(), filter()
Airplanes: sort(), filter()
Destinations: sort(), filter()

File: read/write methods

Interface: inteface methods
Window: window methods
Menu: menu methods

## Um klasaritið
Klasarituð er byggt á lykil atriðum í kerfinu Þ.a. Starfsmenn, flugferð
og flug. Einnig eru hugsaðir Interface klasar og File klasi sem talar við
Collection klasana. Klasaritið er með þriggja laga hönnun þar sem Interface
fær gögn frá collection klösunum og birtir það og File klasinn tekur gögn
frá Collection klösunum og skrifar eða býr til úr skrá ný instance.

