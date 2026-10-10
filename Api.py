import requests

def fetch_random_user():
      url=" https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
      response=requests.get(url)
      data=response.json()
      
      if data["success"] and "data" in data:
            user_data=data["data"]
            print(f"joke: {user_data['content']}")
            return data
      else:
            raise Exception("Failed to fetch data")


def main():
      try:
            fetch_random_user()
      except Exception as e:
            print(str(e))

if __name__ == "__main__":
      main()