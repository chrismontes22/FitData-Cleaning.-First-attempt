### This is the code I used to get rid of the proper nouns in my large text data. 
### It prints which words are being erased so that I could modify the list. 
### With the help of GPT Libre Calc I cleared up the list of proper nouns. I have the code save the new data on a seperate txt file.

import spacy

def remove_irrelevant_proper_nouns(text, relevant_nouns, exceptions):
    nlp = spacy.load('en_core_web_sm')

    doc = nlp(text)

    
    erased_words = [token.text for token in doc if token.ent_type_ == 'PERSON' and token.text not in relevant_nouns and token.text not in exceptions]
    tokens = [token.text if (token.ent_type_ != 'PERSON' and token.text.lower() not in relevant_nouns and token.text.lower() not in exceptions) or token.text in relevant_nouns or token.text in exceptions else ' ' for token in doc]


    return ' '.join(tokens).strip(), erased_words

def process_large_text_file(input_file, output_file, relevant_nouns, exceptions):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    modified_content, erased_words = remove_irrelevant_proper_nouns(content, relevant_nouns, exceptions)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(modified_content)


    print("Erased Words:", erased_words)

# List of words and file input/output
input_file_path = 'Tuning data 2 spelling.txt'  # Replace with the path to your input file
output_file_path = 'DataNOname.txt'  # Replace with the desired output file path
relevant_nouns = ["yoga", "other", "relevant", "nouns"]  # Add more relevant nouns as needed
exceptions = ["Hypertrophy", "Builds", "More", "Muscle", "Strength", "Strength", 
    "Faster", "Neural", "Fatigue", "Peak", "Strength", "Strength", 
    "Loads", "Should", "Be", "Lighter", "Loads", "Should", "Be", 
    "Lighter", "max", "lighter", "loads", "max", "Strength", "max", 
    "strength", "Strength", "Make", "You", "Strength", "Bench", 
    "deadlifts", "Training", "Training", "First", "Training", "max", 'Oxygen', 'Burns', 'ATP',
    "bench", "press", "bench", "presses", "Cons", "Reduced", 'Burpee', 
    "Strength", "bench", "presses", "Vs", "Strength", "Training", 'Pareto', 'Loading', 'Mesocycles', 'Stretch', 'Yourself', 'Thin', 'Focus', 'Front', 'Squat', 'Split', 'Squat', 'Size',
    "Which", "Olympia", 'Max',   'VO2', 'Reasons', 'Vinyasa', 'Yoga', 'Flow',
    'BenefitsCalms', 'Increases', 'Strong', 'hatha', 'Strong', 'Triangle',
    'Pose',  'The', 'Dolphin', 'Pincha', 'Mayurasana', 'Haka', 'Adonis', 'uttanasana', 'Teaches', 'How',
    'To', 'With', 'Discomfort', 'Seasoned', 'Deadlifts',  'Broken', 
    'Cartwright', 'Stretching', 'Carr', 'Aim', 'Frank', 'Benedetto', 'Bonnie', 'Marks', 'Lou', 'Krystina', 'Czaja',
    'Soft', 'Young',  'Elbow', 'Long', 'Light', 'Dumbbell', 'Exercises', 'Chops', 'Sandbag', 'Imposed', 'Demands',
    'Adaptation', 'Syndrome', 'Hans', 'Selye', 'Fascia', 'Length', 'Best', 'Goblet', 'Turkish', 'Getup', 'Arnold',
    'Press', 'Renegade', 'Row', 'Reverse', 'Fly', 'Lateral', 'Raise', 'Pick',  'Biceps', 'kettlebell',
    'Muscles', 'Frost', 'Schwarzenegger', 'Flat', 'Fly', 'Rotator', 'Bent', 'Arm', 'Pull', 'Over', 'kettlebell',
    'Rotate', 'Push', 'Delivers', 'Strengthens', 'Use', 'Multipower', 'Ant', 'Variations', 'Once', 'Farmer', 'Advanced', 'Covid', 'Jump', 'Biceps',
    'sumo', 'Boulder', 'Obvious', 'Verdict', 'Gym', 'Reviews', 'Grip', 'Snap', 'Landmine',
    'Rainbow', 'Anterior', 'Deltoid', 'Lateral', 'Gluteus', 'Maximus', 'Medius', 'Minimus', 'Rectus', 'Femoris',
    'Vastus', 'Medialis', 'Jerk', 'jerk', 'Grip', 'High', 'Pull', 'Barbell', 'Rollout', 'Tips', 'Cardio', 'Set',
    'SMART', 'Momentum', 'it.1', 'Lifting', 'Chair', 'Bicep', 'Curl', 'Lateral', 'Thigh', 'Circles', 'Tricep', 'Dip', 'Chin', '-', 'Up', 'Drop', 'Broad',
    'Example', 'Hand', 'Stretches', 'Side', 'Leg', 'Raises', 'Shin', 'Strengthener', 'V.', 'Cardio', 'Tai', 'Chi',
    'Tai', 'chi', 'Wrist', 'Curls', 'Place', 'Choose', 'Tik', 'Tok', 'Eric', 'Broser', 'Beginner', 'Workout', 'Greatest', 'Dumbells',
    'Trice', 'aim', 'Plyometric', 'Box', 'Knee', 'buff', 'Complete', '-', 'Ups', 'Settle', 'Squats', 'Donkey', 'Kicks', 'Drop', 'Tuck',
    'Minimize', 'Rest', 'Time', ':', 'Routines', 'Incorporate', 'Skill', 'Based', 'Work', ':',
    'Bodyweight', 'Burpees', 'Bodyweight', 'Bodyweight', 'Rest', 'Torso', 'Cone', 'pain1', 'reflexes1', 'pain1', 'reflexes1', 'pain1', 
    'reflexes1', 'Novice', 'Novice', 'Kettlebell', 'Dumbbells', 'Kick', 'Creative', 'Mind','Active', 'Body', 'Apart', 'Anchor', 'Kick',
    'Snowboard', 'Bodyweight', 'Bodyweight', 'Skull', 'Crusher', 'Bodyweight', 'Bodyweight', 'Windmill', 'Superset', 'Superset']  # Add exceptions here

process_large_text_file(input_file_path, output_file_path, relevant_nouns, exceptions)
