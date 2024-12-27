# Setting Up The Virtual Environment
# python -m venv .venv
# .venv\Scripts\activate

# Real Tarot Reading.py ---------------------------------------------------------------------------------------------------------------
import random



# The Major Arcana - The Fool's Journey
the_fool = "The Fool: Innocence, New Beginnings, Free Spirit"
the_fool_reversed = "The Fool Reversed: Recklessness, Taken Advantage Of, Inconsideration"
the_magician = "The Magician: Willpower, Desire, Creation, Manifestation"
the_magician_reversed = "The Magician Reversed: Trickery, Illusions, Out of Touch"
the_high_priestess = "The High Priestess: Intuitive, Unconscious, Inner Voice"
the_high_priestess_reversed = "The High Priestess Reversed: Lack of Center, Lost Inner Voice, Repressed Feelings"
the_empress = "The Empress: Motherhood, Fertility, Nature"
the_empress_reversed = "The Empress Reversed: Dependence, Smothering, Emptiness, Noisiness"
the_emperor = "The Emperor: Authority, Structure, Control, Fatherhood"
the_emperor_reversed = "The Emperor Reversed: Tyranny, Rigidity, Coldness"
the_hierophant = "The Hierophant: Institution, Tradition, Morality, Ethics"
the_hierophant_reversed = "The Hierophant Reversed: Rebellion, Subveriveness, New Approaches"
the_lovers = "The Lovers: Partnerships, Duality, Union"
the_lovers_reversed = "The Lovers Reversed: Loss of Balance, One-Sidedness, Disharmony"
the_chariot = "The Chariot: Control, Victory, Willpower"
the_chariot_reversed = "The Chariot Reversed: Lack of Control, Lack of Direction, Aggression"
strength = "Strength: Inner Strength, Bravery, Compassion, Focus"
strength_reversed = "Strength Reversed: Self-Doubt, Weakness, Insecurity"
the_hermit = "The Hermit: Contemplation, Search for Truth, Inner Guidance"
the_hermit_reversed = "The Hermit Reversed: Isolation, Loneliness, Lost Away"
the_wheel_of_fortune = "The Wheel of Fortune: Change, Cycles, Inevitable Fate"
the_wheel_of_fortune_reversed = "The Wheel of Fortune Reversed: No Control, Clinging to Control, Bad Luck"
justice = "Justice: Cause and Effect, Clarity, Truth"
justice_reversed = "Justice Reversed: Unfairness, Lack of Accountability, Dishonesty"
the_hanged_man = "The Hanged Man: Sacrifice, Release, Martyrdom"
the_hanged_man_reversed = "The Hanged Man Reversed: Stalling, Needless Sacrifice, Fear of Sacrifice"
death = "Death: End of Cycle, Beginnings, Change, Metamorphosis"
death_reversed = "Death Reversed: Fear of Change, Holding on, Stagnation, Decay"
temperance = "Temperance: Middle Path, Patience, Finding Meaning"
temperance_reversed = "Temperance Reversed: Extremes, Excess, Lack of Balance"
the_devil = "The Devil: Addiction, Materialism, Playfulness"
the_devil_reversed = "The Devil Reversed: Freedom, Release, Restoring Control"
the_tower = "The Tower: Sudden Upheaval, Broken Pride, Disaster"
the_tower_reversed = "The Tower Reversed: Disaster Avoided, Delayed Disaster, Fear of Sufferring"
the_star = "The Star: Hope, Faith, Rejuvenation"
the_star_reversed = "The Star Reversed: Faithlessness, Discouragement, Insecurity"
the_moon = "The Moon: Unconscious, Illusions, Intuition"
the_moon_reversed = "The Moon Reversed: Fear, Confusion, Misinterpretation"
the_sun = "The Sun: Joy, Success, Celebration, Positivity"
the_sun_reversed = "The Sun Reversed: Negativity, Depression, Sadness"
judgement = "Judgement: Reflection, Reckoning, Awakening"
judgement_reversed = "Judgement Reversed: Lack of Self-Awareness, Doubt, Self-Loathing"
the_world = "The World: Fullfillment, Harmony, Completion"
the_world_reversed = "The World Reversed: Incompletion, No Closure"

