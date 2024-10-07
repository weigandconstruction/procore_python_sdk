# RestV10ProjectsProjectIdPeopleGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | [**NormalContact**](NormalContact.md) |  | [optional] 
**employee_id** | **str** | Employee ID for the Project Person | [optional] 
**first_name** | **str** | Project Person first name | [optional] 
**id** | **int** | Unique identifier for the Project Person. | [optional] 
**is_employee** | **bool** | Employee status for the Project Person | [optional] 
**last_name** | **str** | Project Person last name | [optional] 
**user_id** | **int** | User ID if this Project Person represents a User. NULL for a Reference User. | [optional] 
**user_uuid** | **int** | The user UUID for if this Company Person represents a user. This value is set to NULL for a Reference User. | [optional] 
**work_classification_id** | **int** | Work Classification ID for the Project Person | [optional] 
**origin_id** | **int** | The ID of the External Data associated with the Project Person | [optional] 
**work_classification** | [**ExtendedViewWorkClassification**](ExtendedViewWorkClassification.md) |  | [optional] 
**vendor** | [**Compact**](Compact.md) |  | [optional] 
**initials** | **str** | Initials of the Project Person | [optional] 
**avatar** | **str** | URL to the avatar of the Project Person | [optional] 
**reference_user** | **bool** | Whether the Project Person is a Reference User | [optional] 
**created_at** | **datetime** | Date and time the Project Person was created | [optional] 
**updated_at** | **datetime** | Date and time the Project Person was last updated | [optional] 
**email** | **str** | The email address of the Project Person | [optional] 
**mobile_phone** | **str** | The mobile phone number of the Project Person | [optional] 
**business_phone** | **str** | The business phone number of the Project Person | [optional] 
**job_title** | **str** | The job title of the Project Person | [optional] 
**fax_number** | **str** | The fax number of the Project Person | [optional] 
**address** | **str** | The address of the Project Person | [optional] 
**city** | **str** | The city of the Project Person | [optional] 
**country_code** | **str** | The country code of the Project Person | [optional] 
**state_code** | **str** | The state code of the Project Person | [optional] 
**zip** | **str** | The zip code of the Project Person | [optional] 
**connected** | **bool** | Whether the Project Person is connected to the user | [optional] 
**last_login_at** | **datetime** | Date and time the Project Person last logged in | [optional] 
**welcome_email_sent_at** | **datetime** | Date and time the welcome email was sent to the Project Person | [optional] 
**erp_integrated_accountant** | **bool** | Whether the Project Person is an ERP Integrated Accountant | [optional] 
**permission_template** | [**WebViewPermissionTemplate**](WebViewPermissionTemplate.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_people_get200_response_inner import RestV10ProjectsProjectIdPeopleGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdPeopleGet200ResponseInner from a JSON string
rest_v10_projects_project_id_people_get200_response_inner_instance = RestV10ProjectsProjectIdPeopleGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdPeopleGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_people_get200_response_inner_dict = rest_v10_projects_project_id_people_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdPeopleGet200ResponseInner from a dict
rest_v10_projects_project_id_people_get200_response_inner_from_dict = RestV10ProjectsProjectIdPeopleGet200ResponseInner.from_dict(rest_v10_projects_project_id_people_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


