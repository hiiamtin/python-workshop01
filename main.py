import pandas as pd

def main():
    # Read the CSV file into a DataFrame
    df = pd.read_csv('data/data.csv')

    # Display the first few rows of the DataFrame
    print(df.head())

    print(df.isnull().sum())

if __name__ == "__main__":
    main()