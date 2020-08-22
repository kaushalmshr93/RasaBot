## ess happy scenario
*greet
  - utter_greet
  -utter_howcanihelp
* ess
  - action_ess
## leave management happy
*greet
  - utter_greet
  -utter_howcanihelp
*leave
  - action_leave 
*yes
 - utter_bye
## leave management sad
*greet
  - utter_greet
  -utter_howcanihelp
*leave
  - action_leave
  - action_did_that_help
*no
  - action_no

## about
* about
  -utter_about
## vedas
* vedas
  -utter_vedas  
##greet  
* greet
  - utter_greet
## leave 
* leave
  - action_leave
## Outdoor
* Outdoor
  - action_Outdoor
## odapplication
* OutdoorApplication
  - action_OutdoorApplication
## payslip
* payslip
 - action_payslip
##tax_report
* tax_report
 - action_tax_report 
##tax_calculator
* tax_calculator
 - action_tax_calculator
##form16
* form16
 - action_form16
##salary_statement
* salary_statement
 - action_salary_statement
##personal_details
*personal_details
 - action_personal_details
##medical_emergency
*medical_emergency
 -action_medical_emergency 
## goodbye
* bye
  - utter_bye


##action_covid_impact_Company
* covid_impact_Company
  - action_covid_impact_Company

##action_covid_revenue_target
* covid_revenue_target
  - action_covid_revenue_target

##action_yearly_reviews
* yearly_reviews
  - action_yearly_reviews

##action_covid_salary_restructuring
* covid_salary_restructuring
  - action_covid_salary_restructuring 

##action_cpds_amount_calculation
* cpds_amount_calculation
  - action_cpds_amount_calculation

##action_awards_recognitions
* awards_recognition
  - action_awards_recognitions

##action_covid_layoff
* covid_layoffs
  - action_covid_layoff

##action_covid_salary_tax
* covid_salary_tax
  - action_covid_salary_tax

##action_covid_employee_resignation
* covid_employee_resignation
  - action_covid_employee_resignation

##action_variable_pay
* variable_pay
  - action_variable_pay

##action_covid19_helpline
* covid19_helpline
  - action_covid19_helpline

## action_covid19
* covid19
  - action_covid19
## Insurance policy
* policy
  - utter_inssurance_policy

## Insurance policy claim
* inssurance_policy_claim
  - utter_inssurance_policy_claim

## Claim Registeration
* claim_registeration
  - utter_claim_registeration

## Documents for insurance
* documents_required_for_insurance
  - utter_inssurance_documents

## Add memmber in Insurance policy
* add_member_in_insurance_policy
  - utter_add_member
  
## vpn
* vpn
	- utter_vpn

## vpn_for_GS_Labs
* vpn_for_GS_Labs
	- utter_GS_Labs


## vpn_for_kpoint
* vpn_for_kpoint
	- utter_kpoint
	
## vpn_issues
* vpn_issues
	- utter_vpn_issues

## vpn_authentication_issue
* vpn_authentication_issue
	- utter_vpn_authentication_issue
	
## vpn_barcode_issue
* vpn_barcode_issue
	- utter_vpn_barcode_issue
