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

def remove_outliers(df, columns):
    for column in columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    return df