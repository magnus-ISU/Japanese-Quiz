"""
Japanese Questions v1.0

author: Parker J Swierzewski
language: python3
file: japanese_questions.py
desc: This program contains the questions that japanese_quiz.py will utilize.
"""
import random   # Used to randomly shuffle question.

class Question:
    """
    Used to define questions.
    """
    def __init__(self, question, correctAnswer, alternateAnswers=None, kanji=None, context=None):
        """
        This function is used to create a Question object.

        :param self: The object.
        :param question: The question prompt.
        :param correctAnswer: The best, or correct answer.
        :param alternateAnswers: Other accepted answers.
        :param kanji: The kanji of the correctAnswer (None if no kanji).
        :param context: Provides extra information to help.
        """
        self.question = question
        self.correctAnswer = correctAnswer
        self.alternateAnswers = alternateAnswers
        self.kanji = kanji
        self.context = context

    def correct(self, answer, englishQuestion):
        """
        A pointless function to tell the user
        that they got the answer correct.

        :param self: The question object.
        :param answer: The answer the user submitted.
        :param kanjiQuiz: Whether or not the Kanji Quiz is active.
        :return: None
        """
        print("Correct! :)")

        # There is no need to display the Kanji if the Kanji Quiz is active.
        if not englishQuestion:
            if (isHiragana(answer) or isKatakana(answer)) and (self.kanji is not None):
                print("The Kanji (漢字) for this word is {}".format(self.kanji))

    def incorrect(self, englishQuestion):
        """
        A pointless function to tell the user
        that they got the answer incorrect.

        :param self: The question object.
        :param kanjiQuiz: Whether or not the Kanji Quiz is active.
        :return: None
        """
        print("Incorrect! :/")
        print("The correct answer was {}".format(self.correctAnswer))
        
        if self.alternateAnswers is not None:
            if type(self.alternateAnswers) == list:
                print("{} were also accepted answers!".format(self.alternateAnswers))
            else:
                print("{} was also an accepted answers!".format(self.alternateAnswers))
        
        if englishQuestion:
            if self.kanji is not None:
                print("{} was the accepted Kanji answer!".format(self.kanji))

    def isAlternate(self, response):
        """
        This function is used to determine whether the user entered the
        alternate answer.

        :param self: The question object.
        :param response: The user's response.
        :return: Boolean Flag (True = Correct)
        """
        if self.alternateAnswers is not None:
            if type(self.alternateAnswers) == list and response.lower() in self.alternateAnswers:
                return True
            elif type(self.alternateAnswers) == str and response.lower() == self.alternateAnswers:
                return True
        if self.kanji is not None and response == self.kanji:
            return True
        return False

    def reverseQuestion(self, quizType):
        """
        This function is used to reverse the question and the answer
        so that the quiz is always changing and keeping the user
        on the spot.

        :param self: The question object.
        :param quizType: Used to correctly display a prompt.
        :return: None
        """
        q = self.question
        a = self.correctAnswer

        if quizType == "Hiragana" or quizType == "Katakana":
            self.question = a
            self.correctAnswer = q
        elif quizType == "Vocab":
            # This if block will check if there is a Kanji and display it with the prompt.
            if self.kanji is not None:
                a += " (" + self.kanji + ")"
            self.question = a
            self.correctAnswer = q
            self.alternateAnswers = None

class KanjiQuestion:
    """
    Used to define Kanji questions.
    """
    def __init__(self, question, correctAnswer, alternateAnswers=None, meaning=""):
        """
        This function is used to create a KanjiQuestion object.

        :param self: The object.
        :param question: The question prompt.
        :param correctAnswer: The best, or correct answer. 
        :param alternateAnswers: Other accepted answers.
        :param meaning: The meaning of the Kanji.
        """
        self.question = question
        self.correctAnswer = correctAnswer
        self.alternateAnwsers = alternateAnswers
        self.meaning = meaning

    def correct(self):
        pass

    def incorrect(self):
        pass

def calculateScore(score, max_score):
    """
    This function is used to print the score the
    user received.

    :param score: The score the user received.
    :param max_score: The max score for the quiz.
    :return: None
    """
    n_score = (score/max_score)*100

    if n_score < 80:
        print("\n[!] Congrats you scored {:03.2f}!".format(n_score))
        print("[!] You got {} wrong!".format(max_score-score))
    elif n_score < 70:
        print("\n[!] Nice try! You scored {:03.2f}!".format(n_score))
        print("[!] You got {} wrong!".format(max_score-score))
    else:
        print("\n[!] You scored {:03.2f}! Keep practicing!".format(n_score))
        print("[!] You got {} wrong!".format(max_score-score))

    input("[!] Press any key to continue...")