# The Minor Arcana

# The Suite of Wands - Energy, Drive, Willpower, Creativity, Power
the_knight_of_wands = "The Knight of Wands: Action, Adventure, Fearless"
the_knight_of_wands_reversed = "The Knight of Wands Reversed: Anger, Impulsiveness, Recklessness"
the_king_of_wands = "The King of Wands: Big Picture, Leader, Overcoming Challenges"
the_king_of_wands_reversed = "The King of Wands Reversed: Impulsive, Overbearing, Unachievable Expectations"
the_queen_of_wands = "The Queen of Wands: Courage, Determination, Joy"
the_queen_of_wands_reversed = "The Queen of Wands Reversed: Selfishness, Jealousy, Insecurities"
the_page_of_wands = "The Page of Wands: Exploration, Excitement, Freedom"
the_page_of_wands_reversed = "The Page of Wands Reversed: Lack of Direction, Procrastination, Creating Conflict"
the_two_of_wands = "The Two of Wands: Planning, Making Decisions, Leaving Home"
the_two_of_wands_reversed = "The Two of Wands Reversed: Fear of Change, Playing Safe, Bad Planning"
the_three_of_wands = "The Three of Wands: Looking Ahead, Expansion, Rapid Growth"
the_three_of_wands_reversed = "The Three of Wands Reversed: Obstacles, Delays, Frustration"
the_four_of_wands = "The Four of Wands: Community, Home, Celebration"
the_four_of_wands_reversed = "The Four of Wands Reversed: Lack of Support, Transience, Home Conflicts"
the_five_of_wands = "The Five of Wands: Compitition, Rivalry, Conflict"
the_five_of_wands_reversed = "The Five of Wands Reversed: Avoiding Conflict, Respecting Differences"
the_six_of_wands = "The Six of Wands: Victory, Success, Public Reward"
the_six_of_wands_reversed = "The Six of Wands Reversed: Excess Pride, Lack of Recognition, Punishment"
the_seven_of_wands = "The Seven of Wands: Perseverance, Defensive, Maintaining Control"
the_seven_of_wands_reversed = "The Seven of Wands Reversed: Give Up, Destroyed Confidence, Overwhelmed"
the_eight_of_wands = "The Eight of Wands: Rapid Action, Movement, Quick Decisions"
the_eight_of_wands_reversed = "The Eight of Wands Reversed: Panic, Waiting, Slow Down"
the_nine_of_wands = "The Nine of Wands: Resilience, Grit, Last Stand"
the_nine_of_wands_reversed = "The Nine of Wands Reversed: Exhaustion, Fatigue, Questioning Motivation"
the_ten_of_wands = "The Ten of Wands: Accomplishment, Burden, Responsibility"
the_ten_of_wands_reversed = "The Ten of Wands Reversed: Inability to Delegate, Overstressed, Burnt Out"
the_ace_of_wands = "The Ace of Wands: Creation, Willpower, Inspiration, Desire"
the_ace_of_wands_reversed = "The Ace of Wands Reversed: Lack of Energy, Lack of Passion, Boredom"


