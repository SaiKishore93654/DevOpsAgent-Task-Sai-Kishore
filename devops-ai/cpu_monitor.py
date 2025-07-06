import requests

PROMETHEUS_URL = "http://localhost:9090/api/v1/query"

def get_cpu_usage():
    query = '100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[1m])) * 100)'
    try:
        response = requests.get(PROMETHEUS_URL, params={'query': query})
        result = response.json()["data"]["result"]

        if not result:
            print(" No CPU metrics found from Prometheus.")
            return 0.0

        value = float(result[0]["value"][1])
        return value
    except Exception as e:
        print(f" Error fetching CPU usage: {e}")
        return 0.0

#  Test block
if __name__ == "__main__":
    cpu = get_cpu_usage()
    print(f" CPU Usage: {cpu:.2f}%")