def isHiragana(str):
    """
    This function is used to determine whether a given string is
    in Hiragana. This is mainly used for the vocab quizzes as most
    Japanese sentences contain all three writing scripts.

    :param str: The string entered.
    :return: Boolean Flag (True = Is Hiragana).
    """
    hiraganaCharacters = { 
                           # Hiragana characters including Dakuten, or diacritic marks.
                           "あ", "い", "う", "え", "お",                            
                           "か", "き", "く", "け", "こ", "が", "ぎ", "ぐ", "げ", "ご",                                 
                           "さ", "し", "す", "せ", "そ", "ざ", "じ", "ず", "ぜ", "ぞ",                                 
                           "た", "ち", "つ", "て", "と", "だ", "ぢ", "づ", "で", "ど",                                 
                           "な", "に", "ぬ", "ね", "の",                                                              
                           "ま", "み", "む", "め", "も",                                                              
                           "は", "ひ", "ふ", "へ", "ほ", "ば", "び", "ぶ", "べ", "ぼ", "ぱ", "ぴ", "ぷ", "ぺ", "ぽ",    
                           "ら", "り", "る", "れ", "ろ",
                           "や",       "ゆ",       "よ",
                           "わ",                   "を", 
                           "ん",
                           
                           # Combos
                           "ゃ", "ゅ", "ょ" 
                           }
    
    for ch in str:
        if ch not in hiraganaCharacters:
            return False
    return True
       
def isKatakana(str):
    """
    This function is used to determine whether a given string is
    in Katakana. This is mainly used for the vocab quizzes as most
    Japanese sentences contain all three writing scripts.

    :param str: The string entered.
    :return: Boolean Flag (True = Is Katakana).
    """
    katakanaCharacters = { 
                           # Katakana characters including Dakuten, or diacritic marks.
                           "ア", "イ", "ウ", "エ", "オ",                            
                           "カ", "キ", "ク", "ケ", "コ", "ガ", "ギ", "グ", "ゲ", "ゴ",                                 
                           "サ", "シ", "ス", "セ", "ソ", "ザ", "ジ", "ズ", "ゼ", "ゾ",                                 
                           "タ", "チ", "ツ", "テ", "ト", "ダ", "ヂ", "ヅ", "デ", "ド",                                 
                           "ナ", "ニ", "ヌ", "ネ", "ノ",                                                              
                           "マ", "ミ", "ム", "メ", "モ",                                                              
                           "ハ", "ヒ", "フ", "ヘ", "ホ", "バ", "ビ", "ブ", "ベ", "ボ", "パ", "ピ", "プ", "ペ", "ポ",    
                           "ラ", "リ", "ル", "レ", "ロ",
                           "ヤ",       "ユ",       "ヨ",
                           "ワ",                   "ヲ", 
                           "ン",
                           
                           # Combos
                           "ャ", "ュ", "ョ", 
                           }
    
    for ch in str:
        if ch not in katakanaCharacters:
            return False
    return True

def hasJapaneseKeyboard():
    """
    This function is used to determine whether or not the user
    has a Japanese keyboard installed. If they do they'll be asked
    to set it up before continuing.
    
    :return: Boolean Flag (True = Has Japanese Keyboard)
    """
    while True:
        flag = input("Do you have a Japanese keyboard installed? (y/n): ")
        
        if flag.lower() == "y" or flag.lower() == "n":
            break

    if flag.lower() == "y":
        flag = True
        print("[!] You will be asked to type in Japanese Writing Script(s)!")
        wait = input("[!] Please get your Japanese keyboard setup and enter `y` when ready: ")
        
        while wait.lower() != "y":
            wait = input("[!] Please get your Japanese keyboard setup and enter `y` when ready: ")
            continue
            
    elif flag.lower() == "n":
        flag = False
        print("[!] You will only be asked to type Romaji!")
        print("[!] Set up a Japanese keyboard for the full experience! :)")

    return flag

