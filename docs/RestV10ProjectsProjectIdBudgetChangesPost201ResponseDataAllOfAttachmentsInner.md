# RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfAttachmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prostore_file_id** | **int** | Unique identifier of the attached file | [optional] 
**name** | **str** | Base name of the file without its path | [optional] 
**url** | **str** | URL to download the attached file. HTTP client should be prepared to follow redirects to successfully download the file. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_budget_changes_post201_response_data_all_of_attachments_inner import RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfAttachmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfAttachmentsInner from a JSON string
rest_v10_projects_project_id_budget_changes_post201_response_data_all_of_attachments_inner_instance = RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfAttachmentsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfAttachmentsInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_budget_changes_post201_response_data_all_of_attachments_inner_dict = rest_v10_projects_project_id_budget_changes_post201_response_data_all_of_attachments_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfAttachmentsInner from a dict
rest_v10_projects_project_id_budget_changes_post201_response_data_all_of_attachments_inner_from_dict = RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfAttachmentsInner.from_dict(rest_v10_projects_project_id_budget_changes_post201_response_data_all_of_attachments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


