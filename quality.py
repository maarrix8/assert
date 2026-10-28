def classify_score(score):
    if not isinstance (score, int) or isinstance(score, bool):
        return None
    if score  < 0 or score > 100 :
        return None
    if score >= 60:
        return "pass"
    return "fail"

#2
def normalize_status(text):
    if not isinstance(text, str):
        return None
    cleaned = text.strip().lower()
    if cleaned in ("pending", "pass", "fail"):
        return cleaned
    return None


#3
