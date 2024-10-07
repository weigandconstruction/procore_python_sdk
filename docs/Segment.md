# Segment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Segment Name | 
**project_can_modify_origin_project** | **bool** | Whether project-specific Segment Items are able to be added/edited/removed from a Project. | [optional] 
**project_can_delete_origin_company** | **bool** | Whether Segment Items inherited from the company-level are able to be deleted from a Project. | [optional] 
**structure** | **str** | The Structure for this Wbs Segment. | 

## Example

```python
from procore_sdk.models.segment import Segment

# TODO update the JSON string below
json = "{}"
# create an instance of Segment from a JSON string
segment_instance = Segment.from_json(json)
# print the JSON string representation of the object
print(Segment.to_json())

# convert the object into a dict
segment_dict = segment_instance.to_dict()
# create an instance of Segment from a dict
segment_from_dict = Segment.from_dict(segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


