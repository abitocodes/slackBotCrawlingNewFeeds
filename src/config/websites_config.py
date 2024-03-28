websites = [
    {
        "name": "KISA 한국인터넷진흥원>알림마당>공지사항",
        "url": "https://www.kisa.or.kr/401?page=1&searchDiv=30&searchWord=%EB%B8%94%EB%A1%9D%EC%B2%B4%EC%9D%B8&_csrf=e3d30d8e-8d61-4b41-b096-efef607dfcfb",
        "base_url": "https://www.kisa.or.kr",
        "selector": "tbody tr:not(.notice)", 
        "title_selector": "td.sbj.txtL a", 
        "date_selector": "td.date",
        "crawling": "true",
        "selenium": "false",
    },
    {
        "name": "KISA 한국인터넷진흥원>알림마당>입찰공고",
        "url": "https://www.kisa.or.kr/403?page=1&searchDiv=30&searchWord=%EB%B8%94%EB%A1%9D%EC%B2%B4%EC%9D%B8&_csrf=26bd1a90-afef-4a56-8ad9-58d237afca3a",
        "base_url": "https://www.kisa.or.kr",
        "selector": "tbody tr:not(.notice)", 
        "title_selector": "td.sbj.txtL a", 
        "date_selector": "td.date",
        "crawling": "true",
        "selenium": "false",
    },
    {
        "name": "국가과학기술지식정보서비스(NTIS)>국가R&D통합공고",
        "url": "https://www.ntis.go.kr/rndgate/eg/un/ra/mng.do",
        "base_url": "https://www.ntis.go.kr",
        "selector": "table.basic_list tbody tr",
        "title_selector": "td[data-title='공고명'] a",
        "date_selector": "td[data-title='순번']", # 게시글을 눌러서 들어가야만 공고일이 보여서, 순번으로 대체.
        "crawling": "true",
        "selenium": "true",
        "selenium_inputBoxId": "searchKeyword",
        "selenium_searchBtnXpath": '//a[@onclick="javascript: fn_search(\'1\', \'\'); return false;"]',
        "selenium_keyword": "블록체인"
    },
]