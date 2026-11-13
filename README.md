![Skyscout — conceptual project header](docs/assets/banner.svg)

# Skyscout

![Python](docs/assets/badges/python.svg) ![Requests](docs/assets/badges/requests.svg) ![Twilio](docs/assets/badges/twilio.svg)

**A Python automation prototype that compares flight offers against destination price thresholds and prepares SMS alerts.**

## The workflow

```mermaid
flowchart LR
    S[Destination spreadsheet] --> D[DataManager]
    D --> F[FlightSearch / Tequila API]
    F --> C[Price threshold comparison]
    C --> N[NotificationManager / Twilio]
```

The implementation separates sheet access, flight queries, a flight-data object, and notification delivery. Its main script coordinates those components.

## Source map

| File | Responsibility |
|---|---|
| [main.py](main.py) | Destination iteration and price comparison |
| [data_manager.py](data_manager.py) | Sheety destination reads/updates |
| [flight_search.py](flight_search.py) | Location lookup and flight queries |
| [flight_data.py](flight_data.py) | Normalized flight information |
| [notification_manager.py](notification_manager.py) | Twilio message delivery |

## Configuration and use

This is not currently a safe zero-configuration demo. It requires compatible Python dependencies, authorized Sheety/flight-provider/Twilio accounts, and confirmed provider availability. No dependency lock or provider onboarding configuration is supplied on the default branch.

**Do not use committed credential-like values.** A flight-provider key-like literal and account-specific sheet endpoint were identified in the source. The owner must revoke/rotate any valid exposed credential and review the endpoint configuration. Documentation does not revoke credentials or clean Git history.

`main.py` performs external operations immediately: reading data, potentially updating destination codes, and potentially sending SMS. Review/configure these integrations before intentionally running it. It is not a read-only setup check.

## Current boundaries

- Empty destination lists and no-flight results currently raise unhandled exceptions.
- HTTP timeouts, response/schema checks, and robust provider failure handling are incomplete.
- Live flight searches, SMS delivery, savings, and notification reliability were not verified in the audit.

The project demonstrates API orchestration structure. A future demonstration should use synthetic destinations and stub delivery before enabling paid services. Credit applicable tutorial or upstream origins when confirmed.
