# ChecklistTemplate4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**description** | **str** | Description | [optional] 
**company_description** | **str** | Company level inspection template description | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 
**inspection_type** | [**ChecklistTemplate4InspectionType**](ChecklistTemplate4InspectionType.md) |  | [optional] 
**alternative_response_set_id** | **int** | The ID of the associated Alternative Response Set (if null, the default response set is being used) | [optional] 
**response_set** | [**ChecklistDefaultResponseSet**](ChecklistDefaultResponseSet.md) |  | [optional] 
**location** | [**ChecklistTemplate4Location**](ChecklistTemplate4Location.md) |  | [optional] 
**trade** | [**Trade2**](Trade2.md) |  | [optional] 
**created_by** | [**RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy**](RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy.md) |  | [optional] 
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) | Attachments | [optional] 
**sections** | [**List[ChecklistTemplate4SectionsInner]**](ChecklistTemplate4SectionsInner.md) | Checklist Sections | [optional] 

## Example

```python
from procore_sdk.models.checklist_template4 import ChecklistTemplate4

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistTemplate4 from a JSON string
checklist_template4_instance = ChecklistTemplate4.from_json(json)
# print the JSON string representation of the object
print(ChecklistTemplate4.to_json())

# convert the object into a dict
checklist_template4_dict = checklist_template4_instance.to_dict()
# create an instance of ChecklistTemplate4 from a dict
checklist_template4_from_dict = ChecklistTemplate4.from_dict(checklist_template4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


