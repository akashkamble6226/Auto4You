import nexmo

client = nexmo.Client(key='e4d6322c',secret='kMwu0Ywt70W0vuZp')

client.send_message(

    {
        'from':'Nexmo',
        'to':'918605719895,917387148102',
        'text':'Hello world',
    }
)