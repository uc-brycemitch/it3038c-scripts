word = input("Please enter a word to count the vowels/consonants:");
#both set to 0 before counter starts
vowel=0
consonant=0

for i in word:
    if(i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='U'):
        vowel=vowel+1;
    #checks for uppercase and lowercase vowels, increments by one to count the total
    else:
        consonant=consonant+1;
    #anything that is not a vowel is a consonant, increments bt one to count the total
print("The number of vowels is: ", vowel, "\n The number of consonants is: ", consonant, "\n The total number of letters is: ", consonant+vowel);
