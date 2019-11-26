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
