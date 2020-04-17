def even_odd_count(li):
    dict_odd_even = {"odd":0, "even":0, "zero":0}
    print(dict_odd_even.get("odd"))
    for i in li:
        if i != 0:
            if i % 2 == 1:
                dict_odd_even['odd'] = dict_odd_even.get("odd", 0) + 1
            else:
                dict_odd_even['even'] = dict_odd_even.get("even", 0) + 1
        else:
            dict_odd_even['zero'] = dict_odd_even.get("zero", 0) + 1
    return dict_odd_even['odd'], dict_odd_even['even'], dict_odd_even['zero']

li = [45, 23, 85, 64, 22, 75, 14, 16, 24, 86,0, 43, 0, 99,0, 96, 52, 78, 64, 25, 31, 0]
odd, even, zero = even_odd_count(li)
print("Odd:", odd, "Even:", even, "Zero:", zero)