# Class Diagram

```
Employee
    |
    --Pilot
    |
    --FlightAttendant

Voyage
    |
    2->Flight
    |
    2->Pilot
    |
    +->FlightAttendant

Flight
    |
    1->Destination

```

## Attributes
Employee: Name License Ssn Address Landline Mobile Email  
Pilot: License  
FlightAttendant: Rank  
Voyage: OutFlight ReturnFlight FlightCaptain FlightAssistant MainAttendant FlightAttendants[]  
Flight: PlaneType Destination DepartureDate  
Destination: Country Airport FlightTime Distance ContactName ContactNumber
File: file attributes
Interface: interface attributes
Window: window attributes
Menu: menu attributes

## Methods
Voyage: emptySeats(), status()
File: read/write methods
Interface: inteface methods
Window: window methods
Menu: menu methods

## Um klasaritið
Klasarituð er byggt á lykil atriðum í kerfinu Þ.a. Starfsmenn, flugferð og flug.
Einnig eru hugsaðir Interface klasar og File klasi sem talar við .
Klasaritið er með þriggja laga hönnun þar sem UI biður API um gögn sem talar við viðeigandi
klasa og þaðan niður á IO klasa sem skila gögnum eða uppfæra gögn.

