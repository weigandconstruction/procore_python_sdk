# ChecklistTemplate1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**synced_to** | [**ChecklistTemplate1SyncedTo**](ChecklistTemplate1SyncedTo.md) |  | [optional] 
**company_description** | **str** | Company Checklist Template description | [optional] 
**description** | **str** | Description | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 
**inspection_type** | [**InspectionType2**](InspectionType2.md) |  | [optional] 
**trade** | [**Trade**](Trade.md) |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_template1 import ChecklistTemplate1

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistTemplate1 from a JSON string
checklist_template1_instance = ChecklistTemplate1.from_json(json)
# print the JSON string representation of the object
print(ChecklistTemplate1.to_json())

# convert the object into a dict
checklist_template1_dict = checklist_template1_instance.to_dict()
# create an instance of ChecklistTemplate1 from a dict
checklist_template1_from_dict = ChecklistTemplate1.from_dict(checklist_template1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


