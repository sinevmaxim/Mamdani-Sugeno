import json
from matplotlib import pyplot as plt


def appearance_membership(x):
    result = []

    if x <= 30:
        value = (30 - x) / 30

        result.append({
            'term': 'New',
            'membership': round(value, 2)
        })

    if 20 <= x <= 50:
        if x <= 35:
            value = (x - 20) / 15
        else:
            value = (50 - x) / 15

        result.append({
            'term': 'Very Good Condition',
            'membership': round(value, 2)
        })

    if 40 <= x <= 70:
        if x < 55:
            value = (x - 40) / 15
        else:
            value = (70 - x) / 15

        result.append({
            'term': 'Good Condition',
            'membership': round(value, 2)
        })

    if 60 <= x <= 90:
        if x < 75:
            value = (x - 60) / 15
        else:
            value = (90 - x) / 15

        result.append({
            'term': 'Fine Condition',
            'membership': round(value, 2)
        })

    if x >= 80:
        value = (x - 80) / 20

        result.append({
            'term': 'Bad Condition',
            'membership': round(value, 2)
        })

    return result


def date_membership(x):
    result = []

    if x <= 30:
        value = (30 - x) / 30

        result.append({
            'term': 'Newest Release',
            'membership': round(value, 2)
        })

    if 10 <= x <= 50:
        if x <= 30:
            value = (x - 10) / 20
        else:
            value = (50 - x) / 20

        result.append({
            'term': 'Recent',
            'membership': round(value, 2)
        })
    if 40 <= x <= 60:
        if x < 50:
            value = (x - 40) / 10
        else:
            value = (60 - x) / 10

        result.append({
            'term': 'Average',
            'membership': round(value, 2)
        })
    if 55 <= x <= 85:
        if x < 70:
            value = (x - 55) / 15
        else:
            value = (85 - x) / 15
        result.append({
            'term': 'Long-Ago',
            'membership': round(value, 2)
        })
    if x >= 80:
        value = (x - 80) / 20
        result.append({
            'term': 'Aged',
            'membership': round(value, 2)
        })

    return result


def popularity_membership(x):
    result = []

    if x <= 20:
        value = (20 - x) / 20
        result.append({
            'term': 'not popular',
            'membership': round(value, 2)
        })

    if 10 <= x <= 40:
        if x <= 25:
            value = (x - 10) / 15
        else:
            value = (40 - x) / 15
        result.append({
            'term': 'small popularity',
            'membership': round(value, 2)
        })

    if 30 <= x <= 70:
        if x <= 50:
            value = (x - 30) / 20
        else:
            value = (70 - x) / 20
        result.append({
            'term': 'fine popularity',
            'membership': round(value, 2)
        })

    if 60 <= x <= 90:
        if x <= 75:
            value = (x - 60) / 15
        else:
            value = (90 - x) / 15
        result.append({
            'term': 'popular',
            'membership': round(value, 2)
        })

    if x >= 80:
        value = (x - 80) / 20
        result.append({
            'term': 'very popular',
            'membership': round(value, 2)
        })

    return result


def crisp_performance(term, score):
    if term == 'not popular':
        result = 20 - (20 * score)
        return result

    elif term == 'small popularity':
        result_1 = 10 + (15 * score)
        result_2 = 40 - (15 * score)
        return (result_1 + result_2) / 2

    elif term == 'fine popularity':
        result_1 = 30 + (20 * score)
        result_2 = 70 - (25 * score)
        return (result_1 + result_2) / 2

    elif term == 'popular':
        result_1 = 60 + (15 * score)
        result_2 = 90 - (15 * score)
        return (result_1 + result_2) / 2

    elif term == 'very popular':
        result = 80 + (20 * score)
        return result


def crisp_conclusion(score):
    return round(score, 2)


def input_evaluation(appearance_score, date_score):
    a_membership = appearance_membership(appearance_score)
    d_membership = date_membership(date_score)

    results = []
    if len(a_membership) == 2:
        if len(d_membership) == 2:
            results.append({
                'result': min(a_membership[0]['membership'], d_membership[0]['membership']),
                'appearance': a_membership[0]['term'],
                'date': d_membership[0]['term']
            })
            results.append({
                'result': min(a_membership[0]['membership'], d_membership[1]['membership']),
                'appearance': a_membership[0]['term'],
                'date': d_membership[1]['term']
            })
            results.append({
                'result': min(a_membership[1]['membership'], d_membership[0]['membership']),
                'appearance': a_membership[1]['term'],
                'date': d_membership[0]['term']
            })
            results.append({
                'result': min(a_membership[1]['membership'], d_membership[1]['membership']),
                'appearance': a_membership[1]['term'],
                'date': d_membership[1]['term']
            })

        elif len(d_membership) == 1:
            results.append({
                'result': min(a_membership[0]['membership'], d_membership[0]['membership']),
                'appearance': a_membership[0]['term'],
                'date': d_membership[0]['term']
            })
            results.append({
                'result': min(a_membership[1]['membership'], d_membership[0]['membership']),
                'appearance': a_membership[1]['term'],
                'date': d_membership[0]['term']
            })

    elif len(a_membership) == 1:
        if len(d_membership) == 2:
            results.append({
                'result': min(a_membership[0]['membership'], d_membership[0]['membership']),
                'appearance': a_membership[0]['term'],
                'date': d_membership[0]['term']
            })
            results.append({
                'result': min(a_membership[0]['membership'], d_membership[1]['membership']),
                'appearance': a_membership[0]['term'],
                'date': d_membership[1]['term']
            })

        elif len(d_membership) == 1:
            results.append({
                'result': min(a_membership[0]['membership'], d_membership[0]['membership']),
                'appearance': a_membership[0]['term'],
                'date': d_membership[0]['term']
            })

    return results


