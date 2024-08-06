# Define a dictionary to map full position names to abbreviations
position_mapping = {
    'Goalkeeper': 'GK',
    'Defender Centre-Back': 'DF',
    'Defender Left-Back': 'DF',
    'Defender Right-Back': 'DF',
    'midfield-DefensiveMidfield': 'MF',
    'midfield-CentralMidfield': 'MF',
    'midfield-AttackingMidfield': 'MF',
    'Attack-LeftWinger': 'ATT',
    'Attack-RightWinger': 'ATT',
    'Attack Centre-Forward': 'ATT',
    'midfield-RightMidfield': 'MF',
    'midfield-LeftMidfield': 'MF',
    'Attack-SecondStriker': 'ATT',
    'midfield': 'MF',
    'Attack': 'ATT',
    'Defender': 'DF'
}

# Function to replace position names with abbreviations
def abbreviate_positions(position):
    return position_mapping.get(position, position)