url = 'https://www.m-files.com/product-downloads/download-update-links/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
version_xpath = '//*[@id="block_83a55924d6f4e44fcfaa0aac11117510"]/div/h2'

pics_path = './screenshots/'
txts_path = './texts/'

welcome_message = """
At your service, sir.
"""

helper_links = """
<u><b>Useful Websites</b></u>

<a href='https://userguide.m-files.com/user-guide/latest/eng/'>M-Files User Guide</a>
<a href='https://kb.cloudvault.m-files.com/#3ECA226F-7B54-428B-B539-DE443E6134EC/views/V221'>M-Files KnowledgeBase</a>

<a href='https://developer.m-files.com/'>M-Files Developer</a>
<a href='https://developer.m-files.com/APIs/COM-API/Reference/#introduction.html'>M-Files API</a>
<a href='https://www.m-files.com/product-downloads/download-update-links/'>M-Files Download</a>
"""

# Buttons Definitions
btn_01 = "Search_Condition"
btn_02 = "Create_Object"
btn_03 = "Set_Last_Editor"
btn_04 = "Set_Property"
btn_05 = "Get_Property"
btn_06 = "Running_Number"
btn_07 = "Property_Validation"
btn_08 = "Property_Control"
btn_09 = "Set_Other_Object_Property"
btn_10 = "Upper_Case"
btn_11 = "Inside_Parentheses"
btn_12 = "Phone_Formatter"
btn_13 = "Inline_If"
btn_14 = "Send_Mail"
btn_15 = "Remove_HTML_Tags"
btn_16 = "Check_TCKN"
btn_17 = "Get_Date"


buttons = [btn_01, btn_02, btn_03, btn_04, btn_05, btn_06, btn_07, btn_08, btn_09, btn_10, btn_11, btn_12, btn_13, btn_14, btn_15, btn_16, btn_17]
