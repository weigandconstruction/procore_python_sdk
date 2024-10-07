# CompanyUser6

Company User

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | User address | [optional] 
**avatar** | **str** | User avatar url | [optional] 
**business_phone** | **str** | User business phone | [optional] 
**business_phone_extension** | **int** | User business phone extension | [optional] 
**city** | **str** | User city | [optional] 
**country_code** | **str** | User country code (ISO-3166 Alpha-2 format) | [optional] 
**email_address** | **str** | User email | [optional] 
**email_signature** | **str** | User email signature | [optional] 
**employee_id** | **str** | User employee id | [optional] 
**erp_integrated_accountant** | **bool** | User ERP integrated accountant status | [optional] 
**fax_number** | **str** | User fax number | [optional] 
**first_name** | **str** | User first name | [optional] 
**id** | **int** | User id | [optional] 
**initials** | **str** | User initials | [optional] 
**is_active** | **bool** | User active status | [optional] 
**is_employee** | **bool** | User employee status | [optional] 
**job_title** | **str** | User job title | [optional] 
**last_login_at** | **datetime** | User last login at | [optional] 
**last_name** | **str** | User last name | [optional] 
**mobile_phone** | **str** | User mobile phone | [optional] 
**name** | **str** | User full name | [optional] 
**notes** | **str** | User notes | [optional] 
**state_code** | **str** | User state code (ISO-3166 Alpha-2 format) | [optional] 
**welcome_email_sent_at** | **datetime** | User welcome email sent at | [optional] 
**zip** | **str** | User zip code | [optional] 
**origin_id** | **str** | User origin id | [optional] 
**origin_data** | **str** | User origin data | [optional] 
**created_at** | **datetime** | User created at | [optional] 
**updated_at** | **datetime** | User updated at | [optional] 
**vendor** | [**Compact**](Compact.md) |  | [optional] 
**is_insurance_manager** | **bool** | User employee status | [optional] 
**party_id** | **int** | Party id | [optional] 
**work_classification_id** | **int** | Work classification id | [optional] 
**default_permission_template_id** | **int** | User default permission template id | [optional] 
**permission_template** | [**CompanyUser6AllOfPermissionTemplate**](CompanyUser6AllOfPermissionTemplate.md) |  | [optional] 
**company_permission_template_id** | **int** | User&#39;s Company Permission Template id | [optional] 
**business_id** | **str** | Business id | [optional] 
**login_information_uuid** | **str** | Login information uuid | [optional] 

## Example

```python
from procore_sdk.models.company_user6 import CompanyUser6

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyUser6 from a JSON string
company_user6_instance = CompanyUser6.from_json(json)
# print the JSON string representation of the object
print(CompanyUser6.to_json())

# convert the object into a dict
company_user6_dict = company_user6_instance.to_dict()
# create an instance of CompanyUser6 from a dict
company_user6_from_dict = CompanyUser6.from_dict(company_user6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


