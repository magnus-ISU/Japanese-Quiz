"""
Japanese Questions v1.0

author: Parker J Swierzewski
language: python3
desc: This program contains the questions that japanese_quiz.py will utilize.
"""
import random   # Used to randomly shuffle question.

class Question:
    """
    Used to define questions.
    """
    def __init__(self, question, correctAnswer, alternateAnswers):
        """
        This function is used to create a Question object.

        :param self: The object.
        :param question: The question prompt.
        :param correctAnswer: The best, or correct answer. 
        :param alternateAnswers: Other accepted answers.
        """
        self.question = question
        self.correctAnswer = correctAnswer
        self.alternateAnswers = alternateAnswers

    def isAlternate(self, response):
        """
        This function is used to determine whether the user entered the
        alternate answer.

        :param response: The user's response.
        :return: Boolean Flag (True = Correct)
        """
        if self.alternateAnswers is not None:
            if type(self.alternateAnswers) == list and response.lower() in self.alternateAnswers:
                return True
            elif type(self.alternateAnswers) == str and response.lower() == self.alternateAnswers:
                return True
        return False

    def correct(self, answer):
        """
        A pointless function to tell the user
        that they got the answer correct.

        :param self: The question object.
        :param answer: The answer the user submitted.
        :return: None
        """
        print("Correct! :)")

        if self.alternateAnswers is not None:
            if type(self.alternateAnswers) == list and len(self.alternateAnswers) > 1 and isHiragana(answer):
                print("The Kanji (漢字) for this word is {}".format(self.alternateAnswers[len(self.alternateAnswers)-1]))

    def incorrect(self):
        """
        A pointless function to tell the user
        that they got the answer incorrect.

        :param self: The question object.
        :return: None
        """
        print("Incorrect! :/")
        print("The correct answer was {}".format(self.correctAnswer))
        
        if self.alternateAnswers is not None:
            if type(self.alternateAnswers) == list:
                print("{} were also accepted answers!".format(self.alternateAnswers))
            else:
                print("{} was also an accepted answers!".format(self.alternateAnswers))

    def reverseQuestion(self, quizType):
        """
        This function is used to reverse the question and the answer
        so that the quiz is always changing and keeping the user
        on the spot.

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
            if type(self.alternateAnswers) == list and len(self.alternateAnswers) > 1:
                a += "(" + self.alternateAnswers[len(self.alternateAnswers)-1] + ")"
            self.question = a
            self.correctAnswer = q
            self.alternateAnswers = None

def calculateScore(score, max_score):
    """
    This function is used to print the score the
    user received.

    :param score: The score the user received.
    :param max_score: The max score for the quiz.
    :return: None
    """
    print("\n[!] Congrats you scored {:03.2f}!".format((score/max_score)*100))
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
    flag = input("Do you have a Japanese keyboard installed? (y/n): ")

    if flag.lower() == "y":
        flag = True
        print("[!] You will be asked to type in Japanese Writing Script(s) and Romaji!")
        wait = input("[!] Please get your Japanese keyboard setup and enter `y` when ready: ")
        
        while wait.lower() != "y":
            wait = input("[!] Please get your Japanese keyboard setup and enter `y` when ready: ")
            continue
            
    elif flag.lower() == "n":
        flag = False
        print("[!] You will only be asked to type Romaji!")
        print("[!] Set up a Japanese keyboard for the full experience! :)")
    else:
        print("[!] You must answer yes (y) or no (n)! Rerun to try again.")
        exit(1)

    return flag

def hiraganaQuiz():
    """
    This function is for the Hiragana Quiz. You'll only be tested on
    Hiragana characters. You'll either need to enter the Hiragana
    Character or write the Romaji (romanized version, i.e. だ = da).

    :return: None
    """
    print("Hiragana Quiz\n")
    hasJapaneseKeyboard

    hiragana = [ Question("あ", "a", None), Question("い", "i", None), Question("う", "u", None), Question("え", "e", None), Question("お", "o", None),
                    Question("か", "ka", None), Question("き", "ki", None), Question("く", "ku", None), Question("け", "ke", None), Question("こ", "ko", None),
                    Question("が", "ga", None), Question("ぎ", "gi", None), Question("ぐ", "gu", None), Question("げ", "ge", None), Question("ご", "go", None),
                    Question("さ", "sa", None), Question("し", "shi", None), Question("す", "su", None), Question("せ", "se", None), Question("そ", "so", None),
                    Question("ざ", "za", None), Question("じ", "ji", None), Question("ず", "zu", None), Question("ぜ", "ze", None), Question("ぞ", "zo", None),
                    Question("た", "ta", None), Question("ち", "chi", None), Question("つ", "tsu", None), Question("て", "te", None), Question("と", "to", None),
                    Question("だ", "da", None), Question("ぢ", "ji", None), Question("づ", "zu", None), Question("で", "de", None), Question("ど", "do", None),
                    Question("な", "na", None), Question("に", "ni", None), Question("ぬ", "nu", None), Question("ね", "ne", None), Question("の", "no", None),
                    Question("は", "ha", None), Question("ひ", "hi", None), Question("ふ", "fu", "hu"), Question("へ", "he", None), Question("ほ", "ho", None),
                    Question("ば", "ba", None), Question("び", "bi", None), Question("ぶ", "bu", None), Question("べ", "be", None), Question("ぼ", "bo", None),
                    Question("ぱ", "pa", None), Question("ぴ", "pi", None), Question("ぷ", "pu", None), Question("ぺ", "pe", None), Question("ぽ", "po", None),
                    Question("ま", "ma", None), Question("み", "mi", None), Question("む", "mu", None), Question("め", "me", None), Question("も", "mo", None),
                    Question("や", "ya", None), Question("ゆ", "yu", None), Question("よ", "yo", None), 
                    Question("ら", "ra", None), Question("り", "ri", None), Question("る", "ru", None), Question("れ", "re", None), Question("ろ", "ro", None),
                    Question("わ", "wa", None), Question("を", "wo", "o"), 
                    Question("ん", "n", None) ]

    input("\nThe quiz is about to begin! Press any key to start...")
    score = 0
    max_score = len(hiragana)

    random.shuffle(hiragana)
    for element in hiragana:
        print("\n" + element.question)
        answer = input("What character is this?: ")

        if (answer.lower() == element.correctAnswer.lower()) or element.isAlternate(answer):
            element.correct()
            score += 1
        else:
            element.incorrect()

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

    katakana = [ Question("ア", "a", None), Question("イ", "i", None), Question("ウ", "u", None), Question("エ", "e", None), Question("オ", "o", None),
                    Question("カ", "ka", None), Question("キ", "ki", None), Question("ク", "ku", None), Question("ケ", "ke", None), Question("コ", "ko", None),
                    Question("ガ", "ga", None), Question("ギ", "gi", None), Question("グ", "gu", None), Question("ゲ", "ge", None), Question("ゴ", "go", None),
                    Question("サ", "sa", None), Question("シ", "shi", None), Question("ス", "su", None), Question("セ", "se", None), Question("ソ", "so", None),
                    Question("ザ", "za", None), Question("ジ", "ji", None), Question("ズ", "zu", None), Question("ゼ", "ze", None), Question("ゾ", "zo", None),
                    Question("タ", "ta", None), Question("チ", "chi", None), Question("ツ", "tsu", None), Question("テ", "te", None), Question("ト", "to", None),
                    Question("ダ", "da", None), Question("ヂ", "ji", None), Question("ヅ", "zu", None), Question("デ", "de", None), Question("ド", "do", None),
                    Question("ナ", "na", None), Question("ニ", "ni", None), Question("ヌ", "nu", None), Question("ネ", "ne", None), Question("ノ", "no", None),
                    Question("ハ", "ha", None), Question("ヒ", "hi", None), Question("フ", "fu", "hu"), Question("ヘ", "he", None), Question("ホ", "ho", None),
                    Question("バ", "ba", None), Question("ビ", "bi", None), Question("ブ", "bu", None), Question("べ", "be", None), Question("ボ", "bo", None),
                    Question("パ", "pa", None), Question("ピ", "pi", None), Question("プ", "pu", None), Question("ぺ", "pe", None), Question("ポ", "po", None),
                    Question("マ", "ma", None), Question("ミ", "mi", None), Question("ム", "mu", None), Question("メ", "me", None), Question("モ", "mo", None),
                    Question("ヤ", "ya", None), Question("ユ", "yu", None), Question("ヨ", "yo", None), 
                    Question("ラ", "ra", None), Question("リ", "ri", None), Question("ル", "ru", None), Question("レ", "re", None), Question("ロ", "ro", None),
                    Question("ワ", "wa", None), Question("ヲ", "wo", "o"), 
                    Question("ン", "n", None) ]

    input("\nThe quiz is about to begin! Press any key to start...")
    score = 0
    max_score = len(katakana)

    random.shuffle(katakana)
    for element in katakana:
        print("\n" + element.question)
        answer = input("What character is this?: ")

        if (answer.lower() == element.correctAnswer.lower()) or element.isAlternate(answer):
            element.correct(answer)
            score += 1
        else:
            element.incorrect()

    calculateScore(score, max_score)

def startHomeworkVocabQuiz():
    """
    This function will start a quiz based on words/phrases given in the
    homework. The user will get to choose what chapater they want to be
    quizzed from.

    :return: None
    """
    # This section contains questions from MLJP201 (Beginner Japanese I).
    beginnerVocab = [ Question("Waterfall", "たき", ["taki", "滝"]), Question("Moon", "つき", ["tsuki", "月"]), Question("Near", "ちかい", ["chikai", ""]), 
                     Question("Enemy", "てき", ["teki", ""]), Question("Land", "とち", ["tochi", ""]), Question("Important", "だいじ", ["daiji", ""]), 
                     Question("Toxic Mouth", "どくが", ["dokuga", ""]), Question("Elbow", "うで", ["ude", ""]), Question("Forehead", "おでこ", ["odeko", ""]),
                     Question("Something Continues", "つずく", ["tsuzuku", ""]) ]

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
            print("\n" + element.question)
            answer = input("What is the Japanese for the word above?: ")

            if (answer.lower() == element.correctAnswer) or element.isAlternate(answer):
                element.correct(answer)
                score += 1
            else:
                element.incorrect()
        else:
            element.reverseQuestion("Vocab")

            print("\n" + element.question)
            answer = input("What is the English for the word above?: ")

            # Some words have multiple meanings in English.
            # The next few lines below account for that.
            c = element.correctAnswer.lower().split("/")

            if (answer.lower() in c):
                element.correct(answer)
                score += 1
            else:
                element.incorrect()
        
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
    chapter1Vocab = [ Question("College/University", "だいがく", ["daigaku", "だいがく"]), Question("High School", "こうこう", ["koukou", "高校生"]), 
                     Question("Student", "がくせい", ["gakusei", "学生"]), Question("College Student", "だいがくせい", ["daigakusei", "大学生"]), 
                     Question("International Student", "りゅうがくせい", ["ryuugakusei", "留学生"]), Question("Teacher/Professor", "せんせい", ["sensei", "先生"]), 
                     Question("First Year Student", "いちねんせい", ["ichinensei", "一年生"]), Question("Major", "せんこう", ["senkou", "専攻"]), Question("I", "わたし", ["watashi", "私"]), 
                     Question("Friend", "ともだち", ["tomodachi", "友達"]), Question("Mr/Ms", "さん", "san"), Question("Japanese People", "にほんじん", ["nihonjin", "日本人"]),
                     Question("Now", "いま", ["ima", "今"]), Question("AM", "ごぜん", ["gozen", "午前"]), Question("PM", "ごご", ["gogo", "午後"]), Question("O'Clock", "じ", ["ji", "時"]),
                     Question("One O'Clock", "いちじ", ["ichiji", "一時"]), Question("Half", "はん", ["han", "半"]), Question("2:30", "にじはん", ["nijihan", "二時半"]), 
                     Question("Japan", "にほん", ["nihon", "日本"]),  Question("America/USA", "アメリカ", "amerika"),  Question("Language", "ご", ["go", "語"]),  
                     Question("Japanese Language", "にほんご", ["nihongo", "日本語"]),  Question("Years Old", "さい", ["sai", "歳"]),  Question("Telephone/Phone", "でんわ", ["denwa", "電話"]),  
                     Question("Number", "ばんごう", ["bangou", "番号"]),  Question("Name", "なまえ", ["namae", "名前"]),  Question("What", "なん", ["nan", "nani", "なに", "何"]),
                     Question("Um", "あの", "ano"), Question("Yes", "はい", "hai"), Question("That's Right", "そうです", "soudesu"), Question("I See/Is That So", "そうですか", "soudesuka"),
                     Question("Britian", "イギリス", "igirisu"), Question("Australia", "オーストラリア", "oosutoraria"), Question("Korea", "かんこく", ["kankoku", "韓国"]),
                     Question("China", "ちゅうごく", ["chuugoku", "中国"]), Question("India", "インド", "indo"), Question("Egypt", "エジプト", "ejiputo"), 
                     Question("Philippines", "フィリピン", "firipin"), Question("Asian Studies", "アジアけんきゅう", ["ajiakenkyuu", "アジア研究"]), 
                     Question("Economics", "けいざい", ["keizai", "経済"]), Question("Engineering", "こうがく", "kougaku"), 
                     Question("International Relations", "こくさいかんけい", ["kakusaikankei", "国際関係"]), Question("Computer", "コンピュータ", "konpyuuta"), 
                     Question("Politics", "せいじ", "政治"), Question("Biology", "せいぶつがく", ["seibutsugaku", "生物学"]), Question("Business", "ビジネス", "bijinesu"),
                     Question("Literature", "ぶんがく", ["bungaku", "文学"]), Question("History", "れきし", ["rekishi", "歴史"]), Question("Doctor", "いしゃ", ["isha", "医者"]), 
                     Question("Office Worker", "かいしゃいん", ["kaishain", "会社員"]), Question("Nurse", "かんごし", ["kangoshi", "看護師"]), 
                     Question("High School Student", "こうこうせい", ["koukousei", "高校生"]), Question("Housewife", "しゅふ", ["shufu", "主婦"]), 
                     Question("Graduate Student", "だいがくいんせい", ["daigakuinsee", "大学院生"]), Question("Lawyer", "べんごし", ["bengoshi", "弁護士"]), 
                     Question("Mother", "おかあさん", ["okaasan", "お母さん"]), Question("Father", "お父さん", ["otousan", "お父さん"]), 
                     Question("Older Sister", "おねえさん", ["oneesan", "お姉さん"]), Question("Older Brother", "おにいさん", ["oniisan", "お兄さん"]), 
                     Question("Younger Sister", "いもうと", ["imouto", "妹"]), Question("Younger Brother", "おとうと", ["otouto", "弟"]), ]

    # Chapter 2 Vocab. Located on Genki page 58-69.
    chapter2Vocab = []

    # Chapter 3 Vocab. Located on Genki page 84-85.
    chapter3Vocab = [ Question("Movie", "えいが", ["eiga", "映画"]), Question("Music", "おんがく", ["ongaku", "音楽"]), Question("Magazine", "ざっし", ["zasshi", "雑誌"]),
                     Question("Sports", "スポーツ", "supaatsu"), Question("Date (Romantic)", "デート", "deeto"), Question("Tennis", "テニス", "tenisu"), Question("TV", "テリビ", "teribi"),
                     Question("Ice Cream", "アイスクリーム", "aisukariimu"), Question("Hamburger", "ハンバーガー", "hanbaagaa"), Question("Sake/Alcohol", "おさけ", ["osake", "お酒"]),
                     Question("Green Tea/Tea", "おちゃ", ["ocha", "お茶"]), Question("Coffee", "コーヒー", "koohii"), Question("Water", "みず", ["mizu", "水"]),
                     Question("Breakfast", "あさごはん", ["asagohan", "朝ご飯"]), Question("Lunch", "ひるごはん", ["hirugohan", "昼ご飯"]),
                     Question("Dinner", "ばんごはん", ["bangohan", "晩ご飯"]), Question("Home/House/My Place", "いえ", ["ie", "uchi", "うち", "家"]), 
                     Question("School", "がっこう", ["gakkou", "学校"]), Question("Cafe", "カフェ", "cafe"), Question("Tomorrow", "あした", ["ashita", "明日"]),
                     Question("Today", "きょう", ["kyou", "きょう"]), Question("Morning", "あさ", ["asa", "朝"]), Question("Tonight", "こんばん", ["konban", "今晩"]),
                     Question("Every Day", "まいにち", ["mainichi", "毎日"]), Question("Every Night", "まいばん", ["maiban", "毎晩"]),
                     Question("Weekend", "しゅうまつ", ["shuumatsu", "週末"]), Question("Saturday", "どようび", ["doyoubi", "土曜日"]), 
                     Question("Sunday", "にちようび", ["nichiyoubi", "日曜日"]), Question("When", "いつ", "itsu"), Question("At About / Around", "ごろ", "goro"), 
                     Question("To Go", "いく", ["iku", "行く"]), Question("To Go Back/To Return", "かえる", ["kaeru", "帰る"]), Question("To Listen/To Hear", "きく", ["kiku", "聞く"]),
                     Question("To Drink", "のむ", ["nomu", "飲む"]), Question("To Speak/To Talk", "はなす", ["hanasu", "話す"]), Question("To Read", "よむ", ["yomu", "読む"]),
                     Question("To Get Up", "おきる", ["okiru", "起きる"]), Question("To Eat", "たべる", ["taberu", "食べる"]), Question("To Sleep/To Go To Sleep", "ねる", ["neru", "寝る"]),
                     Question("To See/To Look At/To Watch", "みる", ["miru", "見る"]), Question("To Come", "くる", ["kuru", "来る"]), Question("To Do", "する", "suru"),
                     Question("To Study", "べんきょうする", ["benkyoushiru", "勉強する"]), Question("Good", "いい", "ii"), Question("Early", "はやい", ["hayai", "早い"]),
                     Question("Not Much", "あまり", "amari"), Question("Not At All", "ぜんぜん", ["zenzen", "全然"]), Question("Usually", "たいてい", "taitei"),
                     Question("A Little", "ちょっと", "chyotto"), Question("Sometimes", "ときどき", ["tokidoki", "時々"]), Question("Often/Much", "よく", "yoku"),
                     Question("That's Right/Let Me See", "そうですね", "soudesune"), Question("But", "でも", "demo"), Question("How About...?/How Is...?", "どうですか", "doudesuka"), 
                     Question("Yes (Casual)", "ええ", "ee") ]

    # Chapter 4 Vocab. Located on Genki page 104-106.
    chapter4Vocab = [ Question("Game", "ゲーム", ["geemu"]), Question("Part-Time Job", "アルバイト", ["arubaito", "バイト"]), Question("Shopping", "かいもの", ["kaimono", "買い物"]),
                     Question("Class", "クラス", "kurasu"), Question("Dog", "いぬ", ["inu", "犬"]), Question("Cat", "ねこ", ["neko", "猫"]), Question("Person", "ひと", ["hito", "人"]),
                     Question("Child", "こども", ["kodomo", "子供"]), Question("You", "あなた", "anata"), Question("Chair", "いす", "isu"), Question("Desk", "つくえ", ["tsukue", "机"]),
                     Question("Picture/Photohraph", "じゃしん", ["jashin", "邪神"]), Question("Flower", "はな", ["hana", "花"]), Question("Term Paper", "レポート", "repooto"), 
                     Question("Rice/Meal", "ごはん", ["gohan", "ご飯"]), Question("Bread", "パン", "pan"), Question("Temple", "おてら", ["otera", "お寺"]), 
                     Question("Park", "こうえん", ["kouen", "公園"]), Question("Supermarket", "スーパー", "suupaa"), Question("Bus Stop", "バスてい", ["basutei", "バス停"]), 
                     Question("Hospital", "びょういん", ["byouin", "病院"]), Question("Hotel", "ホテル", "hoteru"), Question("Bookstore", "ほんや", ["honya", "本屋"]), 
                     Question("Town/City", "まち", ["machi", "町"]), Question("Resturant", "レストラン", "resutoran"), Question("Yesterday", "きのう", ["kinou", "昨日"]),
                     Question("Hours", "じかん", ["jikan", "時間"]), Question("One Hour", "いちじかん", ["ichijikan", "一時間"]), Question("Last Week", "せんしゅう", ["senshuu", "先週"]),
                     Question("When/At The Time Of", "とき", ["toki", "時"]), Question("Monday", "げつように", ["getsuyoubi", "月曜日"]), Question("Tuesday", "かようび", ["kayoubi", "火曜日"]),
                     Question("Wednesday", "すいようび", ["suiyoubi", "水曜日"]), Question("Thursday", "もくようび", ["mokuyoubi", "木曜日"]), 
                     Question("Friday", "きにょうび", ["kinyoubi", "金曜日"]), Question("To Meet A Person/To See A Person", "あう", ["au", "会う"]), Question("There Is", "ある", "aru"), 
                     Question("To Buy", "かう", ["kau", "買う"]), Question("To Write", "かく", ["kaku", "書く"]), Question("To Take A Picture", "とる", ["toru", "撮る"]), 
                     Question("To Wait", "まつ", ["matsu", "待つ"]), Question("To Understand", "わかる", "wakaru"), Question("About", "ぐらい", "gurai"), 
                     Question("I'm Sorry", "ごめんなさい", "gomenasai"), Question("And Then", "それから", "sorekara"), Question("So/Therefore", "だから", "dakara"), 
                     Question("Many/A Lot", "たくさん", "takusan"), Question("Together With/And", "と", "to"), Question("Why", "どうして", "doushite"), 
                     Question("Alone", "ひとりで", ["hitoride", "一人で"]), Question("Hello?", "もしもし", "moshimoshi"), Question("Right", "みぎ", ["migi", "右"]), 
                     Question("Left", "ひだり",  ["hidari", "ひだり"]), Question("Front", "まえ",  ["mae", "前"]), Question("Back", "うしろ",  ["ushiro", "後ろ"]), 
                     Question("Inside", "なか",  ["naka", "中"]), Question("On", "うえ",  ["ue", "上"]), Question("Under", "した",  ["shita", "下"]), 
                     Question("Near/Nearby", "ちかく", ["chikaku", "近く"]), Question("Next", "となり", ["tonari", "隣"]), Question("Between", "あいだ",  ["aida", "間"]) ]

    print("Vocab Quiz (MLJP201)\n")
    print("\t1 Chapter 1 Vocabulary")
    print("\t2 Chapter 2 Vocabulary")
    print("\t3 Chapter 3 Vocabulary")
    print("\t4 Chapter 4 Vocabulary")
    vocabType = input("\n[+] What quiz would you like to take?: ")

    if vocabType == "1":
        vocabQuizPrompt(chapter1Vocab)
    elif vocabType == "2":
        pass
    elif vocabType == "3":
        vocabQuizPrompt(chapter3Vocab)
    elif vocabType == "4":
        vocabQuizPrompt(chapter4Vocab)

def hardVocabQuiz():
    """
    This function will start a quiz on vocab words I've taught myself
    or have learned from different sources. Most of the words here come
    from "Word of the Day" by JapanesePod101.com.

    :return: None
    """
    hardVocab = [ "" ]