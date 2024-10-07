# ProjectChecklistTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**deletable** | **bool** | Deletable | [optional] 
**company_description** | **str** | Company Description | [optional] 
**description** | **str** | Description | [optional] 
**trade** | [**Trade**](Trade.md) |  | [optional] 
**synced_to** | [**ProjectChecklistTemplateSyncedTo**](ProjectChecklistTemplateSyncedTo.md) |  | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 

## Example

```python
from procore_sdk.models.project_checklist_template import ProjectChecklistTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectChecklistTemplate from a JSON string
project_checklist_template_instance = ProjectChecklistTemplate.from_json(json)
# print the JSON string representation of the object
print(ProjectChecklistTemplate.to_json())

# convert the object into a dict
project_checklist_template_dict = project_checklist_template_instance.to_dict()
# create an instance of ProjectChecklistTemplate from a dict
project_checklist_template_from_dict = ProjectChecklistTemplate.from_dict(project_checklist_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


