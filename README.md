<p align="center"><img src="docs/assets/banner.svg" alt="Skyscout — Watch routes. Compare fares. Prepare the alert." width="100%"></p>

<p align="center"><img src="docs/assets/badges/python.svg" alt="python" height="28"> <img src="docs/assets/badges/requests.svg" alt="requests" height="28"> <img src="docs/assets/badges/twilio.svg" alt="twilio" height="28"></p>

<p align="center"><strong>A modular Python workflow that checks flight offers against destination price thresholds and prepares SMS alerts.</strong></p>

## Overview

A modular Python workflow that checks flight offers against destination price thresholds and prepares SMS alerts.

### Why it matters

Skyscout demonstrates clean API orchestration across a destination sheet, flight search, normalized offer data, and notification delivery.

## Key features

- Destination and threshold management through Sheety
- Airport-code lookup and flight-offer search
- Normalized flight data objects
- Twilio-backed notification delivery

## Architecture

```mermaid
flowchart LR
  A[Destination sheet] --> B[DataManager]
  B --> C[FlightSearch]
  C --> D{Below threshold?}
  D -->|Yes| E[Twilio alert]
```

## Technology stack

**python** · **requests** · **twilio**

## Getting started

Create an isolated Python environment, install the imported packages, and provide your own authorized provider configuration. Review `main.py` before running because it can update remote data and send messages.
