import time
import random

# Sample texts for typing test
sample_texts = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a popular programming language for data analysis.",
    "A journey of a thousand miles begins with a single step.",
    "Artificial intelligence is transforming the way we live and work.",
    "Typing practice improves your speed and accuracy."
]

def calculate_wpm_and_accuracy(start_time, end_time, user_input, sample_text):
    # Calculate time elapsed
    elapsed_time = end_time - start_time
    elapsed_minutes = elapsed_time / 60
    
    # Calculate WPM
    words = user_input.split()
    wpm = len(words) / elapsed_minutes
    
    # Calculate accuracy
    sample_words = sample_text.split()
    correct_words = sum(1 for i, word in enumerate(user_input.split()) if i < len(sample_words) and word == sample_words[i])
    accuracy = (correct_words / len(sample_words)) * 100
    
    return wpm, accuracy

def typing_test():
    # Select a random text
    sample_text = random.choice(sample_texts)
    print("\nTyping Speed Test")
    print("-" * 30)
    print("Type the following text as quickly and accurately as possible:")
    print(f"\n\"{sample_text}\"\n")
    
    # Wait for user to start typing
    input("Press Enter when you are ready to start...\n")
    start_time = time.time()
    
    # Capture user input
    user_input = input("Start typing here:\n")
    end_time = time.time()
    
    # Calculate results
    wpm, accuracy = calculate_wpm_and_accuracy(start_time, end_time, user_input, sample_text)
    
    # Display results
    print("\nResults:")
    print("-" * 30)
    print(f"Typing Speed: {wpm:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")
    print("-" * 30)

# Run the typing test
if __name__ == "__main__":
    typing_test()