# The Suite of Cups - Emotion, Feelings, Intuition, Relationships
the_ace_of_cups = "The Ace of Cups: New Feelings, Spirituality, Intuition"
the_ace_of_cups_reversed = "The Ace of Cups Reversed: Emotional Loss, Blocked Creativity, Emptiness"
the_two_of_cups = "The Two of Cups: Unity, Partnership, Connection"
the_two_of_cups_reversed = "The Two of Cups Reversed: Imbalance, Broken Communication, Tension"
the_three_of_cups = "The Three of Cups: Friendship, Community, Happiness"
the_three_of_cups_reversed = "The Three of Cups Reversed: Overindulgence, Gossip, Isolation"
the_four_of_cups = "The Four of Cups: Apathy, Contemplation, Disconnectedness"
the_four_of_cups_reversed = "The Four of Cups Reversed: Sudden Awareness, Choosing Happiness, Acceptance"
the_five_of_cups = "The Five of Cups: Loss, Grief, Self-Pity"
the_five_of_cups_reversed = "The Five of Cups Reversed: Acceptance, Moving On, Finding Peace"
the_six_of_cups = "The Six of Cups: Familiarity, Happy Memories, Healing"
the_six_of_cups_reversed = "The Six of Cups Reversed: Moving Forward, Leaving Home, Independence"
the_seven_of_cups = "The Seven of Cups: Searching for Purpose, Choices, Daydreaming"
the_seven_of_cups_reversed = "The Seven of Cups Reversed: Lack of Purpose, Diversion, Confusion"
the_eight_of_cups = "The Eight of Cups: Walking Away, Disillusionment, Leaving Behind"
the_eight_of_cups_reversed = "The Eight of Cups Reversed: Avoidance, Fear of Change, Fear of Loss"
the_nine_of_cups = "The Nine of Cups: Satisfaction, Emotional Stability, Luxury"
the_nine_of_cups_reversed = "The Nine of Cups Reversed: Lack of Inner Joy, Smugness, Dissatisfaction"
the_ten_of_cups = "The Ten of Cups: Inner Happiness, Fulfillment, Dreams Coming True"
the_ten_of_cups_reversed = "The Ten of Cups Reversed: Shattered Dreams, Broken Family, Domestic Disharmony"
the_page_of_cups = "The Page of Cups: Happy Surprise, Dreamer, Sensitivity"
the_page_of_cups_reversed = "The Page of Cups Reversed: Emotional Immaturity, Insecurity, Disappointment"
the_knight_of_cups = "The Knight of Cups: Following the Heart, Idealist, Romantic"
the_knight_of_cups_reversed = "The Knight of Cups Reversed: Moodiness, Disappointment"
the_queen_of_cups = "The Queen of Cups: Compassion, Calm, Comfort"
the_queen_of_cups_reversed = "The Queen of Cups Reversed: Martyrdom, Insecurity, Dependence"
the_king_of_cups = "The King of Cups: Compassion, Control, Balance"
the_king_of_cups_reversed = "The King of Cups Reversed: Coldness, Moodiness, Bad Advice"


# The Suite of Swords - Logic, Ideas, Intellect, Communication
the_ace_of_swords = "The Ace of Swords: Breakthrough, Clarity, Sharp Mind"
the_ace_of_swords_reversed = "The Ace of Swords Reversed: Confusion, Brutality, Chaos"
the_two_of_swords = "The Two of Swords: Difficult Choices, Indecision, Stalemate"
the_two_of_swords_reversed = "The Two of Swords Reversed: Lesser of Two Evils, No Right Choice, Confusion"
the_three_of_swords = "The Three of Swords: Heartbreak, Suffering, Grief"
the_three_of_swords_reversed = "The Three of Swords Reversed: Recovery, Forgiveness, Moving On"
the_four_of_swords = "The Four of Swords: Rest, Restoration, Contemplation"
the_four_of_swords_reversed = "The Four of Swords Reversed: Restlessness, Burnout, Stress"
the_five_of_swords = "The Five of Swords: Unbridled Ambition, Win at All Costs, Sneakiness"
the_five_of_swords_reversed = "The Five of Swords Reversed: Lingering Resentment, Desire to Reconcile, Forgiveness"
the_six_of_swords = "The Six of Swords: Transition, Leaving Behind, Moving On"
the_six_of_swords_reversed = "The Six of Swords Reversed: Emotional Baggage, Unresolved Issues, Resisting Transition"
the_seven_of_swords = "The Seven of Swords: Deception, Trickery, Tactics and Strategy"
the_seven_of_swords_reversed = "The Seven of Swords Reversed: Coming Clean, Rethinking Approach, Deception"
the_eight_of_swords = "The Eight of Swords: Imprisonment, Self-Victimization, Entrapment"
the_eight_of_swords_reversed = "The Eight of Swords Reversed: Self-Acceptance, New Perspective, Freedom"
the_nine_of_swords = "The Nine of Swords: Anxiety, Hopelessness, Trauma"
the_nine_of_swords_reversed = "The Nine of Swords Reversed: Hope, Reaching Out, Despair"
the_ten_of_swords = "The Ten of Swords: Failure, Collapse, Defeat"
the_ten_of_swords_reversed = "The Ten of Swords Reversed: Can't Get Worse, Only Upwards, Enivitable End"
the_page_of_swords = "The Page of Swords: Curiosity, Restlessness, Mental Energy"
the_page_of_swords_reversed = "The Page of Swords Reversed: Deception, Manipulation, All Talk"
the_knight_of_swords = "The Knight of Swords: Action, Impulsiveness, Defending Beliefs"
the_knight_of_swords_reversed = "The Knight of Swords Reversed: No Direction, Disregard for Consequences, Unpredictability"
the_queen_of_swords = "The Queen of Swords: Complexity, Perceptiveness, Clear Mindedness"
the_queen_of_swords_reversed = "The Queen of Swords Reversed: Cold-Hearted, Cruel, Bitterness"
the_king_of_swords = "The King of Swords: Head Over Heart, Discipline, Truth"
the_king_of_swords_reversed = "The King of Swords Reversed: Manipulative, Cruel, Weakness"


