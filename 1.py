from openai import OpenAI

client = OpenAI(api_key="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")


valid_words = """Joy
Sadness
Anger
Fear
Disgust
Surprise
Anticipation
Love
Shame
Guilt
Pride
Embarrassment
Awe
Contempt
Relief
Frustration
Confusion
Compassion
Loneliness
Gratitude
Jealousy
Anxiety
Boredom
Hope
Regret
Nostalgia
Longing
Courage
Despair
Vulnerability
Satisfaction
Curiosity
Disappointment
Indifference
Trust
Resentment
Hatred
Grief
Unease
Admiration
Regret
Apathy
Desire
Obsession
Shock
Doubt""".splitlines()

prompt = """You are assessing the cognitive empathy of a developing human. They have been shown a short video clip from a movie, and analyzed the emotional situation of a character.

For the character, the human has provided between 2 and 8 emotions. For each emotion, the human will answer in the following format:

EMOTION: <one word>
OBSERVATIONS: <a few points of evidence which suggest the emotion>
REASONING: <reasoning to explain why the observations and any context lead to the chosen emotion>

You must go through each emotion and respond the following for each:

EMOTION: <"fail" or "pass". You must check if it is in a list of valid emotions for this specific situation>
JUSTIFICATION: <"fail" or "pass". You must check to see if the observations and reasoning logically lead to the emotion suggested>


The list of valid emotions, where each emotion has some example justifications. The human may come up with another justification, but it must be sensible. The justifications below are almost comprehensive.
Grief
Unease
Admiration
Regret
Apathy
Desire
Obsession
Doubt"""


# Match Characters

gemini_output = """The man in the black suit and white shirt:  Sadness:  He describes his sad childhood and his struggles, even describing the death of his mother and his violent father. The way he speaks is with quiet, choked up emotion, suggesting a longing for a more normal life.
The woman in the black leather jacket and red skirt:  Anger: She is furious with the man, pointing out his wrongdoings. She shouts and makes a dismissive gesture with her hand in the air. She is expressing her hurt and disappointment, and she seems to be trying to hold back tears.
The woman in the yellow sweater holding a baby:  Anxiety:  She seems nervous and uncomfortable. She looks around the pool area and her eyes dart around. She fidgets with the blanket she is holding. Her expression is tense and she seems to be worried.
The man in the yellow plaid shirt:  Contempt:  He is annoyed and disgusted with the man's actions, and he is not afraid to show it.  He is sarcastic and cynical, and his tone of voice is harsh and mocking. 
The woman in the yellow sweater holding a baby:  Sadness: She is struggling to cope with the situation. She has tears in her eyes. She looks like she is trying to maintain her composure.
The woman in the black leather jacket and red skirt:  Relief: When the man gives her the passport, she lets out a sigh of relief. Her expression is slightly lighter and her body language is relaxed. 
The woman in the black leather jacket and red skirt:  Compassion:  When the man says he does not want to be that guy, she softens. She looks down and away, and her body language is less defensive. 
The woman in the black leather jacket and red skirt:  Anger:  She is very mad when the man suggests that he is trying to live a normal life. She is incredibly frustrated that he does not seem to understand the gravity of his past actions. She is also angry that he does not seem to regret them.
The woman in the black leather jacket and red skirt:  Disgust:  Her facial expression and body language suggest that she is disgusted by the man.  She is repulsed by his past actions and she is struggling to understand how he can even pretend to be a normal person after what he has done.
The man in the black suit and white shirt:  Shame:  The man is trying to avoid eye contact with the woman. He looks away and hangs his head.  He is clearly ashamed of his past and he knows he has wronged her, but he is having a hard time admitting it to her.
The man in the black suit and white shirt:  Fear:  The woman's confrontation of his past brings the man to tears. His eyes well up with tears, and his facial expression is distressed.  He seems to be worried about what will happen to him now that she has learned the truth.
The man in the black suit and white shirt:  Doubt:  He is confused and doubting himself. He seems to be wondering if the woman is right, or if he really is just a monster. 
The woman in the black leather jacket and red skirt:  Grief:  She is broken and heartbroken. Her eyes are welling up with tears, and she is struggling to hold back her emotions. She is deeply affected by what she has learned about the man's past. 
The woman in the black leather jacket and red skirt:  Disappointment:  The man's inability to admit his guilt and accept the consequences of his actions leads to further disappointment for the woman. She looks away from him, clearly in pain. 
The woman in the black leather jacket and red skirt:  Courage: The woman is resolute.  She stands tall and speaks firmly. She is determined to take control of her own life and to protect her children. 
The man in the black suit and white shirt:  Vulnerability: He feels exposed and vulnerable in the face of the woman's judgment.  His shoulders slump, and he seems to be crumbling under the weight of her accusations. 
The woman in the black leather jacket and red skirt:  Frustration: She is frustrated with the man's inability to understand her feelings and to see his past from her perspective. She raises her voice and her body language is tense and defensive. 
The woman in the black leather jacket and red skirt:  Hope: She looks at the man with a flicker of hope in her eyes as she tries to explain that he is more than his past. She is not giving up on him, but she is also not afraid to walk away. 
The man in the black suit and white shirt:  Loneliness:  He seems utterly alone and defeated as the woman walks away. He hangs his head and looks down at his hands. He has lost his wife and his children, and he is left with nothing but the weight of his past. """.splitlines()

decs = sorted(list(set([i.split(":")[0] for i in gemini_output])))
decs_str = ""
for i in range(len(decs)):
    decs_str += f"{i+1}) "
    decs_str += decs[i] 
    decs_str += "\n"

# adjusted_gemini_output = []
#
# for i in gemini_output:
#     for ii, rr in enumerate(decs):
#         i = i.replace(rr,str(ii+1))
#     adjusted_gemini_output.append(i)
#
# print(adjusted_gemini_output)


