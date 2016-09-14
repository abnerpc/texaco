class TestViews(object):

    def test_404(self, app_client):
        response = app_client.get('/wrong/url')
        assert response.status_code == 404

    def test_index(self, app_client):
        response = app_client.get('/')
        assert response.status_code == 200
