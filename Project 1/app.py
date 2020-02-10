from random import shuffle

from flask import Flask
from flask import render_template


import data

app = Flask(__name__)


@app.route('/')
def index():
    tour_ids = list(data.tours.keys())
    shuffle(tour_ids)
    selected_ids = tour_ids[0:6]
    tours = {t_id: data.tours[t_id] for t_id in selected_ids }
    return render_template('index.html', base=data.base, tours=tours)


@app.route('/tour/<tour_id>/')
def tour_route(tour_id):
    return render_template('tour.html', tour=data.tours[int(tour_id)], base=data.base)


@app.route('/departure/<city_from>/')
def departure_route(city_from='msk'):
    tours = {key: tour for key, tour in data.tours.items() if tour['departure'] == city_from}
    if len(tours) == 0:
        return render_template('departure_no_tours.html', base=data.base, city_from=city_from)

    count = 0
    max_price, min_price, max_nights, min_nights = None, None, None, None

    for tour in tours.values():
        count += 1
        max_price = max(tour['price'], max_price) if max_price else tour['price']
        min_price = min(tour['price'], min_price) if min_price else tour['price']
        max_nights = max(tour['nights'], max_nights) if max_nights else tour['nights']
        min_nights = min(tour['nights'], min_nights) if min_nights else tour['nights']

    stats = {
        'count': count,
        'max_price': max_price,
        'min_price': min_price,
        'max_nights': max_nights,
        'min_nights': min_nights,
    }

    return render_template(
        'departure.html',
        base=data.base,
        city_from=city_from,
        tours=tours,
        stats=stats
    )


if __name__ == '__main__':
    app.run(debug=True)
