#!/bin/python3
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
import japanese_questions   # Japanese questions

if __name__ == "__main__":
    while True:
        print("Japanese Quiz (日本語クイズ) v1.0")
        print("[!] 問題がありますか？ https://github.com/magnus-ISU/Japanese-Quiz")

        print("\n[!] クイズオプション:")
        print("\tー ひらがな")
        print("\t二 カタカナ")
        print("\t三 漢字")
        print("\t四 Vocab Quizzes (MLJP201)")
        #print("\t五 Hard Vocab")
        
        quizType = input("[+] どのクイズを受験しますか？ ")

        if quizType == "-1":
            break
        elif quizType == "1":
            japanese_questions.hiraganaQuiz()
        elif quizType == "2":
            japanese_questions.katakanaQuiz()
        elif quizType == "3":
            result = japanese_questions.kanjiQuiz()
            if result == -1:
                break
        elif quizType == "4":
            japanese_questions.vocabQuizMLJP1()
        #elif quizType == "5":
            #japanese_questions.hardVocabQuiz()
        else:
            print("[!] This quiz has not been implemented yet.\n\n")