# The Suite of Pentacles - Nature, Body, Material World, Stability
the_ace_of_pentacles = "The Ace of Pentacles: Opportunity, Prosperity, New Venture"
the_ace_of_pentacles_reversed = "The Ace of Pentacles Reversed: Lost Opportunity, Missed Chance, Bad Investment"
the_two_of_pentacles = "The Two of Pentacles: Balancing Decisions, Priorities, Adapting to Change"
the_two_of_pentacles_reversed = "The Two of Pentacles Reversed: Loss of Balance, Disorganized, Overwhelmed"
the_three_of_pentacles = "The Three of Pentacles: Teamwork, Collaboration, Building"
the_three_of_pentacles_reversed = "The Three of Pentacles Reversed: Lack of Teamwork, Disorganized, Group Conflict"
the_four_of_pentacles = "The Four of Pentacles: Conservation, Frugality, Security"
the_four_of_pentacles_reversed = "The Four of Pentacles Reversed: Greediness, Selfishness, Possiveness"
the_five_of_pentacles = "The Five of Pentacles: Need, Poverty, Insecurity"
the_five_of_pentacles_reversed = "The Five of Pentacles Reversed: Recovery, Charity, Improvement"
the_six_of_pentacles = "The Six of Pentacles: Charity, Generosity, Sharing"
the_six_of_pentacles_reversed = "The Six of Pentacles Reversed: Strings Attached, Stinginess, Power and Domination"
the_seven_of_pentacles = "The Seven of Pentacles: Hard Work, Perseverance, Diligence"
the_seven_of_pentacles_reversed = "The Seven of Pentacles Reversed: Work Without Results, Distractions, Lack of Rewards"
the_eight_of_pentacles = "The Eight of Pentacles: Apprenticeship, Passion, High Standards"
the_eight_of_pentacles_reversed = "The Eight of Pentacles Reversed: Lack of Passion, Uninspired, No Motivation"
the_nine_of_pentacles = "The Nine of Pentacles: Fruits of Labor, Rewards, Luxury"
the_nine_of_pentacles_reversed = "The Nine of Pentacles Reversed: Reckless Spending, Living Beyond Means, False Success"
the_ten_of_pentacles = "The Ten of Pentacles: Legacy, Culmination, Inheritance"
the_ten_of_pentacles_reversed = "The Ten of Pentacles Reversed: Fleeting Success, Lack of Stability, Lack of Resources"
the_page_of_pentacles = "The Page of Pentacles: Ambition, Desire, Diligence"
the_page_of_pentacles_reversed = "The Page of Pentacles Reversed: Lack of Commitment, Greediness, Laziness"
the_knight_of_pentacles = "The Knight of Pentacles: Efficiency, Hard Work, Responsibility"
the_knight_of_pentacles_reversed = "The Knight of Pentacles Reversed: Laziness, Obsessiveness, Work Without Reward"
the_queen_of_pentacles = "The Queen of Pentacles: Practicality, Creature Comforts, Financial Security"
the_queen_of_pentacles_reversed = "The Queen of Pentacles Reversed: Self-Centeredness, Jealousy, Smothering"
the_king_of_pentacles = "The King of Pentacles: Abundance, Prosperity, Security"
the_king_of_pentacles_reversed = "The King of Pentacles Reversed: Greed, Indulgence, Sensuality"