def get_rules_data():
    """ LOADING CUSTOM RULES FROM CONFIG FILE """
    rules = []

    with open('config.json') as json_file:
        data = json.load(json_file)

        for rule in data['rules']:
            rules.append({
                'conditions': rule['conditions'],
                'mamdani_output': rule['mamdani_output'],
                'sugeno_output': rule['sugeno_output']
            })

    return rules


def mamdani(appearance_score, date_score):
    """ MAMDANI """
    memberships = input_evaluation(appearance_score, date_score)
    result = max(list(map(lambda x: x['result'], memberships)))

    resulting_rule = next(
        item for item in memberships if item["result"] == result)

    rules = get_rules_data()

    power_rule = next(
        rule for rule in rules if rule["conditions"] == [resulting_rule['appearance'], resulting_rule['date']])

    return crisp_performance(power_rule['mamdani_output'], resulting_rule['result'])


def sugeno(appearance_score, date_score):
    """ SUGENO """
    memberships = input_evaluation(appearance_score, date_score)
    w = list(map(lambda x: x['result'], memberships))
    y = []

    rules = get_rules_data()

    for i, rule in enumerate(memberships):
        power_rule = next(
            item for item in rules if
            item["conditions"] == [rule['appearance'], rule['date']])

        y.append(eval(
            power_rule['sugeno_output'], {}, {"x": appearance_score, "y": date_score}))

    result = []
    for i in range(len(w)):
        result.append(round((w[i] * y[i]), 2))

    result = sum(result) / sum(w)
    return round(result, 2)


def build_semantic_graphs():
    """ PLOTTING GRAPHS """
    fig = plt.figure()
    fig.set_figheight(7)
    fig.set_figwidth(7)

    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    fig.suptitle('Семантические графики термов')

    appearance_semantics = {
        'New': {'x': [], 'y': [], 'color': 'purple'},
        'Very Good Condition': {'x': [], 'y': [], 'color': 'red'},
        'Good Condition': {'x': [], 'y': [], 'color': 'orange'},
        'Fine Condition': {'x': [], 'y': [], 'color': 'yellow'},
        'Bad Condition': {'x': [], 'y': [], 'color': 'black'},
    }

    for x in range(101):
        x_membership = appearance_membership(x)
        for term in x_membership:
            appearance_semantics[term['term']]['x'].append(x)
            appearance_semantics[term['term']]['y'].append(
                round(term['membership'] * 100, 2))

    for _, value in appearance_semantics.items():
        ax1.plot(value['x'], value['y'], color=value['color'])

    date_semantics = {
        'Newest Release': {'x': [], 'y': [], 'color': 'purple'},
        'Recent': {'x': [], 'y': [], 'color': 'red'},
        'Average': {'x': [], 'y': [], 'color': 'orange'},
        'Long-Ago': {'x': [], 'y': [], 'color': 'yellow'},
        'Aged': {'x': [], 'y': [], 'color': 'black'},
    }

    for x in range(101):
        x_membership = date_membership(x)
        for term in x_membership:
            date_semantics[term['term']]['x'].append(x)
            date_semantics[term['term']]['y'].append(
                round(term['membership'] * 100, 2))

    for _, value in date_semantics.items():
        ax2.plot(value['x'], value['y'], color=value['color'])

    performance_semantics = {
        'not popular': {'x': [], 'y': [], 'color': 'purple'},
        'small popularity': {'x': [], 'y': [], 'color': 'red'},
        'fine popularity': {'x': [], 'y': [], 'color': 'orange'},
        'popular': {'x': [], 'y': [], 'color': 'blue'},
        'very popular': {'x': [], 'y': [], 'color': 'green'},
    }

    for x in range(101):
        x_membership = popularity_membership(x)
        for term in x_membership:
            performance_semantics[term['term']]['x'].append(x)
            performance_semantics[term['term']]['y'].append(
                round(term['membership'] * 100, 2))

    for _, value in performance_semantics.items():
        ax3.plot(value['x'], value['y'], color=value['color'])

    ax1.legend(["New", "Very Good", "Good", "Fine", "Bad"])
    ax2.legend(["Newest Release", "Recent", "Average", "Long-Ago", "Aged"])
    ax3.legend(["Not popular", "Small popularity",
                "Fine popularity", "Popular", "Very popular"])

    plt.show()


def build_3d_graph():
    _points = [[], [], [], []]

    for x in range(100):
        for y in range(100):
            _points[0].append(x)
            _points[1].append(y)
            _points[2].append(mamdani(x, y))
            _points[3].append(sugeno(x, y))

    ax2 = plt.axes(projection='3d')
    ax2.plot_trisurf(_points[0], _points[1], _points[3],
                     cmap='pink', linewidth=1)

    ax2.set_title("Sugeno")
    ax2.set_xlabel("Book Appearance")
    ax2.set_ylabel("Book Release Date")
    ax2.set_zlabel("Book Popularity")
    plt.show()

    ax1 = plt.axes(projection='3d')
    ax1.plot_trisurf(_points[0], _points[1], _points[2],
                     cmap='bone', linewidth=1)

    ax1.set_title("Mamdani")
    ax1.set_xlabel("Book Appearance")
    ax1.set_ylabel("Book Release Date")
    ax1.set_zlabel("Book Popularity")
    plt.show()


build_semantic_graphs()
build_3d_graph()

print('Enter appearance score (Lower - Better):')
appearance_score = input()

print('Enter date score (Lower - Newer):')
date_score = input()

result_mamdani = mamdani(float(appearance_score), float(date_score))
result_sugeno = sugeno(float(appearance_score), float(date_score))

print(
    f'\nResults:\n> Mamdani: {result_mamdani}\n> Sugeno: {result_sugeno}\n\n\n')
