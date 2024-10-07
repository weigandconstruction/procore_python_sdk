# ProjectChecklistTemplate1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**company_description** | **str** | Company Description | [optional] 
**description** | **str** | Description | [optional] 
**inspection_type** | [**InspectionType**](InspectionType.md) |  | [optional] 
**trade** | [**Trade**](Trade.md) |  | [optional] 
**synced_to** | [**ProjectChecklistTemplate1SyncedTo**](ProjectChecklistTemplate1SyncedTo.md) |  | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 

## Example

```python
from procore_sdk.models.project_checklist_template1 import ProjectChecklistTemplate1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectChecklistTemplate1 from a JSON string
project_checklist_template1_instance = ProjectChecklistTemplate1.from_json(json)
# print the JSON string representation of the object
print(ProjectChecklistTemplate1.to_json())

# convert the object into a dict
project_checklist_template1_dict = project_checklist_template1_instance.to_dict()
# create an instance of ProjectChecklistTemplate1 from a dict
project_checklist_template1_from_dict = ProjectChecklistTemplate1.from_dict(project_checklist_template1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


