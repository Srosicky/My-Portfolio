package hw2final;

import java.util.ArrayList;

public class Deck {
	

    private ArrayList<Card> deckCards;

    // Default Constructor
    public Deck() {
        deckCards = new ArrayList<>(); // Initialize the ArrayList for cards

        // Create all 52 cards (4 suits and ranks 2 to Ace)
        char[] suits = {'c', 's', 'h', 'd'}; // clubs, spades, hearts, diamonds
        for (char suit : suits) {
            for (int rank = 2; rank <= 14; rank++) { // Ranks from 2 to 14 (Ace)
                deckCards.add(new Card(rank, suit)); // Add each card to the deck
            }
        }
    }

    // Method to deal a card from the deck
    public Card deal() {
        if (!deckCards.isEmpty()) {
            return deckCards.remove(0); // Remove and return the top card (index 0)
        }
        return null; // Return null if the deck is empty
    }

    // Method to shuffle the deck
    public void shuffle() {
        for (int i = 0; i < 100; i++) { // Shuffle 100 times
            int index1 = (int) (Math.random() * deckCards.size()); // Random index
            int index2 = (int) (Math.random() * deckCards.size()); // Another random index
            // Swap the cards at these indices
            Card temp = deckCards.get(index1);
            deckCards.set(index1, deckCards.get(index2));
            deckCards.set(index2, temp);
        }
    }

    // Method to stack the 4 Aces on top of the deck
    public void stack() {
        ArrayList<Card> aces = new ArrayList<>(); // Temporary list for Aces
        // Iterate through the deck and find all Aces
        for (int i = 0; i < deckCards.size(); i++) {
            if (deckCards.get(i).getRank() == 14) { // Check for Ace (rank 14)
                aces.add(deckCards.get(i)); // Add Ace to the temporary list
            }
        }
        // Remove Aces from the deck
        deckCards.removeAll(aces);
        // Add Aces back on top of the deck
        deckCards.addAll(0, aces);
    }

    // toString method to display the cards in the deck
    @Override
    public String toString() {
        StringBuilder result = new StringBuilder("Deck: ");
        for (Card card : deckCards) {
            result.append(card.toString()).append(", "); // Append each card's string representation
        }
        // Remove the trailing comma and space, if any
        if (result.length() > 6) {
            result.setLength(result.length() - 2); // Remove the last comma and space

        }
        //If empty, add brackets to indicated empty deck
        if (result.length() == 6) {
        	result.append("[]");
        }
        
        return result.toString(); // Return the full string representation of the deck
    }

}