def hiraganaQuiz():
    """
    This function is for the Hiragana Quiz. You'll only be tested on
    Hiragana characters. You'll either need to enter the Hiragana
    Character or write the Romaji (romanized version, i.e. だ = da).

    :return: None
    """
    print("Hiragana Quiz\n")
    hasJapaneseKeyboard()

    hiragana = [ Question("あ", "a"), Question("い", "i"), Question("う", "u"), Question("え", "e"), Question("お", "o"),
                    Question("か", "ka"), Question("き", "ki"), Question("く", "ku"), Question("け", "ke"), Question("こ", "ko"),
                    Question("が", "ga"), Question("ぎ", "gi"), Question("ぐ", "gu"), Question("げ", "ge"), Question("ご", "go"),
                    Question("さ", "sa"), Question("し", "shi"), Question("す", "su"), Question("せ", "se"), Question("そ", "so"),
                    Question("ざ", "za"), Question("じ", "ji"), Question("ず", "zu"), Question("ぜ", "ze"), Question("ぞ", "zo"),
                    Question("た", "ta"), Question("ち", "chi"), Question("つ", "tsu"), Question("て", "te"), Question("と", "to"),
                    Question("だ", "da"), Question("ぢ", "ji"), Question("づ", "zu"), Question("で", "de"), Question("ど", "do"),
                    Question("な", "na"), Question("に", "ni"), Question("ぬ", "nu"), Question("ね", "ne"), Question("の", "no"),
                    Question("は", "ha"), Question("ひ", "hi"), Question("ふ", "fu", "hu"), Question("へ", "he"), Question("ほ", "ho"),
                    Question("ば", "ba"), Question("び", "bi"), Question("ぶ", "bu"), Question("べ", "be"), Question("ぼ", "bo"),
                    Question("ぱ", "pa"), Question("ぴ", "pi"), Question("ぷ", "pu"), Question("ぺ", "pe"), Question("ぽ", "po"),
                    Question("ま", "ma"), Question("み", "mi"), Question("む", "mu"), Question("め", "me"), Question("も", "mo"),
                    Question("や", "ya"), Question("ゆ", "yu"), Question("よ", "yo"), 
                    Question("ら", "ra"), Question("り", "ri"), Question("る", "ru"), Question("れ", "re"), Question("ろ", "ro"),
                    Question("わ", "wa"), Question("を", "wo"), 
                    Question("ん", "n") ]

    input("\nThe quiz is about to begin! Press any key to start...")
    score = 0
    max_score = len(hiragana)

    random.shuffle(hiragana)
    for element in hiragana:
        print("\n" + element.question)
        answer = input("What character is this?: ")

        if (answer.lower() == element.correctAnswer.lower()) or element.isAlternate(answer):
            element.correct(answer, False)
            score += 1
        else:
            element.incorrect(False)

    calculateScore(score, max_score)

def katakanaQuiz():
    """
    This function is for the Katakana Quiz. You'll only be tested on
    Katakana characters. You'll either need to enter the Katakana
    Character or write the Romaji (romanized version, i.e. ダ = da).

    :return: None
    """
    print("Katakana Quiz (カタカナ)\n")
    hasJapaneseKeyboard()

    katakana = [ Question("ア", "a"), Question("イ", "i"), Question("ウ", "u"), Question("エ", "e"), Question("オ", "o"),
                    Question("カ", "ka"), Question("キ", "ki"), Question("ク", "ku"), Question("ケ", "ke"), Question("コ", "ko"),
                    Question("ガ", "ga"), Question("ギ", "gi"), Question("グ", "gu"), Question("ゲ", "ge"), Question("ゴ", "go"),
                    Question("サ", "sa"), Question("シ", "shi"), Question("ス", "su"), Question("セ", "se"), Question("ソ", "so"),
                    Question("ザ", "za"), Question("ジ", "ji"), Question("ズ", "zu"), Question("ゼ", "ze"), Question("ゾ", "zo"),
                    Question("タ", "ta"), Question("チ", "chi"), Question("ツ", "tsu"), Question("テ", "te"), Question("ト", "to"),
                    Question("ダ", "da"), Question("ヂ", "ji"), Question("ヅ", "zu"), Question("デ", "de"), Question("ド", "do"),
                    Question("ナ", "na"), Question("ニ", "ni"), Question("ヌ", "nu"), Question("ネ", "ne"), Question("ノ", "no"),
                    Question("ハ", "ha"), Question("ヒ", "hi"), Question("フ", "fu", "hu"), Question("ヘ", "he"), Question("ホ", "ho"),
                    Question("バ", "ba"), Question("ビ", "bi"), Question("ブ", "bu"), Question("べ", "be"), Question("ボ", "bo"),
                    Question("パ", "pa"), Question("ピ", "pi"), Question("プ", "pu"), Question("ぺ", "pe"), Question("ポ", "po"),
                    Question("マ", "ma"), Question("ミ", "mi"), Question("ム", "mu"), Question("メ", "me"), Question("モ", "mo"),
                    Question("ヤ", "ya"), Question("ユ", "yu"), Question("ヨ", "yo"), 
                    Question("ラ", "ra"), Question("リ", "ri"), Question("ル", "ru"), Question("レ", "re"), Question("ロ", "ro"),
                    Question("ワ", "wa"), Question("ヲ", "wo"), 
                    Question("ン", "n") ]

    input("\nThe quiz is about to begin! Press any key to start...")
    score = 0
    max_score = len(katakana)

    random.shuffle(katakana)
    for element in katakana:
        print("\n" + element.question)
        answer = input("What character is this?: ")

        if (answer.lower() == element.correctAnswer.lower()) or element.isAlternate(answer):
            element.correct(answer, False)
            score += 1
        else:
            element.incorrect(False)

    calculateScore(score, max_score)

