package hw2final;

public class Card {
	
	//Instance variables
	private int rank;
	private char suit;
	
	//Class Constructor
	public Card(int rank, char suit) {
		this.rank = rank;
		this.suit = suit;
	}
	
	//Copy Constructor
	public Card(Card other) {
		this(other.rank, other.suit);

	}


	//Method #1: return string representation of a given card
	@Override
	public String toString() {
		
		String rankString;

	    // Determine the rank string representation
	    switch (rank) {
	        case 11: rankString = "J"; break; // Jack
	        case 12: rankString = "Q"; break; // Queen
	        case 13: rankString = "K"; break; // King
	        case 14: rankString = "A"; break; // Ace
	        default: rankString = String.valueOf(rank); // 2-10
	    }
		return "Card: " + rankString + suit;
		
    }
		

	//Method #2: return true if two card objects are the same, and false otherwise
	public boolean equals(Object card) {
		
		//check that the given object is a valid instance of the Card class
		if (card == null || !(card instanceof Card)) {
			return false;
		}
		
		//cast instance of card to new variable in order to access 'rank' and 'suit
		Card otherCard = (Card) card;
		
		//compare card with given object
		if ((this.rank == otherCard.rank) && (this.suit == otherCard.suit)) {
			return true;
		}
		
		//If nothing else, return false
		return false;
	}
	

	//Method #3: return the rank of a give card
	public int getRank() {
		return this.rank;
	}
	
	
	//Method #4: getCardWorth
	public int getCardWorth() {
		
		int cardWorth;
		
		if (this.rank >= 11) {
			cardWorth = 10;
		}
		else {
			cardWorth = this.rank;
		}
		
		return cardWorth;
	}


	

}
