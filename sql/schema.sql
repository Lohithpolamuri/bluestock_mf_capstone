CREATE TABLE fund_master (
    amfi_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    risk_category TEXT
);

CREATE TABLE nav_history (
    amfi_code INTEGER,
    date TEXT,
    nav REAL
);

CREATE TABLE investor_transactions (
    investor_id TEXT,
    transaction_date TEXT,
    amfi_code INTEGER,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city TEXT,
    kyc_status TEXT
);

CREATE TABLE scheme_performance (
    amfi_code INTEGER,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    expense_ratio_pct REAL,
    risk_grade TEXT
);