def startHomeworkVocabQuiz():
    """
    This function will start a quiz based on words/phrases given in the
    homework. The user will get to choose what chapter they want to be
    quizzed from.

    :return: None
    """
    pass

def vocabQuizPrompt(quizList):
    """
    This function will print the prompt for each vocab quiz.

    :param quizList: The vocab quiz list (chapter).
    :return: None
    """
    flag = hasJapaneseKeyboard()

    input("\nThe quiz is about to begin! Press any key to start...")
    score = 0
    max_score = len(quizList)

    random.shuffle(quizList)
    for element in quizList:
        choice = 0
        if flag:
            choice = random.randint(0, 1)

        if choice == 0:
            prompt = ""
            if element.context is not None:
                prompt = element.question + " (" + element.context + ")"
            else:
                prompt = element.question

            print("\n" + prompt)
            answer = input("What is the Japanese for the word above?: ")

            if (answer.lower() == element.correctAnswer) or (answer.lower() == element.isAlternate(answer)):
                element.correct(answer, False)
                score += 1
            else:
                element.incorrect(False)
        else:
            element.reverseQuestion("Vocab")

            print("\n" + element.question)
            answer = input("What is the English for the word above?: ")

            c = element.correctAnswer.lower().split("/")
            if (answer.lower() in c):
                element.correct(answer, False)
                score += 1
            else:
                element.incorrect(False)
        
    # Calculates the users final score.
    calculateScore(score, max_score)

