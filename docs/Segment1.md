# Segment1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Segment Name | [optional] 
**project_can_modify_origin_project** | **bool** | Whether project-specific Segment Items are able to be added/edited/removed from a Project. | [optional] 
**project_can_delete_origin_company** | **bool** | Whether Segment Items inherited from the company-level are able to be deleted from a Project. | [optional] 

## Example

```python
from procore_sdk.models.segment1 import Segment1

# TODO update the JSON string below
json = "{}"
# create an instance of Segment1 from a JSON string
segment1_instance = Segment1.from_json(json)
# print the JSON string representation of the object
print(Segment1.to_json())

# convert the object into a dict
segment1_dict = segment1_instance.to_dict()
# create an instance of Segment1 from a dict
segment1_from_dict = Segment1.from_dict(segment1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


