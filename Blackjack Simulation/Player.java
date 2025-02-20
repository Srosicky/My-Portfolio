package hw2final;

public class Player {
	
	private int standValue;
	private Hand playerHand;
	private boolean softStand;
	
	
	public Player(int standValue) {
		
		playerHand = new Hand();
		this.standValue = standValue;
		softStand = true;
	}
	
	
	@Override
	public String toString() {
		return playerHand.toString();
	}
	
	
	public void play(Deck d) {
		
		// start the handValue at 0, as no cards have been added to the hand yet
	    int handValue = 0;

	    // if doing soft stands
	    if (softStand == true) {
	        while (handValue < standValue) {
	            // call the deal method and add that card to the player's hand
	            playerHand.addCard(d.deal());
	            // update the hand value based on the card that has been dealt
	            handValue = playerHand.getScore();  // Use playerHand.getScore() directly
	        }
	    }

	    // if doing hard stands
	    if (softStand == false) {
	        while (true) {
	            handValue = playerHand.getScore();  // Update the score at the start of each iteration

	            // the hand is soft
	            if (playerHand.getStatus() == true) {  // playerHand.getStatus() is used to check if the hand is soft
	                if (handValue < standValue) {
	                    // call the deal method and add that card to the player's hand
	                    playerHand.addCard(d.deal());
	                    // update the hand value based on the card that has been dealt
	                    handValue = playerHand.getScore();  // Update the hand score after the card is dealt
	                } else {
	                    break;  // Soft hand, but the hand value has reached or exceeded standValue, so stop
	                }
	            // the hand is hard
	            } else {
	                if (handValue >= standValue) {
	                    // Hard hand, if the score is at or above the standValue, stop hitting
	                    break;
	                } else {
	                    // Hand is hard, and handValue is below the standValue, so continue hitting
	                    playerHand.addCard(d.deal());
	                    handValue = playerHand.getScore();  // Update the hand score after the card is dealt
	                }
	            }
	        }
	    }
	}
	
	
	public boolean isBust() {
		if (playerHand.getScore() > 21) {
			return true;
		}
		else {
			return false;
		}
	}
	
	public void setSoftStand(boolean status) {
		softStand = status;
	}
	
	
	public int compareScores(Player other) {
		return playerHand.getScore() - other.playerHand.getScore();
	}
		
		
}
	


