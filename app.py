import helpers
# import from packages
# absolute path
from utilities import api_interactions_v1, api_interactions_v2
# relative (. - current directory, .. - go to parent directory) 
# from . import api_interactions_v1, api_interactions_v2


def main():
    print("Main module is executed!")
    
    helpers.greet("Alice")
    result = helpers.calculate_rect_area(10, 5)
    print(f"Result: {result}")
    print(f"URL: {helpers.URL}")
    
    # import from package
    api_interactions_v1.api_v1_request()
    api_interactions_v2.api_v2_request()
    
    

if __name__ == "__main__":
    main()