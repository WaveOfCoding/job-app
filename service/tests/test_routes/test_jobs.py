

def test_create_job(client):
    data = {
        "title": "SDE super",
        "company": "googlemoogle",
        "company_url": "www.googlemoogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2023-04-19"
    }
    response = client.post("/jobs/create-job/", json=data)
    assert response.status_code == 200
    assert response.json()["company"] == "googlemoogle"
    assert response.json()["description"] == "python"


def test_read_job(client):
    data = {
        "title": "SDE super",
        "company": "googlemoogle",
        "company_url": "www.googlemoogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2023-04-19"
    }
    response = client.post("/jobs/create-job/", json=data)

    response = client.get("/jobs/get/1/")
    assert response.status_code == 200
    assert response.json()['title'] == "SDE super"
