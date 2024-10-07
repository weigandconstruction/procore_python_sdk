# TimeAndMaterialEntry2

Time and Material Entry Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_and_material_entry_ids** | **List[int]** | ID&#39;s of the Time And Material Entry Objects to be updated | [optional] 
**change_event_id** | **int** | Associated Change Event ID | [optional] 
**update_change_event_attachment** | **bool** | Will the attachments need to be updated | [optional] 

## Example

```python
from procore_sdk.models.time_and_material_entry2 import TimeAndMaterialEntry2

# TODO update the JSON string below
json = "{}"
# create an instance of TimeAndMaterialEntry2 from a JSON string
time_and_material_entry2_instance = TimeAndMaterialEntry2.from_json(json)
# print the JSON string representation of the object
print(TimeAndMaterialEntry2.to_json())

# convert the object into a dict
time_and_material_entry2_dict = time_and_material_entry2_instance.to_dict()
# create an instance of TimeAndMaterialEntry2 from a dict
time_and_material_entry2_from_dict = TimeAndMaterialEntry2.from_dict(time_and_material_entry2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


