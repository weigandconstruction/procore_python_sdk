# ProjectUser1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abbreviated_name** | **str** | The Initials of the Project User | [optional] 
**address** | **str** | The street Address of the Project User | [optional] 
**avatar** | **str** | Project User Avatar. To upload avatar you must upload whole payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;user[avatar]&#x60; as file. | [optional] 
**business_phone** | **str** | The Business Phone number of the Project User | [optional] 
**business_phone_extension** | **int** | The Business Phone Extension of the Project User | [optional] 
**city** | **str** | The City in which the Project User resides | [optional] 
**country_code** | **str** | The Country Code of the Project User (ISO-3166 Alpha-2 format) | [optional] 
**email_address** | **str** | The Email Address of the Project User | [optional] 
**email_signature** | **str** | The Email Signature of the Project User | [optional] 
**employee_id** | **str** | The Employee ID of the Project User | [optional] 
**fax_number** | **str** | The Fax Number of the Project User | [optional] 
**first_name** | **str** | The First Name of the Project User | [optional] 
**is_active** | **bool** | The Active status of the Project User | [optional] 
**is_employee** | **bool** | The Employee status of the Project User | [optional] [default to False]
**job_title** | **str** | The Job Title of the Project User | [optional] 
**last_name** | **str** | The Last Name of the Project User | [optional] 
**mobile_phone** | **str** | The Mobile Phone number of the Project User | [optional] 
**notes** | **str** | The Notes (notes/keywords/tags) of the Project User | [optional] 
**state_code** | **str** | The State Code of the Project User (ISO-3166 Alpha-2 format) | [optional] 
**vendor_id** | **int** | The Vendor ID of the Project User | [optional] 
**zip** | **str** | The Zip Code of the Project User | [optional] 

## Example

```python
from procore_sdk.models.project_user1 import ProjectUser1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectUser1 from a JSON string
project_user1_instance = ProjectUser1.from_json(json)
# print the JSON string representation of the object
print(ProjectUser1.to_json())

# convert the object into a dict
project_user1_dict = project_user1_instance.to_dict()
# create an instance of ProjectUser1 from a dict
project_user1_from_dict = ProjectUser1.from_dict(project_user1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


