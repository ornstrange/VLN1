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

## Methods
ÞETTA ERU BARA GÖGN

## Um klasaritið
Klasarituð er byggt á lykil atriðum í kerfinu Þ.a. Starfsmenn, flugferð og flug.  Þessir klasar eru brotnir niður í smærri klasa eins og Pilot og FlightAttendant sem auðveldar vinnulag og flæði í kerfinu.  Einnig eru hugsaðir UI klasar og IO klasar sem tala við megin part af kerfinu. Klasaritið er með þriggja laga hönnun þar sem UI biður API um gögn sem talar við viðeigandi klasa og þaðan niður á IO klasa sem skila gögnum eða uppfæra gögn.
