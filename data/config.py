"""
Define global config variables for use in finlit scripts and notebooks.
"""

TREATMENT_COLS =  ['FIN_ED_HS']   #M20 overall can be a second option with maybe more power?

OUTCOME_VARS = ['SATISFACTION_WITH_FINANCIAL_CONDITION', 
            'SPENDING_COMPARISON_TO_INCOME', 
            'DIFFICULTY_COVERING_EXPENSES', 'FIN_ANXIETY',
            'EMERGENCY_FUNDS', 'CONFIDENCE_GET_2000', 
            'CREDIT_RECORD_RATING', 'CHECKING_ACCOUNT', 'SAVINGS_ACCOUNT',
            'OVERDRAW_CHECKING_ACCOUNT', 'REGULAR_CONTRIBUTION_TO_RETIREMENT',
            'OTHER_INVESTMENTS', 'ALWAYS_PAY_CR_FULL_12MO', 
            'USED_PAYDAY_LOAN', 
            'DEBT_COLLECTED_12MO', 'TOO_MUCH_DEBT_STRENGTH',
            'D2D_FINANCIAL_SKILL', 'FINANCIAL_KNOWLEDGE_ASSESS',]   

COVARIATES = [ 'RACE_ETHNICITY', 'EDUCATION_LEVEL',
                    'HIGHEST_EDUCATION_OF_RAISERS', 'NUM_DEPENDENT_CHILDREN',
                    'BINARIZED_GENDER', 'AGE', 'LAYOFF_PANDEMIC', 
                    'EXPECT_INHERIT_10K_PLUS', 'STATE']  #need to dummy/ factor all of these, poor value orderingf

