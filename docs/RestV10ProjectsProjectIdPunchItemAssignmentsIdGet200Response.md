# RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**approved** | **bool** | Resolution status | [optional] 
**status** | **str** | Status of Assignment | [optional] 
**name** | **str** | Assignment&#39;s name | [optional] 
**comment** | **str** | Comment | [optional] 
**login_information_id** | **int** |  | [optional] 
**login_information_name** | **str** |  | [optional] 
**login_information** | [**RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200ResponseLoginInformation**](RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200ResponseLoginInformation.md) |  | [optional] 
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) |  | [optional] 
**vendor** | [**RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200ResponseVendor**](RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200ResponseVendor.md) |  | [optional] 
**notified_at** | **str** | Date assignee was notified of Punch Item | [optional] 
**responded_at** | **str** | Date Assignee responded to the Punch Item | [optional] 
**manager_accepted_at** | **str** | Date Punch Item Manager resolved the Punch Item Assignment | [optional] 
**user_name** | **str** |  | [optional] 
**updated_at** | **str** | Date Assignment was updated | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_punch_item_assignments_id_get200_response import RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200Response from a JSON string
rest_v10_projects_project_id_punch_item_assignments_id_get200_response_instance = RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200Response.to_json())

# convert the object into a dict
rest_v10_projects_project_id_punch_item_assignments_id_get200_response_dict = rest_v10_projects_project_id_punch_item_assignments_id_get200_response_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200Response from a dict
rest_v10_projects_project_id_punch_item_assignments_id_get200_response_from_dict = RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200Response.from_dict(rest_v10_projects_project_id_punch_item_assignments_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


