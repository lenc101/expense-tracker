# Expense Tracker

A simple command-line Expense Tracker built with Python.

This project allows users to add, view, categorize, calculate, and delete expenses through an interactive terminal menu.

## Features

- Add new expenses
- View all expenses
- Calculate total expenses
- Search expenses by category
- Delete expenses
- Input validation
- Error handling for invalid numeric input
- Prevent empty descriptions and categories
- Prevent zero or negative expense amounts
- Interactive command-line menu

## Technologies

- Python 3
- Lists
- Dictionaries
- Functions
- Loops
- Conditional statements
- `try` / `except`
- User input handling
- `.append()`
- `.pop()`
- `enumerate()`

## How It Works

Expenses are stored as dictionaries inside a list.

Example expense:

    {
        "description": "Coffee",
        "amount": 60,
        "category": "Food"
    }

The program provides an interactive menu:

    1. Add expense
    2. View expenses
    3. View total
    4. View expenses by category
    5. Delete expense
    6. Exit

## Input Validation

The application validates user input to prevent common errors.

- Empty descriptions are rejected.
- Empty categories are rejected.
- Invalid numbers are handled with `try` / `except`.
- Expenses must have an amount greater than `0`.
- Invalid expense numbers cannot be deleted.
- Invalid menu options are rejected.

## Example

    1. Add expense
    2. View expenses
    3. View total
    4. View expenses by category
    5. Delete expense
    6. Exit

    Choose an option: 3

    Total: 430 CZK

## What I Learned

This project helped me practice working with structured data and building a multi-function Python application.

Key concepts practiced:

- Working with lists of dictionaries
- Creating and calling functions
- Using loops to process data
- Using `enumerate()` to display numbered items
- Filtering data with conditions
- Adding items with `.append()`
- Removing items with `.pop()`
- Handling invalid user input
- Building an interactive CLI application

## Project Status

**Completed**

This is Project #17 in my Python learning roadmap.

## Author

**Lenc101**

GitHub: https://github.com/Lenc101