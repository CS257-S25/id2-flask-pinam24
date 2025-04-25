import csv


def parse_bookban_csv(database_file):
    bookban_list = []
    with open(database_file, newline="") as csv_file:
        reader = csv.reader(csv_file)
        next(reader, None)  # Skips header
        for (
            title,
            author,
            secondary_author,
            illustrator,
            translator,
            state,
            district,
            ban_date,
            ban_status,
            origin,
        ) in reader:
            bookban_list.append(
                {
                    "title": title,
                    "author": lastfirst_to_firstlast(author),
                    "secondary_author": secondary_author,
                    "illustrator": illustrator,
                    "translator": translator,
                    "state": state,
                    "district": district,
                    "ban_date": ban_date,
                    "ban_status": ban_status,
                    "origin": origin,
                }
            )
    return bookban_list


def lastfirst_to_firstlast(field):
    words = field.split(", ")
    if len(words) > 1:
        return words[1] + " " + words[0]
    else:
        return field


def main():
    book_banlist = parse_bookban_csv("Data/bookbans-merged.csv")
    print(book_banlist[0])


if __name__ == "__main__":
    main()
