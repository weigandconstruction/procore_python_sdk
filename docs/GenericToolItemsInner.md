# GenericToolItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique idenfitier of the generic tool item. | 
**due_date** | **date** | The due date for the generic tool item. | [optional] 
**private** | **bool** | If this property is set to true, the generic tool item is private. If this property is set to false, the generic tool item is not private. | [optional] 
**schedule_impact** | **str** | The schedule impact of the generic tool item. | [optional] 
**cost_impact** | **str** | The cost impact of the generic tool item. | [optional] 
**status** | **str** | The status of the generic tool item. | [optional] 
**assignee_ids** | **List[int]** |  | [optional] 
**received_from_id** | **int** | The unique identifier for the Received From entity for the generic tool item. | [optional] 
**location_id** | **int** | The location identifier for the generic tool item. | [optional] 
**cost_code_id** | **int** | The cost code identifier for the generic tool item. | [optional] 
**specification_section_id** | **int** | The specification section identifier for the generic tool item. | [optional] 
**sub_job_id** | **int** | The sub job identifier for the generic tool item. | [optional] 
**trade_ids** | **List[int]** |  | [optional] 
**task_ids** | **List[int]** |  | [optional] 

## Example

```python
from procore_sdk.models.generic_tool_items_inner import GenericToolItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GenericToolItemsInner from a JSON string
generic_tool_items_inner_instance = GenericToolItemsInner.from_json(json)
# print the JSON string representation of the object
print(GenericToolItemsInner.to_json())

# convert the object into a dict
generic_tool_items_inner_dict = generic_tool_items_inner_instance.to_dict()
# create an instance of GenericToolItemsInner from a dict
generic_tool_items_inner_from_dict = GenericToolItemsInner.from_dict(generic_tool_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


