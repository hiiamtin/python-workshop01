import pandas as pd

def preprocess_data(df):
    # Read the CSV file into a DataFrame
    df = pd.read_csv('data/data.csv')

    # Display the first few rows of the DataFrame
    print(df.head())

    print(df.isnull().sum())

    # filter year >= 2023 delete it
    df = df[df['year'] < 2023]

    # If gender is null or empty -> replace it with ‘Male’
    df['gender'] = df['gender'].fillna('Male')

    # if age ​​is null/empty/na -> replaced with the ‘mean’ value of age. (Round up)
    average_age = df['age'].mean()
    average_age = round(average_age)
    print(f"Average age: {average_age}")
    df['age'] = df['age'].fillna(average_age)

    # save the modified DataFrame to a new CSV file
    df.to_csv('data/transformed_data.csv', index=False)
    print(df.isnull().sum())

def main():
    # preprocess_data()
    df = pd.read_csv('data/transformed_data.csv')
    print(df.head())

    

if __name__ == "__main__":
    main()