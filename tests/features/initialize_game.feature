Feature: Initialize the buraco
    In order to start playing
    As a buraco
    I want to initalize it

    Scenario Outline: start with valid number of players
        Given I have the players <names>
        When I initialize the game
        Then each player has 11 cards
        And the game has 2 pots with 11 cards each

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

