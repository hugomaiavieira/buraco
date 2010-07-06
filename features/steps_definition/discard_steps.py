from lettuce import *

@step(r'When I discard')
def when_i_discard(step):
    # Take any card of the player's hand. The 5 was occasional
    card = world.player.hand[5]
    world.player.discard(card)

