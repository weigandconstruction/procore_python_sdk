# ChecklistTemplate2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**synced_to** | [**ChecklistTemplate1SyncedTo**](ChecklistTemplate1SyncedTo.md) |  | [optional] 
**company_description** | **str** | Company level inspection template description | [optional] 
**description** | **str** | Description | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 
**alternative_response_set_id** | **int** | The ID of the associated Alternative Response Set (if null, the default response set is being used) | [optional] 
**sections** | [**List[ChecklistTemplateSection]**](ChecklistTemplateSection.md) | Checklist Sections | [optional] 
**inspection_type** | [**InspectionType2**](InspectionType2.md) |  | [optional] 
**trade** | [**Trade**](Trade.md) |  | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**company_attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) | Company Attachments | [optional] 
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) | Attachments | [optional] 
**response_set** | [**ChecklistDefaultResponseSet**](ChecklistDefaultResponseSet.md) |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_template2 import ChecklistTemplate2

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistTemplate2 from a JSON string
checklist_template2_instance = ChecklistTemplate2.from_json(json)
# print the JSON string representation of the object
print(ChecklistTemplate2.to_json())

# convert the object into a dict
checklist_template2_dict = checklist_template2_instance.to_dict()
# create an instance of ChecklistTemplate2 from a dict
checklist_template2_from_dict = ChecklistTemplate2.from_dict(checklist_template2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


