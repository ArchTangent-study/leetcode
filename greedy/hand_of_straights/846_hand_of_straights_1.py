from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """Warning: can't iterate and mutate a dict, so use count=0 vice deleting keys."""
        # Use a counter that decrements every time a card is consumed
        num_cards = len(hand)
        cards = {}
        for card in hand:
            if card in cards:
                cards[card] += 1
            else:
                cards[card] = 1

        # Find a card that *starts* a sequence, then check if it forms a group
        while num_cards > 0:
            for card in cards:
                # Don't check if the card is no longer in play
                if cards[card] == 0:
                    continue
                prev = card - 1
                # Start of sequence - count sequential cards up to groupSize
                if prev not in cards or cards[prev] == 0:
                    # Note: this includes card that started sequence
                    for increment in range(0, groupSize):
                        next_card = card + increment
                        if next_card in cards and cards[next_card] > 0:
                            # Remove current card
                            cards[next_card] -= 1
                            num_cards -= 1
                        else:
                            # Not enough consecutive cards found -> return False
                            return False

        # If you get through all cards -> success
        return True
