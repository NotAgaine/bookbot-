def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read() 
        lower_case_string = file_contents.lower()
        words = file_contents.split()
        number_of_words = len(words)

        res = {}
        for keys in lower_case_string:
            if keys.isalpha():  # This checks if the character is alphabetic
                res[keys] = res.get(keys, 0) + 1

        char_list = [{"character": char, "count": count} for char, count in res.items()]
        char_list.sort(key=lambda x: x["count"], reverse=True)

        for item in char_list:
            char = item["character"]
            count = item["count"]
            report_line = f"The '{char}' character was found {count} times"
            print(report_line)

        print("Count of all alphabetic characters in Frankenstein is: " + str(res))
        print(number_of_words)

main()