#!/usr/bin/env python3
"""
Quick test script for the cake countdown functionality
"""

from src.cake_counter.cake import parse_time_input


def test_time_parsing():
    print("Testing time parsing functionality:")

    # Test minutes from now
    result = parse_time_input("5")
    print(f"5 minutes from now: {result}")

    # Test HH:MM format
    result = parse_time_input("23:59")
    print(f"23:59 format: {result}")

    # Test invalid input
    result = parse_time_input("invalid")
    print(f"Invalid input: {result}")

    print("\nTime parsing tests completed!")


if __name__ == "__main__":
    test_time_parsing()