# Variable Assignments ---------------------------------------------------------------------------------------------------------------



the_suite_of_pentacles = [
    the_ace_of_pentacles, the_ace_of_pentacles_reversed,
    the_two_of_pentacles, the_two_of_pentacles_reversed,
    the_three_of_pentacles, the_three_of_pentacles_reversed,
    the_four_of_pentacles, the_four_of_pentacles_reversed,
    the_five_of_pentacles, the_five_of_pentacles_reversed,
    the_six_of_pentacles, the_six_of_pentacles_reversed,
    the_seven_of_pentacles, the_seven_of_pentacles_reversed,
    the_eight_of_pentacles, the_eight_of_pentacles_reversed,
    the_nine_of_pentacles, the_nine_of_pentacles_reversed,
    the_ten_of_pentacles, the_ten_of_pentacles_reversed,
    the_page_of_pentacles, the_page_of_pentacles_reversed,
    the_knight_of_pentacles, the_knight_of_pentacles_reversed,
    the_queen_of_pentacles, the_queen_of_pentacles_reversed,
    the_king_of_pentacles, the_king_of_pentacles_reversed
]

the_suite_of_swords = [
    the_ace_of_swords, the_ace_of_swords_reversed,
    the_two_of_swords, the_two_of_swords_reversed,
    the_three_of_swords, the_three_of_swords_reversed,
    the_four_of_swords, the_four_of_swords_reversed,
    the_five_of_swords, the_five_of_swords_reversed,
    the_six_of_swords, the_six_of_swords_reversed,
    the_seven_of_swords, the_seven_of_swords_reversed,
    the_eight_of_swords, the_eight_of_swords_reversed,
    the_nine_of_swords, the_nine_of_swords_reversed,
    the_ten_of_swords, the_ten_of_swords_reversed,
    the_page_of_swords, the_page_of_swords_reversed,
    the_knight_of_swords, the_knight_of_swords_reversed,
    the_queen_of_swords, the_queen_of_swords_reversed,
    the_king_of_swords, the_king_of_swords_reversed
]

the_suite_of_cups = [
    the_ace_of_cups, the_ace_of_cups_reversed,
    the_two_of_cups, the_two_of_cups_reversed,
    the_three_of_cups, the_three_of_cups_reversed,
    the_four_of_cups, the_four_of_cups_reversed,
    the_five_of_cups, the_five_of_cups_reversed,
    the_six_of_cups, the_six_of_cups_reversed,
    the_seven_of_cups, the_seven_of_cups_reversed,
    the_eight_of_cups, the_eight_of_cups_reversed,
    the_nine_of_cups, the_nine_of_cups_reversed,
    the_ten_of_cups, the_ten_of_cups_reversed,
    the_page_of_cups, the_page_of_cups_reversed,
    the_knight_of_cups, the_knight_of_cups_reversed,
    the_queen_of_cups, the_queen_of_cups_reversed,
    the_king_of_cups, the_king_of_cups_reversed
]

