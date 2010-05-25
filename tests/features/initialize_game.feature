Feature: Initialize the game
    In order to start the game
    As a game
    I want to initalize the game

    Scenario: start with 2 players
        Given I have the players Hugo, Pedro
        When I initialize the game
        Then each player has 11 cards

    Scenario: start with 3 players
        Given I have the players Hugo, Pedro, Dudu
        When I initialize the game
        Then each player has 11 cards

    Scenario: start with 4 players
        Given I have the players Hugo, Pedro, Dudu, Max
        When I initialize the game
        Then each player has 11 cards

    Scenario: do not start with 1 player
        Given I have the players Hugo
        When I initialize the game
        Then the game cannot be started

