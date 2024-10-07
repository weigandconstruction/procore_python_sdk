# RestV10ProjectsProjectIdUsersGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | User first name | [optional] 
**id** | **int** | User id | [optional] 
**initials** | **str** | User initials | [optional] 
**last_name** | **str** | User last name | [optional] 
**name** | **str** | User full name | [optional] 
**vendor** | [**RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200ResponseVendor**](RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200ResponseVendor.md) |  | [optional] 
**address** | **str** | User address | [optional] 
**avatar** | **str** | User avatar url | [optional] 
**business_id** | **str** | Business id | [optional] 
**business_phone** | **str** | User business phone | [optional] 
**business_phone_extension** | **int** | User business phone extension | [optional] 
**city** | **str** | User city | [optional] 
**country_code** | **str** | User country code (ISO-3166 Alpha-2 format) | [optional] 
**email_address** | **str** | User email | [optional] 
**email_signature** | **str** | User email signature | [optional] 
**employee_id** | **str** | User employee id | [optional] 
**erp_integrated_accountant** | **bool** | User ERP integrated accountant status | [optional] 
**fax_number** | **str** | User fax number | [optional] 
**is_active** | **bool** | User active status | [optional] 
**is_employee** | **bool** | User employee status | [optional] 
**job_title** | **str** | User job title | [optional] 
**last_login_at** | **datetime** | User last login at | [optional] 
**mobile_phone** | **str** | User mobile phone | [optional] 
**notes** | **str** | User notes | [optional] 
**state_code** | **str** | User state code (ISO-3166 Alpha-2 format) | [optional] 
**welcome_email_sent_at** | **datetime** | User welcome email sent at | [optional] 
**zip** | **str** | User zip code | [optional] 
**origin_id** | **str** | User origin id | [optional] 
**origin_data** | **str** | User origin data | [optional] 
**created_at** | **datetime** | User created at | [optional] 
**updated_at** | **datetime** | User updated at | [optional] 
**contact_id** | **int** |  | [optional] 
**work_classification_id** | **int** | Work classification id | [optional] 
**permission_template** | [**NormalViewPermissionTemplate**](NormalViewPermissionTemplate.md) |  | [optional] 
**company_permission_template** | [**NormalViewCompanyPermissionTemplate**](NormalViewCompanyPermissionTemplate.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_users_get200_response_inner import RestV10ProjectsProjectIdUsersGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdUsersGet200ResponseInner from a JSON string
rest_v10_projects_project_id_users_get200_response_inner_instance = RestV10ProjectsProjectIdUsersGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdUsersGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_users_get200_response_inner_dict = rest_v10_projects_project_id_users_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdUsersGet200ResponseInner from a dict
rest_v10_projects_project_id_users_get200_response_inner_from_dict = RestV10ProjectsProjectIdUsersGet200ResponseInner.from_dict(rest_v10_projects_project_id_users_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


