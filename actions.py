# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from tabulate import tabulate
from rasa_sdk.events import FollowupAction


class ActionOutdoor(Action):

    def name(self) -> Text:
        return "action_Outdoor"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="OD is Outdoor application. If employees are working out of office to mark his/her attendance it is needed")

        return []


class ActionODApplication(Action):

    def name(self) -> Text:
        return "action_OutdoorApplication"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="• Go to https://pulse.Company.com/ \
                                        • Select ESS Click on it and login with AD credentials \
                                        • Select a menu “Attendance” and select “My OD Applications” \
                                        • Click on “Apply for new OD application • Select date and click on “Go” \
                                        • Fill the information and click on “submit” ")
        return []


class Actionpayslip(Action):

    def name(self) -> Text:
        return "action_payslip"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="• Go to https://pulse.company.com/ \
                                         • Select ESS based on your organization like ESS \
                                         • Select “Main Menu” and click on “pay slip” option")
        return []


class Actiontax_report(Action):

    def name(self) -> Text:
        return "action_tax_report"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="• Go to  https://pulse.company.com/ \
                                         • Select ESS based on your organization like ESS \
                                         • Select “Main Menu” and click on “My Tax  Report” option")
        return [FollowupAction('utter_followup_response')]


class Actiontax_calculator(Action):

    def name(self) -> Text:
        return "action_tax_calculator"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="• Go to  https://pulse.company.com/ \
                                         • Select ESS based on your organization like ESS \
                                         • Select “Main Menu” and click on “Income Tax Calculator” option")
        return [FollowupAction('utter_followup_response')]


class Actionform16(Action):

    def name(self) -> Text:
        return "action_form16"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="• Go to  https://pulse.company.com/ \
                                         • Select ESS based on your organization like ESS \
                                         • Select “Main Menu” and click on “Form 16” option")
        return [FollowupAction('utter_followup_response')]


class Actions_alary_statement(Action):

    def name(self) -> Text:
        return "action_salary_statement"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="• Go to  https://pulse.company.com/ \
                                         • Select ESS based on your organization like ESS\
                                         • Select “Main Menu” and click on “Annual Salary statement” option")
        return [FollowupAction('utter_followup_response')]


class Actions_personal_details(Action):

    def name(self) -> Text:
        return "action_personal_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="• Go to  https://pulse.com/ \
                                       • Select ESS based on your organization like ESS \
                                       • Select “Main Menu” and click on “Personal details” option \
                                       • Raise a new request for it.")
        return [FollowupAction('utter_followup_response')]


class Actions_medical_emergency(Action):

    def name(self) -> Text:
        return "action_medical_emergency"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=tabulate(
            [['name1', '+91-1234', ' insurance company', 'name1@company.com'],
             ['name2', '+91-745566', ' (TM team)', 'name@company.com']],
            headers=['Contact person', 'Contact number', 'Entity', 'Email id']))
        return []


class Actions_ess(Action):

    def name(self) -> Text:
        return "action_ess"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="ESS is Employee self service.It keeps track of employees attendance and leave management")
        return [FollowupAction('utter_followup_response')]


class Actions_leave(Action):

    def name(self) -> Text:
        return "action_leave"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="• Go to https://pulse.com/ \n• Select ESS Click on it and login with AD credentials \n• Select a menu Leave management Under that click on My leave application \n• Provide required information and click on OK")
        return [FollowupAction('utter_followup_response')]


class Actions_No(Action):

    def name(self) -> Text:
        return "action_no"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        prevAction = getAction.get_last_utter_action(tracker)
        if prevAction == "action_leave" or prevAction == "action_personal_details" or prevAction=="action_ess":
            dispatcher.utter_message(
                text="I am really sorry please contach HR Department or send a mail to HR@company.com")
        elif prevAction == "action_salary_statement" or prevAction == "action_form16" \
                or prevAction == "action_tax_report"or prevAction == "action_tax_calculator":
            dispatcher.utter_message("I am really sorry please contact finance department or send mail to finance@company.com")
        else:
            dispatcher.utter_message(
                text="I am really sorry please contach HR Department or send a mail to dontknow@company.com")
        # dispatcher.utter_message("utter_did_that_help", tracker)
        return []


class getAction():
    def get_last_utter_action(tracker):

        for event in reversed(tracker.events):
            try:
                if event.get('name') not in ['action_listen', None, 'utter_ask_continue','utter_followup_response']:
                    last_utter_action = event.get('name')
                    return last_utter_action
                else:
                    pass
            except:
                pass
        return 'error! no last action found'


class ActionCovid19(Action):
    def name(self) -> Text:
        return "action_covid19"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Coronavirus disease (COVID-19) is an infectious disease caused by a newly\
        discovered coronavirus. \nfor more details you can visit this page https://www.who.int/health-topics/coronavirus")
        return []


class ActionCovidHelpline(Action):
    def name(self) -> Text:
        return "action_covid19_helpline"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="company (24x7) helplines – Facility Team -12334/ IT Team- company\n \
                                Email for escalations - csg-managers@company.com for more info visit this \
                                      page https://pulse.com/covid-19/")
        return []


