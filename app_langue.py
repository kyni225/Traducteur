
import random
# Liste des 100 mots les plus courants en chinois avec leurs traductions en anglais et en français
mots = [
    {"chinese": "的", "english": "of", "french": "de"},
    {"chinese": "一", "english": "one", "french": "un"},
    {"chinese": "是", "english": "is", "french": "est"},
    {"chinese": "了", "english": "le", "french": "a"},
    {"chinese": "我", "english": "I", "french": "je"},
    {"chinese": "不", "english": "not", "french": "pas"},
    {"chinese": "人", "english": "person", "french": "personne"},
    {"chinese": "在", "english": "at", "french": "à"},
    {"chinese": "有", "english": "have", "french": "avoir"},
    {"chinese": "这", "english": "this", "french": "ce"},
    {"chinese": "中", "english": "middle", "french": "milieu"},
    {"chinese": "大", "english": "big", "french": "grand"},
    {"chinese": "来", "english": "come", "french": "venir"},
    {"chinese": "上", "english": "up", "french": "haut"},
    {"chinese": "国", "english": "country", "french": "pays"},
    {"chinese": "和", "english": "and", "french": "et"},
    {"chinese": "地", "english": "earth", "french": "terre"},
    {"chinese": "到", "english": "arrive", "french": "arriver"},
    {"chinese": "以", "english": "by", "french": "par"},
    {"chinese": "说", "english": "say", "french": "dire"},
    {"chinese": "时", "english": "time", "french": "temps"},
    {"chinese": "要", "english": "want", "french": "vouloir"},
    {"chinese": "就", "english": "then", "french": "alors"},
    {"chinese": "出", "english": "exit", "french": "sortir"},
    {"chinese": "会", "english": "can", "french": "savoir"},
    {"chinese": "可", "english": "can", "french": "pouvoir"},
    {"chinese": "也", "english": "also", "french": "aussi"},
    {"chinese": "你", "english": "you", "french": "tu"},
    {"chinese": "对", "english": "correct", "french": "correct"},
    {"chinese": "生", "english": "life", "french": "vie"},
    {"chinese": "能", "english": "able", "french": "capable"},
    {"chinese": "而", "english": "and", "french": "et"},
    {"chinese": "子", "english": "child", "french": "enfant"},
    {"chinese": "得", "english": "get", "french": "obtenir"},
    {"chinese": "于", "english": "in", "french": "dans"},
    {"chinese": "着", "english": "continuous", "french": "en train de"},
    {"chinese": "下", "english": "down", "french": "bas"},
    {"chinese": "自", "english": "self", "french": "soi"},
    {"chinese": "年", "english": "year", "french": "année"},
    {"chinese": "过", "english": "pass", "french": "passer"},
    {"chinese": "发", "english": "send", "french": "envoyer"},
    {"chinese": "后", "english": "after", "french": "après"},
    {"chinese": "作", "english": "do", "french": "faire"},
    {"chinese": "里", "english": "inside", "french": "dedans"},
    {"chinese": "用", "english": "use", "french": "utiliser"},
    {"chinese": "道", "english": "road", "french": "route"},
    {"chinese": "行", "english": "go", "french": "aller"},
    {"chinese": "所", "english": "place", "french": "endroit"},
    {"chinese": "然", "english": "so", "french": "alors"},
    {"chinese": "家", "english": "home", "french": "maison"},
    {"chinese": "种", "english": "kind", "french": "genre"},
    {"chinese": "事", "english": "thing", "french": "chose"},
    {"chinese": "成", "english": "become", "french": "devenir"},
    {"chinese": "方", "english": "direction", "french": "direction"},
    {"chinese": "多", "english": "many", "french": "beaucoup"},
    {"chinese": "经", "english": "pass through", "french": "traverser"},
    {"chinese": "十", "english": "ten", "french": "dix"},
    {"chinese": "六", "english": "six", "french": "six"},
    {"chinese": "无", "english": "none", "french": "aucun"},
    {"chinese": "知", "english": "know", "french": "savoir"},
    {"chinese": "对", "english": "correct", "french": "correct"},
    {"chinese": "其", "english": "its", "french": "son"},
    {"chinese": "者", "english": "one who", "french": "celui qui"},
    {"chinese": "得", "english": "get", "french": "obtenir"},
    {"chinese": "让", "english": "let", "french": "laisser"},
    {"chinese": "长", "english": "long", "french": "long"},
    {"chinese": "现", "english": "appear", "french": "apparaître"},
    {"chinese": "下", "english": "next", "french": "prochain"},
    {"chinese": "先", "english": "first", "french": "premier"},
    {"chinese": "清", "english": "clear", "french": "clair"},
    {"chinese": "当", "english": "when", "french": "quand"},
    {"chinese": "应", "english": "should", "french": "devrait"},
    {"chinese": "非", "english": "not", "french": "pas"},
    {"chinese": "还", "english": "still", "french": "encore"},
    {"chinese": "先", "english": "first", "french": "premier"},
    {"chinese": "心", "english": "heart", "french": "cœur"},
    {"chinese": "里", "english": "in", "french": "dans"},
    {"chinese": "日", "english": "day", "french": "jour"},
    {"chinese": "个", "english": "measure word", "french": "compteur"},
    {"chinese": "当", "english": "act as", "french": "agir comme"},
    {"chinese": "明", "english": "bright", "french": "clair"},
    {"chinese": "世", "english": "world", "french": "monde"},
    {"chinese": "话", "english": "word", "french": "mot"},
    {"chinese": "时", "english": "time", "french": "temps"},
    {"chinese": "制", "english": "system", "french": "système"},
    {"chinese": "然", "english": "naturally", "french": "naturellement"},
    {"chinese": "产", "english": "produce", "french": "produire"},
    {"chinese": "图", "english": "image", "french": "image"},
    {"chinese": "新", "english": "new", "french": "nouveau"},
    {"chinese": "次", "english": "next", "french": "suivant"}
]


def quiz_user(mots):
    random.shuffle(mots)
    score = 0

    for mot in mots:
        print(f"quel est la traduiction du mots en '{mot['chinese']}' en Anglais ")
        user_answer = input("votre reponse :").strip().lower()
        correct_answer = mot['english'].lower()

        if user_answer == correct_answer:
            print("Correct!!\n!")
            score += 1
        else:
            print(f"incorrect! réessais! La bonne reponse c'est:'{mot['english']}'.\n")

    print(f"Fin de test! ton score : {score}/{len(mots)}")

    for mot in mots:
        print(f"quel est la traduiction du mots en '{mot['english']}' en Français")
        user_answer = input("votre reponse :").strip().lower()
        correct_answer = mot['french'].lower()
        
        if user_answer == correct_answer:
            print("Correct!!\n!")
            score += 1
        else:
            print(f"incorrect! réessais! La bonne reponse c'est:'{mot['french']}'.\n")

    print(f"Fin de test! ton score : {score}/{len(mots)}")


def main():
    
    print("Bienvenu sur l'application d'appentissage de langue")
    input("presse Start pour commencez ...")
    quiz_user(mots)


if __name__ == "__main__":
   main()
