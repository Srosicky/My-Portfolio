package hw2final;

public class BlackJackOdds {

    public static void main(String args[]) {

        // number of BlackJack games to simulate for each case
        int numGames = 5000;

        // set the dealer stand value (16-18) and soft/hard stand option
        for (int dStandValue = 16; dStandValue < 19; dStandValue++) {
            for (boolean dealerSoftStand : new boolean[]{true, false}) { // soft and hard stand for dealer

                // set the player stand value (16-18) and soft/hard stand option
                for (int pStandValue = 16; pStandValue < 19; pStandValue++) {
                    for (boolean playerSoftStand : new boolean[]{true, false}) { // soft and hard stand for player

                        // Variables to keep track of number of wins for each combo
                        double playerWins = 0;
                        double dealerWins = 0;
                        double tiedGames = 0;

                        // loop through simulation (iterations determined by numGames variable)
                        for (int i = 0; i < numGames; i++) {

                            // create a dealer
                            Player dealer = new Player(dStandValue);
                            dealer.setSoftStand(dealerSoftStand); // Assuming a setSoftStand method exists in the Player class

                            // create a player
                            Player player = new Player(pStandValue);
                            player.setSoftStand(playerSoftStand); // Assuming a setSoftStand method exists in the Player class

                            // create a deck and shuffle it
                            Deck deck = new Deck();
                            deck.shuffle();

                            // call the play method on the player
                            player.play(deck);

                            // call the play method on the dealer
                            dealer.play(deck);

                            // case one: player busts
                            if (player.isBust()) {
                                dealerWins++;
                            }
                            // case two: player does not bust, but dealer busts
                            else if (!player.isBust() && dealer.isBust()) {
                                playerWins++;
                            }
                            // case three: player does not bust, and dealer does not bust
                            else {
                                int scoreDifference = player.compareScores(dealer);

                                // if difference is negative, player loses
                                if (scoreDifference < 0) {
                                    dealerWins++;
                                }

                                // if difference is positive, player wins
                                if (scoreDifference > 0) {
                                    playerWins++;
                                }

                                // if difference is 0, it is a tie
                                if (scoreDifference == 0) {
                                    tiedGames++;
                                }
                            }
                        }

                        // Print results with soft/hard stand information
                        String dealerStandType = dealerSoftStand ? "Soft" : "Hard";
                        String playerStandType = playerSoftStand ? "Soft" : "Hard";

                        System.out.println("Dealer " + dStandValue + " (" + dealerStandType + " Stand) vs Player " + pStandValue + " (" + playerStandType + " Stand)");
                        System.out.println("Dealer Won: " + (dealerWins / numGames) * 100 + "%");
                        System.out.println("Player Won: " + (playerWins / numGames) * 100 + "%");
                        System.out.println("Tied Games: " + (tiedGames / numGames) * 100 + "%\n");
                    }
                }
            }
        }
    }
}
