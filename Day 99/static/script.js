document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.card');
    const winMessage = document.getElementById('win-message');
    const resetButton = document.getElementById('reset-game');
    
    let hasFlippedCard = false;
    let lockBoard = false;
    let firstCard, secondCard;
    let matchedPairs = 0;
    const totalPairs = cards.length / 2;

    function flipCard() {
        if (lockBoard) return;
        if (this === firstCard) return; // Prevents double clicking the same card

        this.classList.add('flipped');

        if (!hasFlippedCard) {
            // First card click
            hasFlippedCard = true;
            firstCard = this;
        } else {
            // Second card click
            secondCard = this;
            checkForMatch();
        }
    }

    function checkForMatch() {
        const isMatch = firstCard.dataset.value === secondCard.dataset.value;
        isMatch ? disableCards() : unflipCards();
    }

    function disableCards() {
        firstCard.classList.add('matched');
        secondCard.classList.add('matched');
        
        firstCard.removeEventListener('click', flipCard);
        secondCard.removeEventListener('click', flipCard);
        
        matchedPairs++;
        if (matchedPairs === totalPairs) {
            setTimeout(() => {
                winMessage.style.display = 'block';
            }, 500);
        }

        resetBoard();
    }

    function unflipCards() {
        lockBoard = true; // Lock the board so no other cards can be flipped
        
        setTimeout(() => {
            firstCard.classList.remove('flipped');
            secondCard.classList.remove('flipped');
            resetBoard();
        }, 1000); // Wait 1 second before flipping back
    }

    function resetBoard() {
        [hasFlippedCard, lockBoard] = [false, false];
        [firstCard, secondCard] = [null, null];
    }
    
    cards.forEach(card => card.addEventListener('click', flipCard));
    
    resetButton.addEventListener('click', () => {
        location.reload(); // The simplest way to restart with a new board
    });
});