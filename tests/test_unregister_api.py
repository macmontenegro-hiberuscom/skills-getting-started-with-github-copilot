def test_unregister_success_removes_participant(client):
    activity_name = "Chess Club"
    existing_email = "michael@mergington.edu"

    response = client.delete(
        f"/activities/{activity_name}/participants/{existing_email}",
    )

    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json

    activities_response = client.get("/activities")
    assert activities_response.status_code == 200
    activities_json = activities_response.json()
    assert existing_email not in activities_json[activity_name]["participants"]


def test_unregister_fails_for_nonexistent_activity(client):
    response = client.delete(
        "/activities/Nonexistent Club/participants/student@mergington.edu",
    )

    assert response.status_code == 404
    response_json = response.json()
    assert "detail" in response_json


def test_unregister_fails_for_missing_participant(client):
    response = client.delete(
        "/activities/Chess Club/participants/not-registered@mergington.edu",
    )

    assert response.status_code == 404
    response_json = response.json()
    assert "detail" in response_json
