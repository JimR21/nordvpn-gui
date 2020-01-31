import requests

api = "https://api.nordvpn.com/server"


class NordApi(object):
    def get_api_data(self):
        try:
            resp = requests.get(api, timeout=5)
            if resp.status_code == requests.codes.ok:
                return resp.json()
            else:
                print('Get API failed')
        except Exception as ex:
            print('Get API failed')

    def get_country_list(self, api_data):
        countries_list = []
        for server in api_data:
            country = server['country']
            if country not in countries_list:
                countries_list.append(country)
        return sorted(countries_list)

    def get_servers_by_country(self, api_data, country):
        server_list = []
        for server in api_data:
            server_country = server['country']
            if server_country == country:
                server_list.append(server)
        return server_list


# nordApi = NordApi()
# apiData = nordApi.get_api_data()
# servers = nordApi.get_servers_by_country(apiData, "United States")
# for server in servers:
#     print(server)
