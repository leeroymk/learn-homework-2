import csv


mafia_list = [
    {'name': 'Tony Soprano', 'age': 40, 'job': 'Boss'},
    {'name': 'Paulie Gualtieri', 'age': 65, 'job': 'Captain'},
    {'name': 'Silvio Dante', 'age': 55, 'job': 'Consigliere'},
    {'name': 'Christopher Moltisanti', 'age': 31, 'job': 'Captain'},
    ]


def main():

    with open('mafia.csv', 'w', encoding='utf-8', newline='') as mafia:

        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(mafia, fields, delimiter=';')
        writer.writeheader()

        for user in mafia_list:
            writer.writerow(user)


if __name__ == "__main__":
    main()
