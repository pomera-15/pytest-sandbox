import re
from openai import OpenAI

def gen_haiku(haiku_theme):
    """
    テーマに対して俳句を生成して返却する
    ひらがな以外が含まれる場合はエラーを返す
    """
    # OpenAi APIを呼び出す
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system", 
                "content": f"""次のテーマに対して日本語のひらがなで俳句を生成してください。
                [生成例1]テーマ:ミカン, 出力:ふゆのひに みかんのかおり へやみたす
                [生成例2]テーマ:ふじのやま, 出力:ふじのやま ゆきにかがやく あさのそら"""
            },
            {
                "role": "user", 
                "content": f"テーマ:{haiku_theme}, 出力:"
            }
        ]
    )
    haiku = completion.choices[0].message.content

    # フォーマットエラーをチェックする（ひらがな以外のときにエラーにする）
    if not re.fullmatch(r"[\u3041-\u3096\s]+", haiku):
        raise ValueError("生成された俳句にひらがな以外の文字が含まれています: " + haiku)

    # 生成した俳句を返却する
    return haiku


if __name__ == "__main__":
    print(gen_haiku(input()))