def vocabQuizMLJP1():
    """
    This function will start a quiz based on the chapater vocabulary for
    MLJP 201 (Japanese Beginner 1). The user will get to choose what chapter
    they want to be quizzed from.

    :return: None
    """
    # Chapter 1 Vocab. Located on Genki page 38-39.
    chapter1Vocab = [ Question("College/University", "だいがく", "daigaku", "大学"), Question("High School", "こうこう", "koukou" "高校生"), 
                     Question("Student", "がくせい", "gakusei" "学生"), Question("College Student", "だいがくせい", "daigakusei" "大学生"), 
                     Question("International Student", "りゅうがくせい", "ryuugakusei", "留学生"), Question("Teacher/Professor", "せんせい", "sensei" "先生"), 
                     Question("First Year Student", "いちねんせい", "ichinensei", "一年生"), Question("Major", "せんこう", "senkou", "専攻"), Question("I", "わたし", "watashi" "私"), 
                     Question("Friend", "ともだち", "tomodachi" "友達"), Question("Mr/Ms", "さん", "san"), Question("Japanese People", "にほんじん", "nihonjin", "日本人"),
                     Question("Now", "いま", "ima", "今"), Question("AM", "ごぜん", "gozen", "午前"), Question("PM", "ごご", "gogo", "午後"), Question("O'Clock", "じ", "ji", "時"),
                     Question("One O'Clock", "いちじ", "ichiji", "一時"), Question("Half", "はん", "han", "半"), Question("2:30", "にじはん", "nijihan", "二時半"), 
                     Question("Japan", "にほん", "nihon", "日本"), Question("America/USA", "アメリカ", "amerika"), Question("Language", "ご", "go", "語"),  
                     Question("Japanese Language", "にほんご", "nihongo", "日本語"), Question("Years Old", "さい", "sai", "歳"), Question("Telephone/Phone", "でんわ", "denwa", "電話"),  
                     Question("Number", "ばんごう", "bangou", "番号"), Question("Name", "なまえ", "namae", "名前"), Question("What", "なん", ["nan", "nani", "なに"], "何"),
                     Question("Um", "あの", "ano"), Question("Yes", "はい", "hai"), Question("That's Right", "そうです", "soudesu"), Question("I See/Is That So", "そうですか", "soudesuka"),
                     Question("Britian", "イギリス", "igirisu"), Question("Australia", "オーストラリア", "oosutoraria"), Question("Korea", "かんこく", "kankoku", "韓国"),
                     Question("China", "ちゅうごく", "chuugoku", "中国"), Question("India", "インド", "indo"), Question("Egypt", "エジプト", "ejiputo"), 
                     Question("Philippines", "フィリピン", "firipin"), Question("Asian Studies", "アジアけんきゅう", "ajiakenkyuu", "アジア研究"), 
                     Question("Economics", "けいざい", "keizai", "経済"), Question("Engineering", "こうがく", "kougaku"), 
                     Question("International Relations", "こくさいかんけい", "kakusaikankei", "国際関係"), Question("Computer", "コンピュータ", "konpyuuta"), 
                     Question("Politics", "せいじ", "seiji", "政治"), Question("Biology", "せいぶつがく", "seibutsugaku", "生物学"), Question("Business", "ビジネス", "bijinesu"),
                     Question("Literature", "ぶんがく", "bungaku", "文学"), Question("History", "れきし", "rekishi", "歴史"), Question("Doctor", "いしゃ", "isha", "医者"), 
                     Question("Office Worker", "かいしゃいん", "kaishain", "会社員"), Question("Nurse", "かんごし", "kangoshi", "看護師"), 
                     Question("High School Student", "こうこうせい", "koukousei", "高校生"), Question("Housewife", "しゅふ", "shufu", "主婦"), 
                     Question("Graduate Student", "だいがくいんせい", "daigakuinsee", "大学院生"), Question("Lawyer", "べんごし", "bengoshi", "弁護士"), 
                     Question("Mother", "おかあさん", "okaasan", "お母さん"), Question("Father", "お父さん", "otousan", "お父さん"), 
                     Question("Older Sister", "おねえさん", "oneesan", "お姉さん"), Question("Older Brother", "おにいさん", "oniisan", "お兄さん"), 
                     Question("Younger Sister", "いもうと", "imouto", "妹"), Question("Younger Brother", "おとうと", "otouto", "弟") ]

    # Chapter 2 Vocab. Located on Genki page 58-69.
    chapter2Vocab = [ Question("This One", "これ", "kore"), Question("That One", "それ", "sore"), Question("That One Over There", "あれ", "are"), Question("Which One", "どれ", "dore"),
                     Question("This", "この", "kono"), Question("That", "その", "sono"), Question("That Over There", "あの", "ano"), Question("Which", "どの", "dono"), 
                     Question("Here", "ここ", "koko"), Question("There", "そこ", "soko"), Question("Over There", "あそこ", "asoko"), Question("Where", "どこ", "doko"), 
                     Question("Who", "だれ", "dare"), Question("Delicious", "おいしい", "oishii", "美味しい"), Question("Fish", "さかな", "sakana", "魚"), 
                     Question("Pork Cutlet" "とんかつ", "tonkatsu"), Question("Meat", "にく", "niku", "肉"), Question("Menu", "メニュー", "menyuu"),
                     Question("Vegetables", "やさい", "ysai", "野菜"), Question("Umbrella", "かさ", "kasa", "傘"), Question("Bag", "かばん", "kaban", "鞄"), 
                     Question("Shoes", "くつ", "kutsu", "靴"), Question("Wallet", "さいふ", "saifu", "財布"), Question("Jeans", "ジーンズ", "jiinsu"), 
                     Question("Bicycle", "じてんしゃ", "jitensha", "自転車"), Question("Newspaper", "しんぶん", "shinbun", "新聞"), Question("Smartphone/Mobile", "スマホ", "sumaho"),
                     Question("T-Shirt", "Ｔシャツ", "tiishatsu"), Question("Watch/Clock", "とけい", "tokei", "時計"), Question("Notebook", "ノート", "nooto"), Question("Pen", "ぺん", "pen"),
                     Question("Hat/Cap", "ぼうし", "boushi", "防止"), Question("Book", "ほん", "hon", "本"), Question("Bank", "ぎんこう", "ginkou", "銀行"), 
                     Question("Convenience Store", "コンビニ", "konbini"), Question("Toilet/Restroom", "トイレ", "toire"), Question("Library", "としょかん", "toshokan", "図書館"),
                     Question("Post Office", "ゆうびんきょく", ["yuubinkyoku", "郵便局"]), Question("Britian", "イギリス", "igirisu"), Question("Korea", "かんこく", ["kankoku", "韓国"]),
                     Question("China", "ちゅうごく", "chuugoku", "中国"), Question("English", "えいご", "eigo", "英語"), Question("Economics", "けいざい", "keizai", "経済"), 
                     Question("Computer", "コンピュータ", "konpyuuta"), Question("Business", "ビジネス", "bijinesu"), Question("History", "れきし", "rekishi", "歴史"),
                     Question("Mother", "おかあさん", "okaasan", "お母さん"), Question("Father", "お父さん", "otousan", "お父さん"), 
                     Question("Welcome", "いらっしゃいませ", "irasshamase", context="To A Store"), Question("Please", "おねがいします", "onegaishimasu", "お願いします"), 
                     Question("Please Give Me", "ください", "kudasai"), Question("Then/If That Is The Case", "じゃあ", "jaa"), Question("Here It Is", "どうぞ", "douzo"), 
                     Question("Thank-you", "どうも", "doumo", context="Informal Version") ]

    # Chapter 3 Vocab. Located on Genki page 84-85.
    chapter3Vocab = [ Question("Movie", "えいが", "eiga", "映画"), Question("Music", "おんがく", "ongaku", "音楽"), Question("Magazine", "ざっし", "zasshi", "雑誌"),
                     Question("Sports", "スポーツ", "supaatsu"), Question("Date", "デート", "deeto", context="Romantic Date"), 
                     Question("Tennis", "テニス", "tenisu"), Question("TV", "テリビ", "teribi"), Question("Ice Cream", "アイスクリーム", "aisukariimu"), 
                     Question("Hamburger", "ハンバーガー", "hanbaagaa"), Question("Sake/Alcohol", "おさけ", "osake", "お酒"),
                     Question("Green Tea/Tea", "おちゃ", "ocha", "お茶"), Question("Coffee", "コーヒー", "koohii"), Question("Water", "みず", "mizu", "水"),
                     Question("Breakfast", "あさごはん", "asagohan", "朝ご飯"), Question("Lunch", "ひるごはん", "hirugohan", "昼ご飯"),
                     Question("Dinner", "ばんごはん", "bangohan", "晩ご飯"), Question("Home/House/My Place", "いえ", ["ie", "uchi", "うち"], "家"), 
                     Question("School", "がっこう", "gakkou", "学校"), Question("Cafe", "カフェ", "cafe"), Question("Tomorrow", "あした", "ashita", "明日"),
                     Question("Today", "きょう", "kyou", "今日"), Question("Morning", "あさ", "asa", "朝"), Question("Tonight", "こんばん", "konban", "今晩"),
                     Question("Every Day", "まいにち", "mainichi", "毎日"), Question("Every Night", "まいばん", "maiban", "毎晩"),
                     Question("Weekend", "しゅうまつ", "shuumatsu", "週末"), Question("Saturday", "どようび", "doyoubi", "土曜日"), 
                     Question("Sunday", "にちようび", "nichiyoubi", "日曜日"), Question("When", "いつ", "itsu"), Question("At About/Around", "ごろ", "goro"), 
                     Question("To Go", "いく", "iku", "行く"), Question("To Go Back/To Return", "かえる", "kaeru", "帰る"), Question("To Listen/To Hear", "きく", "kiku", "聞く"),
                     Question("To Drink", "のむ", "nomu", "飲む"), Question("To Speak/To Talk", "はなす", "hanasu", "話す"), Question("To Read", "よむ", "yomu", "読む"),
                     Question("To Get Up", "おきる", "okiru", "起きる"), Question("To Eat", "たべる", "taberu", "食べる"), Question("To Sleep/To Go To Sleep", "ねる", "neru", "寝る"),
                     Question("To See/To Look At/To Watch", "みる", "miru", "見る"), Question("To Come", "くる", "kuru", "来る"), Question("To Do", "する", "suru"),
                     Question("To Study", "べんきょうする", "benkyoushiru", "勉強する"), Question("Good", "いい", "ii"), Question("Early", "はやい", "hayai", "早い"),
                     Question("Not Much", "あまり", "amari"), Question("Not At All", "ぜんぜん", "zenzen", "全然"), Question("Usually", "たいてい", "taitei", "大抵"),
                     Question("A Little", "ちょっと", "chyotto"), Question("Sometimes", "ときどき", "tokidoki", "時々"), Question("Often/Much", "よく", "yoku"),
                     Question("That's Right/Let Me See", "そうですね", "soudesune"), Question("But", "でも", "demo"), Question("How About/How Is", "どうですか", "doudesuka"), 
                     Question("Yes", "ええ", "ee", context="Informal Version") ]

    # Chapter 4 Vocab. Located on Genki page 104-106.
    chapter4Vocab = [ Question("Game", "ゲーム", "geemu"), Question("Part-Time Job", "アルバイト", ["arubaito", "バイト", "baito"]), Question("Shopping", "かいもの", "kaimono", "買い物"),
                     Question("Class", "クラス", "kurasu"), Question("Dog", "いぬ", "inu", "犬"), Question("Cat", "ねこ", "neko", "猫"), Question("Person", "ひと", "hito", "人"),
                     Question("Child", "こども", "kodomo", "子供"), Question("You", "あなた", "anata"), Question("Chair", "いす", "isu", "椅子"), Question("Desk", "つくえ", "tsukue", "机"),
                     Question("Picture/Photograph", "しゃしん", "shashin", "写真"), Question("Flower", "はな", "hana", "花"), Question("Term Paper", "レポート", "repooto"), 
                     Question("Rice/Meal", "ごはん", "gohan", "ご飯"), Question("Bread", "パン", "pan"), Question("Temple", "おてら", "otera", "お寺"), 
                     Question("Park", "こうえん", "kouen", "公園"), Question("Supermarket", "スーパー", "suupaa"), Question("Bus Stop", "バスてい", "basutei", "バス停"), 
                     Question("Hospital", "びょういん", "byouin", "病院"), Question("Hotel", "ホテル", "hoteru"), Question("Bookstore", "ほんや", "honya", "本屋"), 
                     Question("Town/City", "まち", "machi", "町"), Question("Resturant", "レストラン", "resutoran"), Question("Yesterday", "きのう", "kinou", "昨日"),
                     Question("Hours", "じかん", "jikan", "時間"), Question("One Hour", "いちじかん", "ichijikan", "一時間"), Question("Last Week", "せんしゅう", "senshuu", "先週"),
                     Question("When/At The Time Of", "とき", "toki", "時"), Question("Monday", "げつように", "getsuyoubi", "月曜日"), Question("Tuesday", "かようび", "kayoubi", "火曜日"),
                     Question("Wednesday", "すいようび", "suiyoubi", "水曜日"), Question("Thursday", "もくようび", "mokuyoubi", "木曜日"), 
                     Question("Friday", "きんようび", "kinyoubi", "金曜日"), Question("To Meet/To See", "あう", "au", "会う", context="To Meet A Person"), Question("There Is", "ある", "aru"),
                     Question("To Buy", "かう", "kau", "買う"), Question("To Write", "かく", "kaku", "書く"), Question("To Take", "とる", "toru", "撮る", context="To Take a Picture"), 
                     Question("To Wait", "まつ", "matsu", "待つ"), Question("To Understand", "わかる", "wakaru"), Question("About", "ぐらい", "gurai"), 
                     Question("I'm Sorry", "ごめんなさい", "gomenasai"), Question("And Then", "それから", "sorekara"), Question("So/Therefore", "だから", "dakara"), 
                     Question("Many/A Lot", "たくさん", "takusan"), Question("Together With/And", "と", "to"), Question("Why", "どうして", "doushite"), 
                     Question("Alone", "ひとりで", "hitoride", "一人で"), Question("Hello", "もしもし", "moshimoshi", context="Phone"), Question("Right", "みぎ", "migi", "右"), 
                     Question("Left", "ひだり", "hidari", "左"), Question("Front", "まえ", "mae", "前"), Question("Back", "うしろ", "ushiro", "後ろ"), 
                     Question("Inside", "なか", "naka", "中"), Question("On", "うえ", "ue", "上"), Question("Under/Below", "した", "shita", "下"), 
                     Question("Near/Nearby", "ちかく", "chikaku", "近く"), Question("Next", "となり", "tonari", "隣"), Question("Between", "あいだ", "aida", "間") ]

    # Chapter 5 Vocab. Located on Genki page 130-131.
    chapter5Vocab = [ Question("Food", "たべもの", "tabemono", "食べ物"), Question("Drink", "のみもの", "nomimono", "飲み物"), Question("Fruit", "くだもの", "kudamono", "果物"), 
                     Question("Holiday/Day Off/Absense", "やすみ", "yasumi", "休み"), Question("Sea", "うみ", "umi", "海"), Question("Surfing", "サーフィン", "saafin"), 
                     Question("Souvenir", "おみやげ", "omiyage", "お土産"), Question("Bus", "バス", "basu"), Question("Weather", "てんき", "tenki", "天気"), 
                     Question("Homework", "しゅくだい", "shukudai", "宿題"), Question("Test", "テスト", "tesuto"), Question("Birthday", "たんじょうび", "tanjoubi", "誕生日"), 
                     Question("Room", "へや", "heya", "部屋"), Question("I", "ぼく", "boku", "僕", context="Used By Men"), Question("Size L", "Lサイズ", ["lsaizu", "エルサイズ", "erusaizu"]),
                     Question("New", "あたらしい", "atarashii", "新しい"), Question("Old", "ふるい", "furui", "古い", context="Things - Not Used For People"), 
                     Question("Hot", "あつい", "atsui", "暑い", context="Weather"), Question("Cold", "さむい", "samui", "寒い", context="Weather"), 
                     Question("Hot", "熱い", "atsui", "熱い", context="Thing"), Question("Busy", "いそがしい", "isogashii", "忙しい", context="People/Days"), 
                     Question("Large", "おおきい", "ookii", "大きい"), Question("Small", "ちいさい", "chisai", "小さい"), Question("Interesting/Funny", "おもしろい", "omoshiroi", "面白い"),
                     Question("Boring", "つまらない", "tsumaranai"), Question("Easy", "やさしい", "yasashii", context="Problem"), Question("Kind", "やさしい", "yasashii", context="Person"), 
                     Question("Difficult", "むずかしい", "muzukashii", "難しい"), Question("Good-Looking", "かっこいい", "kakkoii"), Question("Frightening", "ぞわい", "kowai", "怖い"),
                     Question("Fun", "たのしい", "tanoshii", "楽しい"), Question("Inexpensive/Cheap", "やすい", "yasui", "安い", context="Thing"), 
                     Question("Fond Of/To Like", "すき", ["suki", "すきな", "sukina"], "好き"), Question("Disgusted With/To Dislike", "きらい", ["kirai", "きらいな", "kiraina"], "嫌いな"),
                     Question("Very Fond Of/To Love", "だいすき", ["daisuki", "だいすきな", "daisukina"], "大好き"), 
                     Question("To Hate", "だいきらい", ["daikirai", "だいきらいな", "daikiraina"], "大嫌い"), Question("Beautiful/Clean", "きれい", ["kirei", "きれいな", "kireina"]), 
                     Question("Healthy/Energetic", "げんき", ["genki", "げんきな", "genkina"], "元気"), Question("Quiet", "しずか", ["shizuka", "しずかな", "shizukana"], "静か"),
                     Question("Lively", "にぎやか", ["nigiyaka", "にぎやかな", "nigiyakana"]), Question("Not Busy/Free", "ひま", ["hima", "ひまな", "himana"], "暇", context="Time"),
                     Question("To Swim", "およぐ", "oyogu", "泳ぐ"), Question("To Ask", "きく", "kiku", "聞く"), Question("To Ride/To Board", "のる", "noru", "乗る"), 
                     Question("To Do/To Perform", "やる", "yaru"), Question("To Go Out", "でかける", "dekakeru", "出かける"), Question("Together", "いっしょに", "isshoni", "一緒に"),
                     Question("Extremely", "すごく", "sugoku"), Question("It's Okay/Not To Worry", "だいじょうぶ", "daijoubu", "大丈夫"), Question("Very", "とても", "totemo"),
                     Question("What Kind Of", "どんな", "donna"), Question("Counter For Flat Objects", "まい", "mai", "枚") ]

    print("Vocab Quiz (MLJP201)\n")
    print("\t1 Chapter 1 Vocabulary")
    print("\t2 Chapter 2 Vocabulary")
    print("\t3 Chapter 3 Vocabulary")
    print("\t4 Chapter 4 Vocabulary")
    vocabType = input("\n[+] What quiz would you like to take?: ")

    if vocabType == "1":
        vocabQuizPrompt(chapter1Vocab)
    elif vocabType == "2":
        vocabQuizPrompt(chapter2Vocab)
    elif vocabType == "3":
        vocabQuizPrompt(chapter3Vocab)
    elif vocabType == "4":
        vocabQuizPrompt(chapter4Vocab)
    elif vocabType == "5":
        vocabQuizPrompt(chapter5Vocab)

def hardVocabQuiz():
    """
    This function will start a quiz on vocab words I've taught myself
    or have learned from different sources. Most of the words here come
    from "Word of the Day" by JapanesePod101.com.

    :return: None
    """
    hardVocab = [ "" ]