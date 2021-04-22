"""
Japanese Quiz v1.0

author: Parker J Swierzewski
language: python3
file: japanese_quiz.py
desc: This program will quiz you on a wide range of Japanese words and Kanji. You can also quiz yourself on Hiragana, Katakana,
        and/or Kanji! Please note that this quiz only contains material I've taught myself and/or learned in lectures at RIT.
    
        Japan has three writing scripts, Hiragana, Katakana, and Kanji. All of these writing scripts can be used in a single senetence,
        so it's important to know how to read and understand all three. A simple example sentence of using all three writing scripts would
        be: "テレビを見ました。" This sentence translates to "I watched TV." Each writing script is defined below.

        I used Genki An Integrated Course In Elementary Japanese 3rd Ed. for the definitions below (Definitions can be found on page 20).

        Hiragana contains 46 basic syllables that are used as conjugation endings, function words, and native Japanese words. Katakana 
        is used for writing loanwords and foreign names. Kanji are Chinese characters that were brought to Japan. Kanji represent not 
        just sounds but also meanings.
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
        print("\t4 Vocab Quizzes (MLJP201)")
        print("\t5 Hard Vocab")
        print("\n\t-1 To Exit")
        
        print("\n[!] Please note that although a Japanese keyboard isn't required, it is strongly recommended!")
        print("[!] Please also make sure you can see the Japanese characters above!")
        quizType = input("[+] What quiz would you like to take?: ")

        if quizType == "-1":
            break
        elif quizType == "1":
            japanese_questions.hiraganaQuiz()
        elif quizType == "2":
            japanese_questions.katakanaQuiz()
        #elif quizType == "3":
            #japanese_questions.kanjiQuiz()
        elif quizType == "4":
            japanese_questions.vocabQuizMLJP1()
        #elif quizType == "5":
            #japanese_questions.hardVocabQuiz()
        else:
            print("[!] This quiz has not been implemented yet.\n\n")

    print("\n\n[!] The program has concluded.")