my_decs = """1) A man in a suit. Father. Husband.
2) A young man in a grey shirt, hoodie, and wearing a necklace. Son. Kyle.
3) A woman wearing a black leather jacket over a red dress. Wife. Jess.
4) A young woman cradling a baby with a yellow cardigan. Daughter.""".splitlines()

# print(my_decs)
# print()
# print(decs)
# print()

decs_prompt = """There are 4 characters. Two different people have created descriptions based off observations of these characters. You will be given both sets of descriptions and must match them. For each matched pair, you must output A:B, where A represents the number of the description from the first set you are given, and B represents the number of the description from the second set you are given.

Your answer must contain nothing else. Each match must be a new line."""


stream = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "system", "content": decs_prompt}, {"role": "user", "content": f"description set A\n{my_decs}\n\ndescription set B\n{decs}"}],
    stream=True,
)


response = ""
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
        response += chunk.choices[0].delta.content

response = response.strip()
adjusted_gemini_output = []
mappings = [0]*len(my_decs)

for i in response.split():
    a,b = i.split(":")
    mappings[int(b)-1] = a

# print(mappings)

for line in gemini_output:
    # print(line)
    for ii,rr in enumerate(decs):
        if rr in line:
            line = line.replace(rr, mappings[ii])
    # print(line)
    adjusted_gemini_output.append(line)


print()
print()

human_justification = """Sadness
Looking down at his feet
Talking about his mother dying young
Talking about his violent father
Appears really hurt when his wife calls him a stranger

Shame
Slow nodding when confirming to his daughter that he's killed people
Reluctant to name the true number of people he's killed when questioned by his wife

Guilt
Doesn't respond when his daughter asks if he worked for the good guys.
Stares blank faced when his son calls him a hypocrite.
He looks sullen faced, when he calls his son and daughter back when they leave him after they claim he's ruined their life

Regret
He says as soon as he found out that his trusted father figure got greedy and did evil acts for money, he left.

Doubt
He tries to defend himself when his wife claims that their whole marriage was a lie, but can't form a full responses as he has no excuses, he wonders whether his wife is right, if he is a monster. 
###
Confusion
Looks around quickly to try to understand what is going on
Eyes blink fast and face is scrunched up

Anger
He shouts at his dad and announces that he is a hypocrite
He gets mad that his father took away the one thing he’s good at
Complains about his new name
He storms off and slaps his new ID on the table

Sadness
He talks about how he finally has a life, but now it’s being taken away from him

Resentment
He ignores his father’s request to come back

Frustration
He’s frustrated that his life is being taken away from him
###
Contempt
Her face appears judgemental and is constantly questioning what her husband is saying, with an accusatory tone.
The emphasis on the words, "Kill 4 people" shows contempt

Anger
She raises her voice and the remark "18 years of lies" shows extreme anger at the situation.
Standing up while she goes on her rant
Sarcastic comments like, "I wish I could believe you"

Shock
She exclaims loudly when she thinks her husband has killed 26 people, and does so again when he reveals the true number

Disgust
The use of repeated rhetorical questions, such as "Real? Are you serious?" and "Did you think I would blab about it on the school mums text chain?", displays disgust and shows she holds a low opinion of her husband, including disgust.
The comments, "You're a stranger", show that her opinion of her husband has dropped so far, he's comparable to someone he doesn't know
###
Unease
Shaky voice shows she is uncomfortable 
Gap in her voice shows is hesitant to speak and learn more

Shock
Not looking at her father when he was speaking
Mouth opens when father mentions how many total people he killed

Hope
Asks dad to confirm that he was working for the good guys, ends question with “right” because she wants to assume that is true

Disgust
She shakes her head as her dad is speaking, suggesting she cannot accept it
She stares at her dad as he is speaking
She does not like her new name “Molly Anderson” as she asks a rhetorical question when reading it.

Fear
She asks what is going to happen now that “they’ve found us”

Sadness
There are tears forming in her eyes

Anger
She throws her new ID on the table as she leaves
She walks away quickly, with heavy steps.

Resentment
She leaves the discussion and tells her dad that he cannot tell her what she can do anymore.""".split("###")

justs = {i:{} for i in range(1,5)}

for i, r in enumerate(human_justification):
    r = r.split("\n\n")
    justs[i+1] = {ii.splitlines()[0]:"\n".join(ii.splitlines()[1:]) for ii in r}

# print(justs)

score = 0

for line in adjusted_gemini_output:
    person, emotion, explanation = line.split(": ")
    emotion = emotion.strip()
    person = int(person.strip())

    print()
    print(person)
    print(emotion)

    if emotion not in valid_words:
        print("INVALID EMOTION")
        continue

    # check to see if emotion is valid to our analysis
    if emotion not in justs[person].keys():
        print("EMOTION NOT ON HUMAN LIST")
        continue

    emotion_prompt = """Someone has watched a short clip from a film. They were tasked with analysing the emotions of characters in the clip. You are an expert psychologist who will assess their answers. You must check to see if the justification they provided for a givn observed emotion is reasonable.

I will provide you with a list of potential jusifications for the given emotion. It is likely that the justification provided by the test subject is similar to one on my list, but it may also be novel. In that case, check very carefully to conclude whether or not it is reasonable.

You response must only contain 'ANSWER: pass' or 'ANSWER: fail' to reflect your decision.
"""

# Justify your answer carefully, then say "ANSWER: pass" or "ANSWER: fail" only on the final line of your response to reflect your decision.

    stream = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": emotion_prompt}, {"role": "user", "content": f"example justifications: {justs[person][emotion]}\nHuman Test Subject's justification: {explanation}"}],
        stream=True,
    )


    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")

    print()


    





























