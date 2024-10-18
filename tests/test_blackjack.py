from blackjack import blackjack
import config


def test_getDeck():
    ranks = [str(i) for i in range(2, 11)]
    ranks += ['J', 'Q', 'K', 'A']
    result = blackjack.getDeck()
    for rank, suit in result:
        assert rank in ranks
        assert suit in (config.HEARTS,
                        config.DIAMONDS,
                        config.SPADES,
                        config.CLUBS)


def test_getBet():
    ...
