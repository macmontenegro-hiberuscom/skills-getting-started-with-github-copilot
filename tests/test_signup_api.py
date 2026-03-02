def test_signup_success_adds_participant(client):
    activity_name = "Chess Club"
    new_email = "new.student@mergington.edu"

    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": new_email},
    )

    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json

    activities_response = client.get("/activities")
    assert activities_response.status_code == 200
    activities_json = activities_response.json()
    assert new_email in activities_json[activity_name]["participants"]


def test_signup_fails_for_nonexistent_activity(client):
    response = client.post(
        "/activities/Nonexistent Club/signup",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    response_json = response.json()
    assert "detail" in response_json


def test_signup_fails_for_duplicate_participant(client):
    existing_email = "michael@mergington.edu"

    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": existing_email},
    )

    assert response.status_code == 400
    response_json = response.json()
    assert "detail" in response_json


def test_signup_fails_when_email_is_missing(client):
    response = client.post("/activities/Chess Club/signup")

    assert response.status_code == 422
