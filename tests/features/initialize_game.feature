Feature: Initialize the game
    In order to start the game
    As a game
    I want to initalize the game

    Scenario Outline: start with valid number of players
        Given I have the players <names>
        When I initialize the game
        Then each player has 11 cards

    Examples:
    |names                 |
    |Hugo, Pedro           |
    |Hugo, Pedro, Dudu     |
    |Hugo, Pedro, Dudu, Max|

    Scenario Outline: do not start with invalid number of players
        Given I have the players <names>
        When I initialize the game
        Then the game cannot be started

    Examples:
    |names                          |
    |Hugo                           |
    |Hugo, Pedro, Dudu, Max, Rodrigo|

