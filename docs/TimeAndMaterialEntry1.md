# TimeAndMaterialEntry1

Time and Material Entry Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The title of T&amp;M ticket | [optional] 
**reference_number** | **str** | The refrence number associate with T&amp;M ticket | [optional] 
**description** | **str** | The description of job | [optional] 
**status** | **str** | Current status of T&amp;M ticket | [optional] 
**private** | **bool** | If the T&amp;M ticket is private | [optional] 
**number** | **int** | Unique number for the T&amp;M ticket | [optional] 
**customer_signature_id** | **int** | The ID associate with customer&#39;s signature | [optional] 
**company_signature_id** | **int** | The ID associate with company&#39;s signature | [optional] 
**company_signee_party_id** | **int** | The ID associate with company&#39;s signature party | [optional] 
**customer_signee_party_id** | **int** | The ID associate with customer&#39;s signature party | [optional] 
**work_performed_on_date** | **str** | Date work performed on | [optional] 
**drawing_revision_ids** | **List[int]** | Drawing Revisions to attach to the response | [optional] 
**file_version_ids** | **List[int]** | File Versions to attach to the response | [optional] 
**form_ids** | **List[int]** | Forms to attach to the response | [optional] 
**image_ids** | **List[int]** | Images to attach to the response | [optional] 

## Example

```python
from procore_sdk.models.time_and_material_entry1 import TimeAndMaterialEntry1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeAndMaterialEntry1 from a JSON string
time_and_material_entry1_instance = TimeAndMaterialEntry1.from_json(json)
# print the JSON string representation of the object
print(TimeAndMaterialEntry1.to_json())

# convert the object into a dict
time_and_material_entry1_dict = time_and_material_entry1_instance.to_dict()
# create an instance of TimeAndMaterialEntry1 from a dict
time_and_material_entry1_from_dict = TimeAndMaterialEntry1.from_dict(time_and_material_entry1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


