# RestV11ProjectsProjectIdChecklistListsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_template_id** | **int** | ID of the Checklist List Template (Inspection Template) that the Checklist (Inspection) will be created from | 
**list** | [**RestV11ProjectsProjectIdChecklistListsPostRequestList**](RestV11ProjectsProjectIdChecklistListsPostRequestList.md) |  | 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_checklist_lists_post_request import RestV11ProjectsProjectIdChecklistListsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdChecklistListsPostRequest from a JSON string
rest_v11_projects_project_id_checklist_lists_post_request_instance = RestV11ProjectsProjectIdChecklistListsPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdChecklistListsPostRequest.to_json())

# convert the object into a dict
rest_v11_projects_project_id_checklist_lists_post_request_dict = rest_v11_projects_project_id_checklist_lists_post_request_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdChecklistListsPostRequest from a dict
rest_v11_projects_project_id_checklist_lists_post_request_from_dict = RestV11ProjectsProjectIdChecklistListsPostRequest.from_dict(rest_v11_projects_project_id_checklist_lists_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


