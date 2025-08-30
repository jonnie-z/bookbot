def count_words(text):
    text_list = text.split()
    return len(text_list)


def count_chars(text):
    text = text.lower()
    result_dict = {}

    for char in text:
        if char not in result_dict:
            result_dict[char] = 1
        else:
            result_dict[char] = result_dict[char] + 1
    
    return result_dict

def get_report_dict(input_dict):
    result = []

    for key in input_dict:
        if key.isalpha():
            result.append({
                "char": key,
                "num": input_dict[key]
            })

    result.sort(reverse=True, key=lambda items: items["num"])
    return result
