# Drive Test Conqueror
> Drive Test Conqueror 是一個透過多種項目幫助用戶考取駕照的服務，以 Django 和 Vue 兩種框架整合開發而成

## 執行方式
```
// 後端套件安裝

cd dtc_server
pip install -r requirements.txt

// 前端套件安裝

cd dtc_server/dtc_vue
npm install

or

cd dtc_server/dtc_vue
yarn install

// 伺服器運行

cd dtc_server/dtc_vue
npm build
cd ..
python manage.py migrate
python manage.py runserver
```

## 專案特色

### 已實現

- 服務網站首頁(各項目連結)
- (部分)駕照題庫參閱
- 模擬筆試測驗
- 交通號誌辨識

### 未實現

- 完整存取所有題庫
- 抽換/優化號誌辨識模組
