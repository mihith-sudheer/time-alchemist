"""
bucketing.py

Maps available time (in minutes) to a time bucket for task recommendation.
Rules:
- minutes < 1  -> treated as 1
- minutes > 240 -> capped at 240
"""
from __future__ import annotations

MAX_MINUTES = 240

def normalize_minutes(minutes):
    """Clamp minutes into the range [1, MAX_MINUTES]."""
    if minutes < 1:
        return 1
    if minutes > MAX_MINUTES:
        return MAX_MINUTES
    return minutes

def get_time_bucket(minutes):
    """
    Return the time bucket name for a given number of minutes.

    Buckets:
    - 1–3: tiny
    - 4–7: quick
    - 8–15: short
    - 16–25: medium
    - 26–40: deep_mini
    - 41–240: deep_work
    """
    m = normalize_minutes(minutes)
    if m <= 3:
        return "tiny"
    if m <=7:
        return "quick"
    if m <= 15:
        return "short"
    if m <= 25:
        return "medium"
    if m <= 40:
        return "deep_mini"
    return "deep_work"

