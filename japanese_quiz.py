"""
Japanese Quiz v1.0

author: Parker J Swierzewski
language: python3
desc: This program will quiz you on a wide range of Japanese words and phrases. You can also quiz yourself on Hiragana, Katakana,
        and/or Kanji! Please note that this quiz only contains material I've taught myself and/or learned in lectures at RIT.
    
        Japan has three writing scripts, Hiragana, Katakana, and Kanji.
"""
import japanese_questions   # Japanese questions.

if __name__ == "__main__":
    while True:
        print("Japanese Quiz (日本語クイズ) v1.0")
        print("[!] This Script/Quiz is still in development!")
        print("[!] If you find any bugs or errors report them on the Github Page.")

        print("\n\n[!] Quiz Options:")
        print("\t1 Hiragana Quiz (ひらがな)")
        print("\t2 Katakana Quiz (カタカナ)")
        print("\t3 Kanji Quiz (漢字)")
        print("\t4 Hard Vocab Quiz")
        print("\t5 Phrases Quiz")
        print("\t6 Vocab Quizzes (MLJP201)")
        
        print("\n[!] Please note that although a Japanese keyboard isn't required, it is strongly recommended!")
        print("[!] Please also make sure you can see the Japanese characters above!")
        quizType = input("[+] What quiz would you like to take?: ")

        if quizType == "-1":
            break
        elif quizType == "1":
            japanese_questions.hiraganaQuiz()
        elif quizType == "2":
            japanese_questions.katakanaQuiz()
        #elif quizType == "4":
            #japanese_questions.hardVocabQuiz()
        elif quizType == "6":
            japanese_questions.vocabQuizMLJP1()
        else:
            print("[!] This quiz has not been implemented yet.\n\n")

    print("\n\n[!] The program has concluded.")