class ActionVariablePay(Action):
    def name(self) -> Text:
        return "action_variable_pay"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Your variable payment will be divided into 4 tranches. Each tranche will\
       be paid with the salary of the first month of the quarter (April, July, October,\
       and January). \n\nIf the situation improves, the company will definitely check\
       the possibility of paying the variable amount early.\nBut you need to be on\
       the payroll of company on 31/Mar/2021 to be eligible for payment of the CPDS\
       amount.")
        return []


class ActionEmployeeResignation(Action):
    def name(self) -> Text:
        return "action_covid_employee_resignation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="We hope you do not leave us ☺. You have earned your variable pay for FY20.\
      It will be paid to you irrespective of whether you are with the company or not.\
      It will be paid in 4 tranches and not lump sum with F&F.")
        return []


class ActionHikePromotions(Action):
    def name(self) -> Text:
        return "action_covid_hike_promotions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="The salary restructuring has to be reversed first in order to roll back\
       all previous decisions. Hence, it follows that the salary revisions will be\
       on hold until 31/Mar/2021. \n\nHike and promotions are freezed and any announcement\
       on hike and promotions will be made on All Hands meetings in future.")
        return []


class ActionSalaryTax(Action):
    def name(self) -> Text:
        return "action_covid_salary_tax"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="The payroll team will ensure that all tax related compliances are met in\
      both cases.")
        return []


class ActionLayOff(Action):
    def name(self) -> Text:
        return "action_covid_layoff"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="We are moving fast and taking precautionary measures to avoid any such situations.\
      We will make all effort to not let that happen but a lot depends on external business circumstances.")
        return []


class ActionAwardsRecognitions(Action):
    def name(self) -> Text:
        return "action_awards_recognitions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Awards (with the associated amount) will continue. We want to encourage\
      all our star performers, as always!")
        return []


class ActionImpactCompany(Action):
    def name(self) -> Text:
        return "action_covid_impact_Company"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="This decisions taken because of covid are applicable to all employees of\
       company across the globe. The specifics may vary based on local regulations\
       and conditions in different countries. \n\nThe restructuring is applicable\
       to all contractors but not applicable to the interns. \n\nIt is applicable\
       to all employees of company, on leave or on duty.")
        return []


class ActionCPDSCalculation(Action):
    def name(self) -> Text:
        return "action_cpds_amount_calculation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="CPDS amount stated in the restructured salary sheet is annual number effective\
       1st May 2020.\nTherefore, actual amount will be pro-rated for 11 months and\
       will be added as CPDS along with April 2021 salary. Illustration CPDS effective\
       1st May in salary sheet is Rs. 60,000. Actual CPDS distributed amount will\
       be Rs. 60,000 * 11 months / 12 months = Rs. 55,000. \n\n This does not result\
       in any loss because, employee has already received amount for Apr-20 before\
       salary restructure decision was made, in April 2020. Therefore, effective\
       amount that is being deferred is only for 11 months. The same will be paid\
       along with April 2021 salary provided conditions attached to CPDS are met.")
        return []


class ActionSalaryRestructuring(Action):
    def name(self) -> Text:
        return "action_covid_salary_restructuring"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="The ‘conditionally payable deferred salary’ (CPDS) will be clearly indicated\
       in the salary restructuring sheet provided to you by the payroll team. You\
       will receive the due amount in April 2021 if the company achieves a revenue\
       of $30M for the financial year 2021. If the company does not achieve $30M\
       by 31/March/2021 then the CPDS amount gets forfeited. \n\nWe track and present\
       our financial numbers during Company All hands meetings. You can join the\
       meeting and get more details.")
        return []


class ActionYearlyReviews(Action):
    def name(self) -> Text:
        return "action_yearly_reviews"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Performance management is independent of revisions. In fact, appraisal and \
                                       rating data will be a MUST when we resume revisions in the future.\
                                       Please ensure that all your appraisals happen diligently and on time.")
        return []


class ActionRevennueTarget(Action):
    def name(self) -> Text:
        return "action_covid_revenue_target"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="You will receive the due amount in April 2021 if the company achieves a\
                                       revenue of $30M for the financial year 2021.\
                                       We track and present our financial numbers during Company All hands meetings.\
                                       You can join the meeting and get more details.")
        return []


class ActionVpn(Action):

    def name(self) -> Text:
        return "action_utter_vpn"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_vpn")

        return []


class ActionVpn_for_Company_Labs(Action):

    def name(self) -> Text:
        return "action_utter_company"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_company")

        return []


class ActionVpn_for_kpoint(Action):

    def name(self) -> Text:
        return "action_utter_kpoint"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_kpoint")

        return []


class ActionVpn_issues(Action):

    def name(self) -> Text:
        return "action_utter_vpn_issues"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_vpn_issues")

        return []


class ActionVpn_authentication_issue(Action):

    def name(self) -> Text:
        return "utter_vpn_barcode_issue"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_vpn_authentication_issue")

        return []


class ActionVpn_barcode_issue(Action):

    def name(self) -> Text:
        return "utter_vpn_barcode_issue"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_vpn_barcode_issue")

        return []
