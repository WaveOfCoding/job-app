from fastapi import status


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


def test_read_all_jobs(client):
    data = {
        "title": "SDE super",
        "company": "googlemoogle",
        "company_url": "www.googlemoogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2023-04-26",
    }
    client.post("/jobs/create-job/", json=data)
    client.post("/jobs/create-job/", json=data)

    response = client.get("/jobs/all/")
    assert response.status_code == 200
    assert response.json()[0]
    assert response.json()[1]


def test_update_a_job(client):
    data = {
        "title": "New Job super",
        "company": "googlemoogle",
        "company_url": "www.googlemoogle.com",
        "location": "USA,NY",
        "description": "fastapi",
        "date_posted": "2023-04-27"
    }
    client.post("/jobs/create-job/", json=data)
    data["title"] = "test new title"
    response = client.put("/jobs/update/1", json=data)
    assert response.json()["msg"] == "Successfully updated data."


def test_delete_a_job(client):  # new
    data = {
        "title": "New Job super",
        "company": "googlemoogle",
        "company_url": "www.googlemoogle.com",
        "location": "USA,NY",
        "description": "fastapi",
        "date_posted": "2023-05-04"
    }
    client.post("/jobs/create-job/", json=data)
    msg = client.delete("/jobs/delete/1")
    response = client.get("/jobs/get/1/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
