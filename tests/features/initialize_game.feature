Feature: Initialize the game
    In order to start the game
    As a game
    I want to initalize the game

    Scenario: start with 2 players
        Given I have 2 players, with names Hugo, Pedro
        When I initialize the game
        Then the cards are distributed

