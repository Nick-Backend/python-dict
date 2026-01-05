def most_common_char(text: str) -> str:
    text = "kjhgfdghjklkjhgfghjkljhgfhjk"
    max_harf = text[0]

    for i in text:
        if text.count(i) > max_harf.count(max_harf)