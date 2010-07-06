Feature: Draw card
    As a player
    I want to draw a card
    In order to add this new card to my Hand

    Scenario: draw one card from the Stock
        Given I am a player named "Pedro"
        And I am on a game with "Hugo, Max, Dudu"
        And is my turn to play
        When I draw a card from the stock
        Then I should have "12" cards in my hand

    Scenario: draw one card from the Discard Pile
        Given I am a player named "Pedro"
        And I am on a game with "Hugo, Max, Dudu"
        And is my turn to play
        And the discard pile has "3" cards
        When I draw from the discard pile
        Then I should have "14" cards in my hand

