import data
import sender_stand_request


def test_create_order_and_get_by_track():

    create_response = sender_stand_request.create_order(data.ORDER_BODY)

    track = create_response.json()["track"]

    get_response = sender_stand_request.get_order_by_track(track)

    assert get_response.status_code == 200
