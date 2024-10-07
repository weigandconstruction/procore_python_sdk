# RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**business_phone** | **str** |  | [optional] 
**business_phone_extension** | **int** |  | [optional] 
**email** | **str** |  | [optional] 
**fax_number** | **str** |  | [optional] 
**job_title** | **str** |  | [optional] 
**login_information_id** | **int** |  | [optional] 
**mobile_phone** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**vendor_name** | **str** |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_manpower_logs_get200_response_inner_contact import RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerContact

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerContact from a JSON string
rest_v10_projects_project_id_manpower_logs_get200_response_inner_contact_instance = RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerContact.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerContact.to_json())

# convert the object into a dict
rest_v10_projects_project_id_manpower_logs_get200_response_inner_contact_dict = rest_v10_projects_project_id_manpower_logs_get200_response_inner_contact_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerContact from a dict
rest_v10_projects_project_id_manpower_logs_get200_response_inner_contact_from_dict = RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerContact.from_dict(rest_v10_projects_project_id_manpower_logs_get200_response_inner_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