COLUMN_MAP = {
    'A2': 'ZIP_CODE',
    'STATEQ': 'STATE',
    'A50': 'GENDER',  # 1 MAN, 2 WOMAN, 3 OTHER   #---- Covariate
    'A50A': 'BINARIZED_GENDER',  # 1 MAN, 2 WOMAN  
    'A3Ar_w': 'AGE',  # AGE IN YEARS (13-101, 999 FOR PREFER NOT TO SAY)   #---- Covariate 
    'A50B': 'GENDER/AGE NET',  # GENDER AND AGE COMBINATION 
    'A4A_new_w': 'RACE_ETHNICITY',  # 1 WHITE, 2 BLACK, 3 HISPANIC, 4 ASIAN, 5 NATIVE HAWAIIAN/OTHER PACIFIC ISLANDER, 6 OTHER, 99 PREFER NOT TO SAY 
    'A4A': 'ETHNICITY_QUOTA',  # 1 WHITE NON-HISPANIC, 2 BLACK NON-HISPANIC, 3 HISPANIC (ALONE OR IN COMBINATION), 4 ASIAN/PACIFIC ISLANDER NON-HISPANIC, 5 OTHER NON-HISPANIC (AMERICAN INDIAN, OTHER, 2+ ETHNICITIES)
    'A51': 'IDENTIFY_HERITAGE_BLACK',  # Column for Q.A51
    'A52': 'IDENTIFY_HERITAGE_HISPANIC',  # Column for Q.A52
    'A53': 'IDENTIFY_HERITAGE_ASIAN_PACIFIC_ISLANDER',  # Column for Q.A53
    'A5_2015': 'EDUCATION_LEVEL',  # Column for Q.A5
    'A6': 'MARITAL_STATUS',  # Column for Q.A6
    'A7': 'LIVING_ARRANGEMENTS',  # Column for Q.A7
    'A7A': 'MARITAL_STATUS_VARIABLE',  # Column for Q.A7a
    'A7AA': 'SPOUSE_OR_PARTNER',  # Column for Q.A7aa
    'A11': 'NUM_DEPENDENT_CHILDREN',  # Column for Q.A11
    'A8': 'APPROX_ANNUAL_INCOME',  # Column for Q.A8
    'AM21': 'ARMED_SERVICES_MEMBERSHIP',  # Column for Q.AM21
    'X3': 'QUESTIONNAIRE_VERSION',  # Column for Q.X3 core [1], military [2]
    'A9': 'EMPLOYMENT_STATUS',  # Column for Q.A9
    'A40': 'OTHER_WORK_IN_PAST_12_MONTHS',  # Column for Q.A40
    'A10': 'SPOUSE_EMPLOYMENT_STATUS',  # Column for Q.A10
    'A10A': 'HOUSEHOLD_RETIREMENT_STATUS',  # Column for Q.A10a
    'A21_2015': 'PART_TIME_STUDENT',  # Column for Q.A21 who in household is more knowledgeable
    'A14': 'KNOWLEDGE_ABOUT_FINANCE',  # Column for Q.A14
    'A41': 'HIGHEST_EDUCATION_OF_RAISERS',  # Column for Q.A41
    'JA': 'FINANCIAL_ATTITUDES_BEHAVIORS',  # Column for SECTION JA
    'J1': 'SATISFACTION_WITH_FINANCIAL_CONDITION',  # Column for Q.J1
    'J2': 'WILLINGNESS_TO_TAKE_RISKS',  # Column for Q.J2
    'J3': 'SPENDING_COMPARISON_TO_INCOME',  # Column for Q.J3
    'J4': 'DIFFICULTY_COVERING_EXPENSES',  # Column for Q.J4
    'J40': 'INCOME_VARIABILITY',  # Column for Q.J40
    'J5': 'EMERGENCY_FUNDS',  # Column for Q.J5
    'J6': 'SAVING_FOR_CHILDRENS_EDUCATION',  # Column for Q.J6
    'J8': 'FIGURING_OUT_RETIREMENT_SAVING',  # Column for Q.J8
    'J9': 'FIGURING_OUT_RETIREMENT_BEFORE_RETIREMENT',  # Column for Q.J9
    'J10': 'EXPERIENCED_LARGE_INCOME_DROP',  # Column for Q.J10
    'J20': 'CONFIDENCE_GET_2000',  # Column for Q.J20
    'J50': 'RECEIVED_STIMULUS_PAYMENT',  # Column for Q.J50
    'J51': 'USE_OF_STIMULUS_PAYMENT',  # Column for Q.J51
    'J52': 'LAYOFF_PANDEMIC',  # Column for Q.J52
    'J32': 'CREDIT_RECORD_RATING',  # Column for Q.J32
    'J33_40': 'FIN_ANXIETY',  # Column for Q.J33
    'J53': 'FREQUENCY_OF_THINKING_ABOUT_FINANCES',  # Column for Q.J53
    'J41': 'MONEY_SITUATION_DESCRIPTION',  # Column for Q.J41
    'J42': 'STATEMENTS_APPLICATION_FREQUENCY',  # Column for Q.J42
    'J43': 'FIN_CONFIDENCE',  # Column for Q.J43
    'B1': 'CHECKING_ACCOUNT',  # Column for Q.B1
    'B2': 'SAVINGS_ACCOUNT',  # Column for Q.B2
    'B4': 'OVERDRAW_CHECKING_ACCOUNT',  # Column for Q.B4
    'B14': 'OTHER_INVESTMENTS',
    'B41_1': 'ONLINE_BANKING',  # Column for Q.B41_1
    'B41_2': 'MOBILE_BANKING',  # Column for Q.B41_2
    'B31': 'MOBILE_PAYMENT_IN_PERSON',  # Column for Q.B31
    'B42': 'MOBILE_TRANSFER_TO_ANOTHER_PERSON',  # Column for Q.B42
    'B43': 'USE_WEBSITES_APPS_FINANCIAL_TASKS',  # Column for Q.B43
    'C2': 'PLANS_PROVIDED_BY_EMPLOYER',  # Column for Q.C2
    'C3': 'PLANS_WITH_INVESTMENT_CHOICE',  # Column for Q.C3
    'C4': 'OTHER_RETIREMENT_ACCOUNTS',  # Column for Q.C4
    'C5_2012': 'REGULAR_CONTRIBUTION_TO_RETIREMENT',  # Column for Q.C5
    'C10': 'LOAN_FROM_RETIREMENT_ACCOUNT',  # Column for Q.C10
    'C11': 'HARDSHIP_WITHDRAWAL_FROM_RETIREMENT_ACCOUNT',  # Column for Q.C11
    'EA_1': 'CURRENTLY_OWN_HOME',  # Column for Q.Ea_1
    'E7': 'CURRENTLY_HAVE_MORTGAGES',  # Column for Q.E7
    'E8': 'CURRENTLY_HAVE_HOME_EQUITY_LOANS',  # Column for Q.E8
    'E20': 'OWE_MORE_THAN_HOME_VALUE',  # Column for Q.E20
    'E15': 'Late Mortgage Payments (Past 12 Months)',  # Values: 1-Never, 2-Once, 3-More than once, 98-Don’t know, 99-Prefer not to say
    'P50': 'Parents/Grandparents Paid $10,000 or More (Anytime in Adult Life)',  # Values: 1-Yes, 2-No, 98-Don’t know, 99-Prefer not to say
    'P51': 'Received Gift $10,000 or More (Not an Inheritance)',  # Values: 1-Yes, 2-No, 98-Don’t know, 99-Prefer not to say
    'P52': 'EXPECT_INHERIT_10K_PLUS',  # Values: 1-Yes, 2-No, 98-Don’t know, 99-Prefer not to say
    'F1': 'Number of Credit Cards',  # Values: 1, 2-3, 4-8, 9-12, 13-20, More than 20, 7-No credit cards, 98-Don’t know, 99-Prefer not to say
    'F2_1': 'ALWAYS_PAY_CR_FULL_12MO',  # Values: 1-Yes, 2-No, 98-Don’t know, 99-Prefer not to say
    'F2_2': 'Carried Over a Balance and Was Charged Interest',  # Values: 1-Yes, 2-No, 98-Don’t know, 99-Prefer not to say
    'F2_3': 'Paid Minimum Payment Only in Some Months',  # Values: 1-Yes, 2-No, 98-Don’t know, 99-Prefer not to say
    'F2_4': 'Charged Late Fee for Late Payment in Some Months',  # Values: 1-Yes, 2-No, 98-Don’t know, 99-Prefer not to say
    'F2_5': 'Charged Over-the-Limit Fee for Exceeding Credit Line in Some Months',  # Values: 1-Yes, 2-No, 98-Don’t know, 99-Prefer not to say
    'F2_6': 'Used Cards for Cash Advance in Some Months',  # Values: 1-Yes, 2-No, 98-Don’t know, 99-Prefer not to say
    'G1': 'Auto Loan',  # Values: 1-Yes, 2-No, 98-Don’t know, 99-Prefer not to say
    'G20': 'Unpaid Bills from Health Care or Medical Service Provider',  # Values: 1-Yes, 2-No, 98-Don’t know, 99-Prefer not to say
    'G30': 'Student Loans for Whose Education',  # Values: 1-Yourself, 2-Your spouse/partner, 3-Your child(ren), 4-Your grandchild(ren), 5-Other person, 97-No student loans, 98-Don’t know, 99-Prefer not to say
    'G33': 'Did You Figure Out Monthly Payments Before Most Recent Student Loan',  # Values: 1-Yes, 2-No, 98-Don’t know, 99-Prefer not to say
    'G35': 'LATE_WITH_STUDENT_LOAN_12MO',  # Values: 1-Never, payments not due; 2-Never, repaying on time; 3-Once; 4-More than once; 98-Don’t know; 99-Prefer not to say
    'G22': 'Concerned about Paying Off Student Loans',  # Values: 1-Yes, 2-No, 98-Don’t know, 99-Prefer not to say
    'G25_1': 'Taken Out an Auto Title Loan',  # Values: 1-Never, 2-1 time, 3-2 times, 4-3 times, 5-4 or more times, 98-Don’t know, 99-Prefer not to say
    'G25_2': 'USED_PAYDAY_LOAN',  # Values: 1-Never, 2-1 time, 3-2 times, 4-3 times, 5-4 or more times, 98-Don’t know, 99-Prefer not to say
    'G25_3': 'Gotten an Advance on Tax Refund',  # Values: 1-Never, 2-1 time, 3-2 times, 4-3 times, 5-4 or more times, 98-Don’t know, 99-Prefer not to say
    'G25_4': 'Used a Pawn Shop',  # Values: 1-Never, 2-1 time, 3-2 times, 4-3 times, 5-4 or more times, 98-Don’t know, 99-Prefer not to say
    'G25_5': 'Used a Rent-to-Own Store',  # Values: 1-Never, 2-1 time, 3-2 times, 4-3 times, 5-4 or more times, 98-Don’t know, 99-Prefer not to say
    'G38': 'DEBT_COLLECTED_12MO',  # Values: 1-Yes, 2-No, 98-Don’t know, 99-Prefer not to say
    'G23': 'TOO_MUCH_DEBT_STRENGTH',  # Values: 1-7 (Strongly Disagree to Strongly Agree), 98-Don’t know, 99-Prefer not to say
    'H1': 'Health Insurance Coverage',  # Values: 1-Yes, 2-No, 98-Don’t know, 99-Prefer not to say
    'H30_1': 'Not Filling Prescription Due to Cost',  # Values: 1-Yes, 2-No, 98-Don’t know, 99-Prefer not to say
    'H30_2': 'Skipping Medical Test, Treatment, or Follow-up Due to Cost',  # Values: 1-Yes, 2-No, 98-Don’t know, 99-Prefer not to say
    'H30_3': 'Not Visiting Doctor or Clinic Due to Cost',  # Values: 1-Yes, 2-No, 98-Don’t know, 99-Prefer not to say
    'M1_1': 'D2D_FINANCIAL_SKILL',  # Values: 1-7, 98-Don’t know, 99-Prefer not to say
    'M1_2': 'Math Proficiency',  # Values: 1-7, 98-Don’t know, 99-Prefer not to say
    'M4': 'FINANCIAL_KNOWLEDGE_ASSESS',  # Values: 1-7, 98-Don’t know, 99-Prefer not to say
    'M20': 'FIN_ED_ALL',  # Values: 1-Yes (did not participate), 2-Yes (participated), 3-No, 98-Don’t know, 99-Prefer not to say
    'M21_1': 'FIN_ED_HS',  # Values: 1-Yes, 2-No, 98-Don’t know, 99-Prefer not to say
    'M21_2': 'Received Financial Education in College',  # Values: 1-Yes, 2-No, 98-Don’t know, 99-Prefer not to say
    'M21_3': 'Received Financial Education from Employer',  # Values: 1-Yes, 2-No, 98-Don’t know, 99-Prefer not to say
    'M21_4': 'Received Financial Education from Military',  # Values: 1-Yes, 2-No, 98-Don’t know, 99-Prefer not to say
    'M6': 'Expected Growth of Savings in 5 Years',  # Values: 1-More than $102, 2-Exactly $102, 3-Less than $102, 98-Don’t know, 99-Prefer not to say
    'M7': 'Effect of Inflation on Purchasing Power',  # Values: 1-More than today, 2-Exactly the same, 3-Less than today, 98-Don’t know, 99-Prefer not to say
    'M8': 'Relationship Between Interest Rates and Bond Prices',  # Values: 1-They will rise, 2-They will fall, 3-They will stay the same, 4-There is no relationship, 98-Don’t know, 99-Prefer not to say
    'M31': 'Years to Double Loan at 20% Interest Rate',  # Values: 1-Less than 2 years, 2-2 to 5 years, 3-5 to 10 years, 4-At least 10 years, 98-Don’t know, 99-Prefer not to say
    'M50': 'Highest Probability of Getting a Disease',  # Values: 1-One-in-twenty chance, 2-2% of the population, 3-25 out of 1,000 people, 98-Don’t know, 99-Prefer not to say
    'M9': 'True or False: 15-year Mortgage vs. 30-year Mortgage',  # Values: 1-True, 2-False, 98-Don’t know, 99-Prefer not to say
    'M10': 'True or False: Single Company’s Stock vs. Stock Mutual Fund',  # Values: 1-True, 2-False, 98-Don’t know, 99-Prefer not to say
    #N questions seem to have been dropped from the actual data
    'N51': 'Tested Positive or Diagnosed with COVID-19',  # Values: 1-Yes, 2-No, 98-Don’t know, 99-Prefer not to say
    'N52': 'SEX_ORIENT',  # Values: 1-Straight or heterosexual, 2-Lesbian, 3-Gay, 4-Bisexual, 5-Transgender, 6-Something else, 98-I don’t know the answer, 99-Prefer not to say
    'N31': 'Deaf or Difficulty Hearing',  # Values: 1-Yes, 2-No, 99-Prefer not to say
    'N32': 'Blind or Difficulty Seeing with Glasses',  # Values: 1-Yes, 2-No, 99-Prefer not to say
    'N33': 'Difficulty Concentrating, Remembering, or Making Decisions',  # Values: 1-Yes, 2-No, 99-Prefer not to say
    'N34': 'Difficulty Walking or Climbing Stairs',  # Values: 1-Yes, 2-No, 99-Prefer not to say
    'N35': 'Difficulty Dressing or Bathing',  # Values: 1-Yes, 2-No, 99-Prefer not to say
    'N36': 'Difficulty Doing Errands Alone',  # Values: 1-Yes, 2-No, 99-Prefer not to say  
}