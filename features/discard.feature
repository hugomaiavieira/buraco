Feature: Discard
    As a player
    I want to discard
    In order to remove a card from my Hand

    Scenario: discard
        Given I am a player named "Pedro"
        And I am on a game with "Hugo, Max, Dudu"
        And is my turn to play
        When I discard
        Then I should have "10" cards in my hand

