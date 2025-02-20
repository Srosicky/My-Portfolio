package hw2final;

import java.util.ArrayList;

public class Hand {
	
   
    private ArrayList<Card> handCards;
    private int handScore;
    private boolean soft;

    // Default constructor
    public Hand() {
        handCards = new ArrayList<>(); // Create an empty ArrayList of Cards
        handScore = 0; // Initialize the score of the hand to be zero, since there is nothing in it yet
        soft = false; //initialize as false, since a empty hand is hard
    }

    // addCard
    public void addCard(Card card) {
        handCards.add(card); // Add the card to the ArrayList
        updateScore(card);
        
    }

	// removeCard
    public void removeCard(Card card) {
        handCards.remove(card); // Remove the card if it exists
    }

    // toString
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder("Hand: ");
        
       // Open brackets
        sb.append("[");
        
        // Check if there are any cards in handCards
        if (!handCards.isEmpty()) {
            for (Card card : handCards) {
                sb.append(card.toString()).append(", "); // Append each card's string representation
            }
            
            // Remove the trailing comma and space
            sb.setLength(sb.length() - 2);
        }
        
        // Close brackets
        sb.append("]"); // Add the closing bracket
        
        // Add score to string
        sb.append(" Score: " + handScore);
        
        // Add if the hand is hard or soft
        if(soft = false) {
        	sb.append("(hard)");
        }
        if(soft = true) {
        	sb.append("(soft)");
        }
        
        return sb.toString(); // Return the full string representation of the hand
    }
    
    //return the score associated with a given hand
    public int getScore() {
    	return handScore;
    }
    
    public boolean getStatus() {
    	return soft;
    }
    
    
    //update the hand's score each time a card is added to the hand
    private void updateScore(Card card) {
    	
    	// If the hand is soft, check if adding the new card would cause a bust
        if (soft) {
            if (handScore + card.getCardWorth() > 21) {
                // The ace becomes a 1, and the hand becomes hard
                handScore -= 10;
                soft = false;
            }
        }
        
        // If the card is an ace, check if the hand should be soft or hard
        if (card.getRank() == 14) {  // Assuming rank 14 represents Ace
            int aceValue;
            
            // If adding 11 would bust, assign the Ace as 1
            if (handScore + 11 > 21) {
                aceValue = 1;
            } else {
                // Otherwise, assign the Ace as 11 and mark the hand as soft
                aceValue = 11;
                soft = true;
            }
            
            handScore += aceValue;  // Add the correct Ace value to the hand score
        } else {
            // For non-Ace cards, add the card's worth to the score
            handScore += card.getCardWorth();
        }

    	
    }
    


	
}
	
	
	


