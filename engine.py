from textblob import TextBlob

def analyze_lead(text):
    """
    Core AI logic: Categorizes text sentiment into business actions.
    """
    analysis = TextBlob(text)
    #Polarity ranges from -1.0 (very negative) to 1.0 (very positive)
    score = analysis.sentiment.polarity

    if score > 0.5:
        return "Warm Lead", "🔥 Immediate Follow-Up", score
    elif score < -0.1:
        return "At-Risk", "☎ Support Escalation", score
    else:
        return "Inquiry", "📩 Send Info Deck", score