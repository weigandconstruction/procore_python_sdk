# InactiveUser

Inactive User

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address of the user. | [optional] 
**avatar** | **str** | The URL pointing to the user avatar. | [optional] 
**business_id** | **str** | Business id | [optional] 
**business_phone** | **str** | The business phone number of the user. | [optional] 
**business_phone_extension** | **int** | The business phone extension of the user. | [optional] 
**city** | **str** | The city that applies to the user. | [optional] 
**country_code** | **str** | The country code that applies to the user, must be in ISO-3166 Alpha-2 format. | [optional] 
**email_address** | **str** | The email address of the user. | [optional] 
**email_signature** | **str** | The email signature of the user. | [optional] 
**employee_id** | **str** | The unique employee identifier of the user. | [optional] 
**erp_integrated_accountant** | **bool** | If this property is set to true, the user is an ERP-integrated accountant, if this property is set to false, the user is not an ERP-integrated accountant. | [optional] 
**fax_number** | **str** | The fax number of the user. | [optional] 
**first_name** | **str** | The first name of the user. | [optional] 
**id** | **int** | The unique idenfier of the user. | [optional] 
**initials** | **str** | The initials of the user. | [optional] 
**is_active** | **bool** | If this property is set to true, the user status is active. If this property is set to false, the user status is inactive. | [optional] 
**is_employee** | **bool** | If this property is set to true, the user is an employee. If this property is set to false, the user is not an employee. | [optional] 
**job_title** | **str** | The job title of the user. | [optional] 
**last_login_at** | **datetime** | The date and time when the user logged in last. | [optional] 
**last_name** | **str** | The last name of the user. | [optional] 
**mobile_phone** | **str** | The mobile phone number of the user. | [optional] 
**name** | **str** | The full name of the user. | [optional] 
**notes** | **str** | The user notes. | [optional] 
**state_code** | **str** | The state code that applies to the user. Must be in ISO-3166 Alpha-2 format. | [optional] 
**welcome_email_sent_at** | **datetime** | The date and time when the welcome email was sent to the user. | [optional] 
**zip** | **str** | The ZIP code of the user. | [optional] 
**origin_id** | **str** | The unique idenfitier for the user origin. | [optional] 
**origin_data** | **str** | User origin data. | [optional] 
**created_at** | **datetime** | The date and time when the user was created in the system. | [optional] 
**updated_at** | **datetime** | The date and time when the user was updated in the system. | [optional] 
**vendor** | [**RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor**](RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor.md) |  | [optional] 
**links** | [**InactiveUserAllOfLinks**](InactiveUserAllOfLinks.md) |  | [optional] 

## Example

```python
from procore_sdk.models.inactive_user import InactiveUser

# TODO update the JSON string below
json = "{}"
# create an instance of InactiveUser from a JSON string
inactive_user_instance = InactiveUser.from_json(json)
# print the JSON string representation of the object
print(InactiveUser.to_json())

# convert the object into a dict
inactive_user_dict = inactive_user_instance.to_dict()
# create an instance of InactiveUser from a dict
inactive_user_from_dict = InactiveUser.from_dict(inactive_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