the_suite_of_wands = [
    the_knight_of_wands, the_knight_of_wands_reversed,
    the_king_of_wands, the_king_of_wands_reversed,
    the_queen_of_wands, the_queen_of_wands_reversed,
    the_page_of_wands, the_page_of_wands_reversed,
    the_two_of_wands, the_two_of_wands_reversed,
    the_three_of_wands, the_three_of_wands_reversed,
    the_four_of_wands, the_four_of_wands_reversed,
    the_five_of_wands, the_five_of_wands_reversed,
    the_six_of_wands, the_six_of_wands_reversed,
    the_seven_of_wands, the_seven_of_wands_reversed,
    the_eight_of_wands, the_eight_of_wands_reversed,
    the_nine_of_wands, the_nine_of_wands_reversed,
    the_ten_of_wands, the_ten_of_wands_reversed,
    the_ace_of_wands, the_ace_of_wands_reversed
]

# minor_arcana = [the_suite_of_cups,the_suite_of_pentacles,the_suite_of_swords,the_suite_of_wands]

major_arcana = [
    the_fool, the_fool_reversed,
    the_magician, the_magician_reversed,
    the_high_priestess, the_high_priestess_reversed,
    the_empress, the_empress_reversed,
    the_emperor, the_emperor_reversed,
    the_hierophant, the_hierophant_reversed,
    the_lovers, the_lovers_reversed,
    the_chariot, the_chariot_reversed,
    strength, strength_reversed,
    the_hermit, the_hermit_reversed,
    the_wheel_of_fortune, the_wheel_of_fortune_reversed,
    justice, justice_reversed,
    the_hanged_man, the_hanged_man_reversed,
    death, death_reversed,
    temperance, temperance_reversed,
    the_devil, the_devil_reversed,
    the_tower, the_tower_reversed,
    the_star, the_star_reversed,
    the_moon, the_moon_reversed,
    the_sun, the_sun_reversed,
    judgement, judgement_reversed,
    the_world, the_world_reversed
]

cards = [major_arcana,the_suite_of_cups,the_suite_of_pentacles,the_suite_of_swords,the_suite_of_wands]


# Functions ----------------------------------------------------------------------------------------------------------------------------

# One Card Reading Ex: "What Should I focus on today?"
def one_card_reading():
    card = random.choice(cards)
    card = random.choice(card)
    return card

# print(one_card_reading())

# Three Card Spread Ex: "What is my Past, Present, and Future?"
def three_card_spread():
    card1 = one_card_reading()
    card2 = one_card_reading()
    card3 = one_card_reading()
    question = input(f"If you're looking for Info on your Past, Present, or Future, Input 'Time'.\nIf you're looking for insight into your mind, body, and spirit, 'Insight'.\nIf you're looking for Guidance or Advice on a personal matter, input 'Guidance'.\nYour Desired Reading: ")
    if question.lower() == "time":
        input("What is your question? ")
        reading = f"Here are the cards that represent your Past, Present, and Future.\nPast: {card1}\nPresent: {card2}\nFuture: {card3}"
        return reading
    elif question.lower() == "insight":
        input("What is your question? ")
        reading = f"Here are the cards the represent your mind, body, and spirit.\nMind: {card1}\nBody: {card2}\nSpirit: {card3}"
        return reading
    elif question.lower() == "guidance":
        input("What is your question? ")
        reading = f"Here are the cards that represent your Situation, Challenges or Obsticals in your way, and Your Advice.\nSituation: {card1}\nChallenge: {card2}\nAdvice: {card3}"
        return reading
    
# print(three_card_spread())


# Celtic Cross Spread Ex: "What is my Current Situation, What is Crossing me, What is Beneath me, What is Behind me, What is Ahead of me, My Fears, My Hopes, My Outcome, My Advice"
def celtic_cross_spread():
    card1 = one_card_reading()
    card2 = one_card_reading()
    card3 = one_card_reading()
    card4 = one_card_reading()
    card5 = one_card_reading()
    card6 = one_card_reading()
    card7 = one_card_reading()
    card8 = one_card_reading()
    card9 = one_card_reading()
    card10 = one_card_reading()
    question = input(f"What is troubling you? ")
    reading = f"Here are the cards that represent the following:\nCurrent Situation: {card1}\nChallenges Ahead: {card2}\nRoot Cause or Causes: {card3}\nPast Influences: {card4}\nYour Goal or Ideal: {card5}\nYour Near Future: {card6}\nYour Self View: {card7}\nExternal Influences: {card8}\nYour Hopes and Fears: {card9}\nYour Overall Outcome: {card10}"
    return reading

