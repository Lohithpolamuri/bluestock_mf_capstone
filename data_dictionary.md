Data Dictionary

fund_master
- amfi_code : Unique fund code
- scheme_name : Name of the scheme
- fund_house : Fund company
- category : Fund category
- risk_category : Risk level

nav_history
- amfi_code : Fund code
- date : NAV date
- nav : Net Asset Value

investor_transactions
- investor_id : Investor ID
- transaction_date : Transaction date
- transaction_type : SIP / Lumpsum / Redemption
- amount_inr : Transaction amount
- state : Investor state
- kyc_status : KYC verification status

scheme_performance
- return_1yr_pct : 1 year return
- return_3yr_pct : 3 year return
- return_5yr_pct : 5 year return
- expense_ratio_pct : Expense ratio
- risk_grade : Risk grade