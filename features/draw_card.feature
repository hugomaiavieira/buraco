Feature: Draw card
    As a player
    I want to draw a card
    In order to add this new card to my Hand

    Scenario: draw one card from the Stock
        Given I am a player named "Pedro"
        And I am on a game with "Hugo, Max, Dudu"
        And is my turn to play
        When I draw a card from the stock
        Then this card should be in my Hand