# print(celtic_cross_spread())

# Relationship Spread Ex: "What is troubling you in your relationship?"
def relationship_spread():
    card1 = one_card_reading()
    card2 = one_card_reading()
    card3 = one_card_reading()
    card4 = one_card_reading()
    card5 = one_card_reading()
    question = input(f"What is troubling you in your relationship? ")
    reading = f"Here are the cards that represent the following:\nYour Perspective: {card1}\nTheir Perspective: {card2}\nStrengths of the Relationship: {card3}\nChallenges in the Relationship: {card4}\nOutcome or Advice: {card5}"
    return reading

# print(relationship_spread())

# Year Ahead Spread Ex: "What are you looking to gain insight on in the next year?"
def year_ahead_spread():
    card1 = one_card_reading()
    card2 = one_card_reading()
    card3 = one_card_reading()
    card4 = one_card_reading()
    card5 = one_card_reading()
    card6 = one_card_reading()
    card7 = one_card_reading()
    card8 = one_card_reading()
    card9 = one_card_reading()
    card10 = one_card_reading()
    card11 = one_card_reading()
    card12 = one_card_reading()
    question = input(f"What are you looking to gain insight on in the next year? ")
    reading = f"Here are the cards that represent the following:\nJanuary: {card1}\nFebruary: {card2}\nMarch: {card3}\nApril: {card4}\nMay: {card5}\nJune: {card6}\nJuly: {card7}\nAugust: {card8}\nSeptember: {card9}\nOctober: {card10}\nNovember: {card11}\nDecember: {card12}"
    return reading

# print(year_ahead_spread())


# Decision Making Spread Ex: "How does each decision affect me?"
def decision_making_spread():
    reading_list = []
    print("This spread is designed to help you make a decision between multiple options.")
    print(f"First number your options from 1 to however many options you have.")
    num = int(input("How many options are you deciding between? "))
    for i in range(1,num+1):
        card = one_card_reading()
        reading = f"Option {i} is represented by: {card}"
        reading_list.append(reading)
    reading_list = "\n".join(reading_list)
    return reading_list


# print(decision_making_spread())


# Shadow Work Spread Ex: "What Shadow aspects should I work on?"
def shadow_work_spread():
    card1 = one_card_reading()
    card2 = one_card_reading()
    card3 = one_card_reading()

    reading = f"Here are the cards that represent the following:\nYour Shadow, or Hidden Self: {card1}\nThe Lesson or Challenge: {card2}\nThe Way to Integrate this Knowledge: {card3}"
    return reading

# print(shadow_work_spread())




# Main.py ----------------------------------------------------------------------------------------------------------------------------
#Main Code

import tkinter as tk
from tkinter import scrolledtext
from queue import Queue
from threading import Thread
import sys



class IORedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.input_queue = Queue()

    def write(self, text):
        # Redirect stdout to the text widget
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.insert(tk.END, text)
        self.text_widget.see(tk.END)  # Ensure the latest text is visible
        self.text_widget.config(state=tk.DISABLED)

    def flush(self):
        pass

    def readline(self):
        # Wait for and return input with a newline appended
        return self.input_queue.get() + '\n'

    # Optionally handle sys.stderr separately
    def handle_stderr(self, text):
        # Do nothing or log to a file if necessary
        pass




class CommandLineGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tarot Reading Terminal")
        self.root.geometry("1100x600")
        
        # Create the main text area
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg='black', fg='magenta', font=('Arial', 14))
        self.text_area.pack(expand=True, fill='both')
        
        # Create the input entry with increased width and font size
        self.entry = tk.Entry(root, bg='black', fg='lime', insertbackground='lime',width=60, font=('Arial', 20))
        self.entry.pack(fill='x')
        self.entry.bind('<Return>', self.process_input)
        
        # Setup IO redirection
        self.redirector = IORedirector(self.text_area)
        self.original_stdout = sys.stdout
        self.original_stdin = sys.stdin
        sys.stdout = self.redirector
        sys.stdin = self.redirector
        sys.stderr = self.redirector  # Redirect stderr
        
        # Focus on entry
        self.entry.focus_set()
        
        # Start the main program loop in a separate thread
        self.thread = Thread(target=self.run_program)
        self.thread.daemon = True
        self.thread.start()


    def process_input(self, event):
        """Handle input from the entry widget"""
        user_input = self.entry.get()
        # Display user input in the text area
        self.text_area.config(state=tk.NORMAL)  # Temporarily enable for inserting user input
        self.text_area.insert(tk.END, user_input + '\n')
        self.text_area.config(state=tk.DISABLED)  # Disable it again to make it read-only

        # Send user input to the input queue for processing
        self.redirector.input_queue.put(user_input)
        
        # Clear the entry box after submission
        self.entry.delete(0, tk.END)


    def run_program(self):
        """Run the main tarot program"""
        try:
            while True:
                print("\nDo you wish to do a tarot reading? (yes/no): ", end='')
                question = input()
                
                if question.lower() == "yes":
                    print("\nWhat type of reading do you want?")
                    print("Available Options:")
                    print("General: A general one card reading.")
                    print("Triple: A three card reading.")
                    print("Cross: A celtic cross reading.")
                    print("Relationship: A reading into your current relationship.")
                    print("Yearly: A reading for every month of the year.")
                    print("Decision: A reading based on possible options of an impending decision.")
                    print("Shadow: A reading on your shadow self.")
                    print("Please choose an option: ", end='')
                    
                    reading_type = input()
                    
                    if reading_type.lower() == "general":
                        print("\nPlease type your general question: ", end='')
                        question = input()
                        print(self.one_card_reading())
                    
                    elif reading_type.lower() == "triple":
                        print(self.three_card_spread())
                    
                    elif reading_type.lower() == "cross":
                        print(self.celtic_cross_spread())
                    
                    elif reading_type.lower() == "relationship":
                        print(self.relationship_spread())
                    
                    elif reading_type.lower() == "yearly":
                        print(self.year_ahead_spread())
                    
                    elif reading_type.lower() == "decision":
                        print(self.decision_making_spread())
                    
                    elif reading_type.lower() == "shadow":
                        print(self.shadow_work_spread())
                    
                    elif reading_type.lower() == "exit":
                        print("Goodbye!")
                        self.root.quit()
                        break
                        
                elif question.lower() == "no":
                    print("Goodbye!")
                    self.root.quit()
                    break
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            sys.stdout = self.original_stdout
            sys.stdin = self.original_stdin
            sys.stderr = self.original_stderr


    # Tarot reading methods
    def one_card_reading(self):
        # from real_tarot_reading import one_card_reading
        return one_card_reading()

    def three_card_spread(self):
        #from real_tarot_reading import three_card_spread
        return three_card_spread()

    def celtic_cross_spread(self):
        #from real_tarot_reading import celtic_cross_spread
        return celtic_cross_spread()

    def relationship_spread(self):
        #from real_tarot_reading import relationship_spread
        return relationship_spread()

    def year_ahead_spread(self):
        #from real_tarot_reading import year_ahead_spread
        return year_ahead_spread()

    def decision_making_spread(self):
        #from real_tarot_reading import decision_making_spread
        return decision_making_spread()

    def shadow_work_spread(self):
        #from real_tarot_reading import shadow_work_spread
        return shadow_work_spread()

def main():
    root = tk.Tk()
    app = CommandLineGUI(root)
    root.mainloop()


main()