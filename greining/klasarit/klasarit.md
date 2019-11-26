# Klasarit

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

---

| --------- |
| Employee  |
| Name      |
| Ssn       |
| Address   |
| Landline  |
| Mobile    |
| Email     |
| --------- |
| notSure() |
| --------- |

