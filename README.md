# car_task
GET request example with filters:
  http://127.0.0.1:8000/api/car_list?mark=Toyota&car_model=Camry&max_price=13000000&max_mileage=20000

result:
  {
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 39,
            "car_model": "Camry",
            "mark": "Toyota",
            "price": 12950000,
            "mileage": 6500,
            "year_manufactured": 2020
        },
        {
            "id": 86,
            "car_model": "Camry",
            "mark": "Toyota",
            "price": 12600000,
            "mileage": 9500,
            "year_manufactured": 2020
        }
    ]
}
