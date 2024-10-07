# TheGenericToolItemObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the generic tool item. | [optional] 
**due_date** | **date** | The due date for the generic tool item. | [optional] 
**position** | **str** | The position/number of the generic tool item. | [optional] 
**private** | **bool** | If this property is set to true, the generic tool item is private. If this property is set to false, the generic tool item is not private. | [optional] 
**skip_emails** | **bool** | If true creating and updating the item will not send emails to the users on the item. | [optional] 
**schedule_impact** | **str** | The schedule impact status for the generic tool item. | [optional] 
**schedule_impact_value** | **str** | Specifies a value for the schedue impact of the generic tool item. | [optional] 
**cost_impact** | **str** | The cost impact of the generic tool item. | [optional] 
**cost_impact_value** | **str** | Specifies a value for the cost impact of the generic tool item. | [optional] 
**status** | **str** | The status of the generic tool item. | [optional] 
**title** | **str** | The title of the generic tool item. | [optional] 
**received_from_id** | **int** | The unique identifier for the Received From entity. | [optional] 
**location_id** | **int** | The location identifier for the generic tool item. | [optional] 
**cost_code_id** | **int** | The cost code identifier for the generic tool item. | [optional] 
**specification_section_id** | **int** | The specification section identifier for the generic tool item. | [optional] 
**trade_id** | **int** | The trade identifier for the generic tool item. | [optional] 
**distribution_member_ids** | **List[int]** | An array of distribution member identifiers for the generic tool item. | [optional] 
**assignee_ids** | **List[int]** | An array of assignee identifiers for the generic tool item. | [optional] 
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) | Specifies an array of generic tool item attachments. To upload attachments you must upload the entire payload as a &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 
**drawing_revision_ids** | **List[int]** | Drawing Revisions to attach to the response | [optional] 
**file_version_ids** | **List[int]** | File Versions to attach to the response | [optional] 
**form_ids** | **List[int]** | Forms to attach to the response | [optional] 
**image_ids** | **List[int]** | Images to attach to the response | [optional] 
**upload_ids** | **List[str]** | Uploads to attach to the response | [optional] 

## Example

```python
from procore_sdk.models.the_generic_tool_item_object import TheGenericToolItemObject

# TODO update the JSON string below
json = "{}"
# create an instance of TheGenericToolItemObject from a JSON string
the_generic_tool_item_object_instance = TheGenericToolItemObject.from_json(json)
# print the JSON string representation of the object
print(TheGenericToolItemObject.to_json())

# convert the object into a dict
the_generic_tool_item_object_dict = the_generic_tool_item_object_instance.to_dict()
# create an instance of TheGenericToolItemObject from a dict
the_generic_tool_item_object_from_dict = TheGenericToolItemObject.from_dict(the_generic_tool_item_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


