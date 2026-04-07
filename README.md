# Risk-Based Authentication Log Analysis with Python
This project analyzes authentication logs to detect suspicious login activity using rule-based risk scoring.

## Objective
The goal is to identify potentially malicious or unusual authentication events by combining multiple behavioral indicators.

## Features
- Detection of failed login attempts
- Detection of off-hours logins
- Detection of country changes
- Detection of device changes
- Detection of impossible travel events
- Risk scoring for each authentication event
- Risk level classification: LOW, MEDIUM, HIGH, CRITICAL

## Technologies Used
- Python
- Pandas
- Matplotlib

## Dataset
The dataset contains simulated authentication log events with the following fields:
- timestamp
- username
- ip
- country
- device
- status

## Detection Logic
Each login event is analyzed using the following rules:
- Failed login: +20 points
- Off-hours login: +30 points
- Country change: +40 points
- Device change: +25 points
- Impossible travel: +70 points

## Risk Levels
- LOW
- MEDIUM
- HIGH
- CRITICAL

## Example Suspicious Cases
- Off-hours login activity
- Login from a different country within a short time
- Device changes for the same user
- Impossible travel between countries

## Outcome
The project produces an enriched authentication log with:
- behavioral indicators
- risk scores
- risk classification

## Sample Output

Example of detected high-risk events:

| username | timestamp           | status  | off_hours | new_country | new_device | impossible_travel | risk_score | risk_level |
|----------|---------------------|---------|-----------|-------------|------------|-------------------|------------|------------|
| carol    | 2026-04-01 15:00:00 | success | False     | True        | False      | True              | 110        | CRITICAL   |
| david    | 2026-04-01 23:42:00 | fail    | True      | False       | False      | False             | 50         | HIGH       |
| emma     | 2026-04-01 03:17:00 | fail    | True      | False       | False      | False             | 50         | HIGH       |
