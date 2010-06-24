Feature: Initialize the buraco
    As a buraco
    I want to initalize it
    In order to start playing

    Scenario Outline: start with valid number of players
        Given I have the players <names>
        When I initialize the game
        Then each player has 11 cards
        And the game has 2 pots with 11 cards each
        And the game has the stock with <ramaining_cards>

    Examples:
    |names                 |ramaining_cards |
    |Hugo, Pedro           |60              |
    |Hugo, Pedro, Dudu     |49              |
    |Hugo, Pedro, Dudu, Max|38              |

    Scenario Outline: do not start with invalid number of players
        Given I have the players <names>
        When I initialize the game
        Then the game cannot be started

    Examples:
    |names                          |
    |Hugo                           |
    |Hugo, Pedro, Dudu, Max, Rodrigo|

