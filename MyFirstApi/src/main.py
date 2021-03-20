def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    from flask import abort, Response
    import json

    def gen_price(area):
        return area * 2

    if request.method == 'GET':
        area = int(request.args.get('area'))

        response = Response(
            response=json.dumps({'price': gen_price(area)}),
            mimetype='application/json'
        )
        response.headers['Content-Type'] = 'application/json; charset=utf-8'

        return response
    elif request.method == 'POST':

        areas = request.json['areas']
        areas = set([area['area'] for area in areas])

        response = {'prices': [{'area': area, 'price': gen_price(area)} for area in areas]}
        response = Response(
            response=json.dumps(response),
            mimetype='application/json'
        )
        response.headers['Content-Type'] = 'application/json; charset=utf-8'

        return response
    else:
        return abort(405)
