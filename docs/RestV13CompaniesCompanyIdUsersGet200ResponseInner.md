# RestV13CompaniesCompanyIdUsersGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | User address | [optional] 
**avatar** | **str** | User avatar url | [optional] 
**business_id** | **str** | Business id | [optional] 
**business_phone** | **str** | User business phone | [optional] 
**business_phone_extension** | **int** | User business phone extension | [optional] 
**city** | **str** | User city | [optional] 
**contact_id** | **int** | User Contact ID | [optional] 
**country_code** | **str** | User country code (ISO-3166 Alpha-2 format) | [optional] 
**created_at** | **datetime** | User created at | [optional] 
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
**origin_id** | **str** | User origin id | [optional] 
**origin_data** | **str** | User origin data | [optional] 
**state_code** | **str** | User state code (ISO-3166 Alpha-2 format) | [optional] 
**updated_at** | **datetime** | User updated at | [optional] 
**welcome_email_sent_at** | **datetime** | User welcome email sent at | [optional] 
**zip** | **str** | User zip code | [optional] 
**work_classification_id** | **int** | Work classification id | [optional] 
**permission_template** | [**CompanyUserPermissionTemplate**](CompanyUserPermissionTemplate.md) |  | [optional] 
**company_permission_template** | [**CompanyUserPermissionTemplate**](CompanyUserPermissionTemplate.md) |  | [optional] 
**vendor** | [**RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200ResponseVendor**](RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200ResponseVendor.md) |  | [optional] 
**role** | **str** | Role of the User | [optional] 
**verified_employee** | **bool** | If a user is a verified employee | [optional] 

## Example

```python
from procore_sdk.models.rest_v13_companies_company_id_users_get200_response_inner import RestV13CompaniesCompanyIdUsersGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV13CompaniesCompanyIdUsersGet200ResponseInner from a JSON string
rest_v13_companies_company_id_users_get200_response_inner_instance = RestV13CompaniesCompanyIdUsersGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV13CompaniesCompanyIdUsersGet200ResponseInner.to_json())

# convert the object into a dict
rest_v13_companies_company_id_users_get200_response_inner_dict = rest_v13_companies_company_id_users_get200_response_inner_instance.to_dict()
# create an instance of RestV13CompaniesCompanyIdUsersGet200ResponseInner from a dict
rest_v13_companies_company_id_users_get200_response_inner_from_dict = RestV13CompaniesCompanyIdUsersGet200ResponseInner.from_dict(rest_v13_companies_company_id_users_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


