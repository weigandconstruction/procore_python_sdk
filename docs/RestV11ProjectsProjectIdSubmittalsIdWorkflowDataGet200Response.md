# RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**steps** | [**List[RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseStepsInner]**](RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseStepsInner.md) |  | [optional] 
**approvers** | [**List[RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseApproversInner]**](RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseApproversInner.md) |  | [optional] 
**attachments** | [**List[RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseAttachmentsInner]**](RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseAttachmentsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_submittals_id_workflow_data_get200_response import RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200Response from a JSON string
rest_v11_projects_project_id_submittals_id_workflow_data_get200_response_instance = RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200Response.to_json())

# convert the object into a dict
rest_v11_projects_project_id_submittals_id_workflow_data_get200_response_dict = rest_v11_projects_project_id_submittals_id_workflow_data_get200_response_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200Response from a dict
rest_v11_projects_project_id_submittals_id_workflow_data_get200_response_from_dict = RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200Response.from_dict(rest_v11_projects_project_id_submittals_id_workflow_data_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


