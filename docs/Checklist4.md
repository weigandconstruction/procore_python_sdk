# Checklist4

Checklist object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The Description of the Checklist | [optional] 
**due_at** | **datetime** | Timestamp indicating when the Inspection is due. | [optional] 
**inspection_date** | **date** | The Inspection Date of the Checklist | [optional] 
**inspection_type_id** | **int** | The ID of the Checklist&#39;s Type | [optional] 
**point_of_contact_id** | **int** | The ID of the Checklist&#39;s Point of Contact | [optional] 
**inspectee_id** | **int** | The ID of the Checklist&#39;s Inspectee | [optional] 
**name** | **str** | The Name of the Checklist | [optional] 
**number** | **int** | The Number of the Checklist | [optional] 
**personal** | **bool** | The Personal status of the Checklist | [optional] [default to True]
**responsible_contractor_id** | **int** | The ID of the Checklist&#39;s Responsible Contractor | [optional] 
**spec_section_id** | **int** | The ID of the Checklist&#39;s Specification Section | [optional] 
**status** | **str** | The Status of the Checklist | [optional] 
**trade_id** | **int** | The ID of the Checklist&#39;s Trade | [optional] 
**sections_attributes** | [**List[Checklist4AllOfSectionsAttributesInner]**](Checklist4AllOfSectionsAttributesInner.md) | An array of hashes of the Checklist&#39;s Section attributes | [optional] 
**inspector_ids** | **List[int]** | An Array of the IDs of the Inspectors | [optional] 
**distribution_member_ids** | **List[int]** | An Array of the IDs of the Distribution Members | [optional] 
**location_id** | **int** | The ID of the Location of the Checklist. &#x60;location_id&#x60; takes precedence over &#x60;mt_location | [optional] 
**mt_location** | **List[str]** | Use for creating a new multi-tier or single-tier Location. Will be ignored if &#x60;location_id&#x60; is provided | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 
**drawing_revision_ids** | **List[int]** | Drawing Revisions to attach to the response | [optional] 
**file_version_ids** | **List[int]** | File Versions to attach to the response | [optional] 
**form_ids** | **List[int]** | Forms to attach to the response | [optional] 
**image_ids** | **List[int]** | Images to attach to the response | [optional] 
**upload_ids** | **List[str]** | Uploads to attach to the response | [optional] 

## Example

```python
from procore_sdk.models.checklist4 import Checklist4

# TODO update the JSON string below
json = "{}"
# create an instance of Checklist4 from a JSON string
checklist4_instance = Checklist4.from_json(json)
# print the JSON string representation of the object
print(Checklist4.to_json())

# convert the object into a dict
checklist4_dict = checklist4_instance.to_dict()
# create an instance of Checklist4 from a dict
checklist4_from_dict = Checklist4.from_dict(checklist4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


