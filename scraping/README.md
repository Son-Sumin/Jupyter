***[기본세팅](https://github.com/Son-Sumin/ml_dl/blob/main/%EC%B4%88%EA%B8%B0%EC%84%A4%EC%A0%95.md) 설치 후 아래 내용 설치 권장** *

## Scraping에서 배운 내용   
BeautifulSoup, selenium, folium, google geocoding api   
  **google geocoding 사용 시 key 삭제 후 공유할 것!!**   
<br>

## Scraping 폴더 실시한 설치사항

- #### Window terminal
  ```
  (ml-env) 환경 확인 후  
   - 원하는 사이트 소스 갖고올 수 있도록 설치   
   $ conda install -c anaconda requests

   - html 파싱 역할   
   $ conda install bs4   

   - 파서 장착   
   $ conda install lxml

   - 해당 사이트의 팝업을 지우고 특정 베너를 클릭하여 들어가는 역할 : selenium  
   $ conda install -c conda-forge selenium  
  ```

- #### Server
  - chromedriver 다운로드(selenium을 구글에서 사용할 것이므로)   
    chromedriver 구글링 후 다운로드 페이지 접속(https://chromedriver.chromium.org/downloads)   
    크롬 설정 → (좌측베너)크롬 정보 → 크롬 버전 확인 후 버전에 맞는 것 다운로드 →    
    다운 시 파일 위치 확인


- #### Window terminal
  ```
  (ml-env) 환경 확인 후  
  - 로딩 시간을 보여주는 진행도를 가시적으로 확인 가능   
  $ conda install tqdm     

  - 오픈맵 사용 시 (오픈맵을 사용하기 위해 folium 설치)   
    (에러 시 Window terminal 관리자 버전 (ml-env) 에서 실행)   
  $ conda install -c conda-forge folium   
  $ conda install -c conda-forge googlemaps
  ```

- #### Server
  - google geocoding api 구글링하여 계정 등록 후 구글맵 사용
